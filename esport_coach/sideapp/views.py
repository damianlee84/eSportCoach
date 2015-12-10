"""
this file calls all page functions and renders the pages with given context.
"""
from .forms import SignupForm, ContactForm, SalePaymentForm
from .models import Signup, Reviews
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core import serializers


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

def findcoach(request):
    title = 'Testing'
    context = {"title": title}
    return render(request, "find_coach.html", context)


def list_of_coaches(request):
    coaches_list = []
    user = Signup.objects.all()
    for i in range(len(user)):
        coaches_list.append([user[i].username, user[i].mmr, user[i].server,
                            user[i].hero, user[i].rating, user[i].reputation,
                            user[i].students, user[i].pricerate, user[i].id])
    context = {'coaches': coaches_list}
    return render(request, "listOfCoachesPage.html", context)


def tutorselected(request, tutor_username):
    sum_all_avg_reviews = 0
    num_reviews = 0
    final_avg_review = 0
    list_reviews = []
    coach_selected = Signup.objects.get(username=tutor_username)
    all_users_reviews = coach_selected.reviews_set.all()

    for user_review in all_users_reviews:
        avg_review = (user_review.skill_stars + user_review.communication_stars + user_review.helpfulness_stars)/3
        list_reviews.append({"skill":user_review.skill_stars, "communication":user_review.communication_stars, "helpfulness":user_review.helpfulness_stars, "avg_rating":avg_review, "comment":user_review.comment, "reviewer":user_review.reviewer})
        sum_all_avg_reviews += avg_review
        num_reviews += 1

    if num_reviews > 0:
        final_avg_review = sum_all_avg_reviews/num_reviews

    context = {
        'coach': coach_selected,
        'reviews': list_reviews,
        'final_avg_review': final_avg_review
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
        # all_users_reviews = coach_selected.reviews_set.all()
        # rating = Reviews(id=None, coach=coach_selected, reviewer=user_reviewer, skill_stars=skill, communication_stars=communication, helpfulness_stars=helpfulness, comment=review_comment)
        # rating.save()
        # for user_review in all_users_reviews:
        #     print user_review.skill_stars
        #     print user_review.communication_stars
        #     print user_review.helpfulness_stars
        #     print user_review.comment
        return HttpResponse(response_sucess)
    else:
        raise Http404     

def populateReviews(request, tutor_username):
    if request.is_ajax:
        try:
            coach_selected = Signup.objects.get(username=tutor_username)
            response = serializers.serialze('json',coach_selected)
            print response
        except KeyError:
            print "Error"
            return HttpResponse("error")
        return HttpResponse(response)
    else:
        print "else"
        raise Http404

def paymentpage(request, tutor_username):
    tutor = Signup.objects.get(username=tutor_username)
    context = {'coachname': tutor.username, 'coachprice': tutor.pricerate}
    return render(request, "summaryReceiptPage.html", context)

def streampage(request):
    tutor = Signup.objects.get(username=tutor_username)
    context = {'coach': tutor.username}
    return render(request, "streamPage.html", context)

def charge(request):
    form = SalePaymentForm(request.POST or None)
    if form.is_valid():
        return render(request, "summaryReceiptPage.html", context)
    context = {"form" : form}
    return render(request, "checkout.html", context)
