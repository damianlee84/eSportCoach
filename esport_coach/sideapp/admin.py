from django.contrib import admin
from .models import *
from .forms import SignupForm


    list_display = ('username', 'name', 'email', 'skype', 'mmr', 'server', 'hero', 'rating', 'reputation', 'students', 'pricerate')class adminSignup(admin.ModelAdmin):
    form = SignupForm



admin.site.register(Signup, adminSignup)
