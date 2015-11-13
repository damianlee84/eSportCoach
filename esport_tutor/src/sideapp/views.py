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
