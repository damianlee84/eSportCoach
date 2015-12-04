from django.contrib import admin
from .models import Signup
from .forms import SignupForm


class adminSignup(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'skype', 'mmr', 'server', 'hero', 'rating', 'reputation', 'students', 'pricerate')
    form = SignupForm


admin.site.register(Signup, adminSignup)


