from django.shortcuts import render
from .forms import SignupForm, ContactForm


def home(request):
    title = 'Welcome'
    form = SignupForm(request.POST or None)
    context = {
        "title": title,
        "form" : form,
    }
     
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        context = {
        "title": "Signup Succesful",
    }
    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "form" : form,
        }
    '''
    if form.is_valid();
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('messsage')
        full_name = form.cleaned_data.get('full_name') 
        '''
    return render(request, "forms.html", context)

def signup(request):
    title = 'Welcome'
    form = SignupForm(request.POST or None)
    context = {
        "title": title,
        "form" : form,
    }
     
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        context = {
        "title": "Signup Succesful",
    }
    return render(request, "forms.html", context)

def findcoach(request):
    title = 'Testing'
    context = {
        "title": title}
    
    return render(request, "find_coach.html", context)

def list_of_coaches(request):
    coach = 'someguy'
    mmr = 6123
    price = 9
    server = "US"
    hero = "somehero"
    reputation = 332
    rating = "9/10"
    students = 50
    usercoach = [coach, mmr, price, server, hero, reputation, rating, students]

    context = {"usercoach": usercoach}

    return render(request, "listOfCoachesPage.html", context)

