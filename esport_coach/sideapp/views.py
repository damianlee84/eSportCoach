"""
this file calls all page functions and renders the pages with given context.
"""
from .forms import SignupForm, ContactForm, SalePaymentForm
from .models import Signup
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


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
        message = form.cleaned_data.get('messsage')
        full_name = form.cleaned_data.get('full_name')
        subject = 'Customers Enquiries'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, settings.EMAIL_HOST_USER]
        contact_message = "%s: %s via %s"%(full_name, message, email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

    context = {"form" : form}
    return render(request, "forms.html", context)

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
        coaches_list.append([user[i].full_name, user[i].mmr, user[i].server,
                            user[i].hero, user[i].rating, user[i].reputation,
                            user[i].students, user[i].pricerate, user[i].id])
    context = {'coaches': coaches_list}
    return render(request, "listOfCoachesPage.html", context)


def tutorselected(request, tutor_id):
    rating_list = []
    sum_stars = 0
    num_ratings = 0
    avg_rating = 0
    coach_selected = Signup.objects.get(pk=tutor_id)
    ratings = coach_selected.ratings_set.all()

    for rating in ratings:
        rating_list.append([rating.num_stars, rating.comment])
        sum_stars += rating.num_stars
        num_ratings += 1

    if num_ratings > 0:
        avg_rating = sum_stars/num_ratings

    context = {'coach': coach_selected, 'ratings': rating_list, 'avg_rating': avg_rating}

    return render(request, "tutorSelectedPage.html", context)


def rateuser(request, tutor_id, stars, tutee_comment):
    coach_selected = Signup.objects.get(pk=tutor_id)
    rate = Ratings(id=None, coach=coach_selected, num_stars=stars, comment=tutee_comment)
    rate.save()

    # return render(request, "listOfCoachesPage.html", context)


# def retrieverating(request, tutor_id):
#     rating_list = []
#     coach_selected = Signup.objects.filter(id=tutor_id)
#     ratings = coach_selected.Ratings.all()
#     for i in range(len(ratings))
#         rating_list.append([rating[i].num_stars, rating[i].comment])
#     context = {'ratings': rating_list}
#     return render(request, "listOfCoachesPage.html", context)


def paymentpage(request, tutor_id):
    tutor = Signup.objects.get(pk=tutor_id)
    context = {'coachname': tutor.full_name, 'coachprice': tutor.pricerate}
    return render(request, "summaryReceiptPage.html", context)

def streampage(request):
    tutor = Signup.objects.get(pk=1)
    context = {'coach': tutor.full_name}
    return render(request, "streamPage.html", context)

def charge(request):
    form = SalePaymentForm(request.POST or None)
    if form.is_valid():
        return render(request, "summaryReceiptPage.html", context)
    context = {"form" : form}
    return render(request, "checkout.html", context)
