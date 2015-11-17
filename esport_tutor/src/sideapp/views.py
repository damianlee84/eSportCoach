from django.shortcuts import render
from .forms import SignupForm, ContactForm
from .models import Signup


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
    coachtest=[]
    #listofcoaches = Signup.objects.all()
    user = Signup.objects.all()
    for i in range(len(user)):
        coachtest.append([user[i].full_name, user[i].mmr, user[i].pricerate, user[i].server, user[i].hero, user[i].reputation, user[i].rating, user[i].students])
#    coach = [user.full_name, user.mmr, user.pricerate, user.server, user.hero, user.reputation, user.rating, user.students]
    context2 = {'coaches': coachtest}
    coach1 = 'someguy'
    mmr = 6123
    price = 9
    server = "US"
    hero = "somehero"
    reputation = 332
    rating = "9/10"
    students = 50
    usercoach = [coach1, mmr, price, server, hero, reputation, rating, students]

    context = {"usercoach": usercoach}

    return render(request, "listOfCoachesPage.html", context2)

