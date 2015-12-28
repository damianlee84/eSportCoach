from django.contrib import admin
from .models import *
from .forms import *

class adminSignup(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'skype', 'mmr', 'server', 'hero', 'rating', 'reputation', 'students', 'pricerate')
    form = SignupForm

class adminCoach(admin.ModelAdmin):
    list_display = ('server', 'champion', 'rating', 'pricerate', 'role', 'avatar', 'overview')

class adminUser(admin.ModelAdmin):
    list_display = ('userid', 'password', 'pname', 'email', 'rank', 'skypeid', 'twitchid')


admin.site.register(Signup, adminSignup)
admin.site.register(Coach, adminCoach)
admin.site.register(User, adminUser)