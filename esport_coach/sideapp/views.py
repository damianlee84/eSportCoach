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
        list_reviews.append([user_review.skill_stars, user_review.communication_stars, user_review.helpfulness_stars, avg_review])
        sum_all_avg_reviews += avg_review
        num_reviews += 1

    if num_reviews > 0:
        final_avg_review = sum_all_avg_reviews/num_reviews

    context = {
        'coach': coach_selected,
        'list_reviews': list_reviews,
        'final_avg_review': final_avg_review
        }
    return render(request, "tutorSelectedPage.html", context)

 
def reviewcoach(request, tutor_username):
    if request.is_ajax:
        try:
            # For now the reviewer is manually inputed below until we have that global username passed around correctly.
            # reviewer = Signup.objects.get(username=tutor_username)
            reviewer = "SomeTutee"
            skill = int(request.GET.get('ratingSkill'))
            communication = int(request.GET.get('ratingCommunication'))
            helpfulness = int(request.GET.get('ratingHelpfulness'))
            comment = request.GET.get('textarea_review')
            # coach_selected = Signup.objects.get(username=tutor_username)
            # rate = Reviews(id=None, coach=coach_selected, skill_stars=skill, communication_stars=communication, helpfulness_stars=helpfulness, comment=tutee_comment)
            # rate.save()
        except KeyError:
            return HttpResponse('keyError')    # Incorrect Post
        return HttpResponse("success")
    else:
        raise Http404     
    # for user_review in all_users_reviews:
    #     print user_review.skill_stars
    #     print user_review.communication_stars
    #     print user_review.helpfulness_stars
    #     print user_review.comment


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
