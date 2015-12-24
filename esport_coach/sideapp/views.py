"""
this file calls all page functions and renders the pages with given context.
"""
from .forms import SignupForm, ContactForm, SalePaymentForm
from .models import Signup, Reviews, Coach, User
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core import serializers
from django.db.models import Count


def home(request):
    title = 'Welcome'
    form = SignupForm(request.POST or None)
    context = {"title": title, "form": form}

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {"title": "Signup Succesful"}
    return render(request, "home.html", context)


def logout(request):
    auth_logout(request)
    return redirect('/')


def contact(request):
    """
    Contact function which creates a contact
    form with some context and renders it.
    """
    form = ContactForm(request.POST)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        message = request.POST.get('message', '')
        #message = form.cleaned_data.get('messsage')
        #print(message)
        username = form.cleaned_data.get('username')
        subject = 'Customers Enquiries'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, settings.EMAIL_HOST_USER]
        contact_message = "%s: %s via %s"%(username, message, email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)


    context = {"form" : form}
    return render(request, "contact.html", context)


def signup(request):
    title = 'Welcome'
    form = SignupForm(request.POST or None)
    context = {"title": title, "form": form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {"title": "Signup Succesful"}
    return render(request, "forms.html", context)


def list_of_coaches(request):
    coaches_list = []

    all_users = User.objects.all()
    for user in all_users:
        coaches = user.coach_set.all()    # It should always return a query set of one coach instance.
        for coach in coaches:
            reviews = coach.reviewing_set.all()
            avg_review = 0;
            for review in reviews:
                avg_review = int((review.skill_stars+review.communication_stars+review.helpfulness_stars)/3)
            coaches_list.append([user.pname, user.MMR, coach.server, coach.champion, coach.role, avg_review, coach.pricerate, user.userid])

    context = {'coaches': coaches_list}
    return render(request, "listOfCoachesPage.html", context)

def searchCoach(request):
    if request.is_ajax:
        try:
            server = request.GET.get('Server')
            role = request.GET.get('Role')
            hero = request.GET.get('Hero')
            mmrRange = request.GET.get('MMR')
            if (mmrRange == "100-300"):
                minRange = 100
                maxRange = 300
            elif mmrRange == "300-500":
                minRange = 300
                maxRange = 500
            elif mmrRange == "500-700":
                minRange = 500
                maxRange = 700
            elif mmrRange == "700-900":
                minRange = 700
                maxRange = 900
            elif mmrRange == "900-1100":
                minRange = 900
                maxRange = 1100
            elif mmrRange == "1100-1300":
                minRange = 1100
                maxRange = 1300

            coaches = User.objects.filter(MMR__range=(minRange,maxRange)).filter(coach__server=server, coach__champion=hero)

            formData = serializers.serialize('json',coaches)

        except KeyError:
            return HttpResponse('Error')
        return HttpResponse(formData)
    else:
        raise Http404


def tutorselected(request, tutor_username):
    coach_info = []
    avg_review = 0;
    user = User.objects.get(userid=tutor_username)
    coaches = user.coach_set.all()    # It should always return a query set of one coach instance.
    for coach in coaches:
        reviews = coach.reviewing_set.all()
        for review in reviews:
            avg_review = int((review.skill_stars+review.communication_stars+review.helpfulness_stars)/3)
        coach_info = {"pname":user.pname, "mmr":user.MMR, "server":coach.server, "champion":coach.champion, "avg_review":avg_review, "pricerate":coach.pricerate, "skypeid":user.skypeid, "twitchid":user.twitchid, "userid":user.userid}

    context = {
        'coach': coach_info,
        }
    return render(request, "tutorSelectedPage.html", context)


def reviewcoach(request, tutor_username):
    if request.is_ajax:
        # Response messages:
        response_sucess = "Thanks for your honest review!"
        response_error1 = "Error: Must input a comment."
        response_error2 = "Error: Error when sending your review."

        try:
            # For now the reviewer is manually inputed below until we have that global username passed around correctly.
            # reviewer = Signup.objects.get(username=tutor_username)
            user_reviewer = "SomeTutee"
            skill = request.GET.get('ratingSkill')
            communication = request.GET.get('ratingCommunication')
            helpfulness = request.GET.get('ratingHelpfulness')
            review_comment = request.GET.get('textarea_review')

            if skill == "":
                skill == 0
            else:
                skill = int(skill)
            if communication == "":
                communication == 0
            else:
                communication = int(communication)
            if helpfulness == "":
                helpfulness == 0
            else:
                helpfulness = int(helpfulness)
            if review_comment == "":
                return HttpResponse(response_error1)

        except KeyError:
            return HttpResponse(response_error2)

        coach_selected = Signup.objects.get(username=tutor_username)
        all_users_reviews = coach_selected.reviews_set.all()
        rating = Reviews(id=None, coach=coach_selected, reviewer=user_reviewer, skill_stars=skill, communication_stars=communication, helpfulness_stars=helpfulness, comment=review_comment)
        rating.save()
        return HttpResponse(response_sucess)
    else:
        raise Http404

def renderReviews(request,tutor_username):
    if request.is_ajax:
        sum_all_avg_reviews = 0
        num_reviews = 0
        list_reviews = []
        try:
            coach = Coach.objects.get(userid=tutor_username)
            all_users_reviews = coach.reviewing_set.all()
        except KeyError:
            return HttpResponse("error")

        # for user_review in all_users_reviews:
        #     avg_review = int((user_review.skill_stars + user_review.communication_stars + user_review.helpfulness_stars)/3)
        #     # list_reviews.append({"skill":user_review.skill_stars, "communication":user_review.communication_stars, "helpfulness":user_review.helpfulness_stars, "avg_review":avg_review, "comment":user_review.comment,"reviewer":user_review.reviewer})

        response = serializers.serialize('json',all_users_reviews)
        return HttpResponse(response)
    else:
        raise Http404

def paymentpage(request, tutor_username):
    user = User.objects.get(userid=tutor_username)
    coaches = user.coach_set.all()

    for coach in coaches:
        reviews = coach.reviewing_set.all()
        for review in reviews:
            avg_review = int((review.skill_stars+review.communication_stars+review.helpfulness_stars)/3)
        coach_info = {"pname":user.pname, "mmr":user.MMR, "server":coach.server, "champion":coach.champion, "avg_review":avg_review, "pricerate":coach.pricerate, "skypeid":user.skypeid, "twitchid":user.twitchid, "userid":user.userid}

    # if request.is_ajax:
    #     lesson_duration = request.POST['lesson_duration']
    #     lesson_date_time = request.POST['lesson_date_time']

    #     context = lesson_duration + "," + lesson_date_time
    #     return HttpResponse(context)
    # else:
    #     raise Http404
    context = {
        "coach":coach_info,
    }

    return render(request, "summaryReceiptPage.html", context)

def streampage(request, tutor_username):
    user = User.objects.get(userid=tutor_username)
    coaches = user.coach_set.all()

    for coach in coaches:
        reviews = coach.reviewing_set.all()
        for review in reviews:
            avg_review = int((review.skill_stars+review.communication_stars+review.helpfulness_stars)/3)
        coach_info = {"pname":user.pname, "mmr":user.MMR, "server":coach.server, "champion":coach.champion, "avg_review":avg_review, "pricerate":coach.pricerate, "skypeid":user.skypeid, "twitchid":user.twitchid, "userid":user.userid}

    context = {'coach': coach_info}
    return render(request, "streamPage.html", context)


def charge(request):
    form = SalePaymentForm(request.POST or None)
    if form.is_valid():
        return render(request, "summaryReceiptPage.html", context)
    context = {"form" : form}
    return render(request, "checkout.html", context)

def fourOfour(request):
    
    form = errorForm(request.POST)
    
    def fourOfour(request):
    
    form = errorForm(request.POST)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        subject = 'Player Ranking Page Down'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, settings.EMAIL_HOST_USER]
        contact_message = "Let me know if the page is up.... %s"%(email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

    context = {"form" : form}
    return render(request, "404.html", context)
    
    context = {"form" : form}
    return render(request, "404.html", context)




# def coachApp(request):
#     """
#     coach application
#     """
#     return render(request, "coachApp.html")
