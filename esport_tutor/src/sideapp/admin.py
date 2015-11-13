from django.contrib import admin

from .models import Signup
from .forms import SignupForm


class adminSignup(admin.ModelAdmin):
    list_display = ("__unicode__", "timestamp", "updated")
    form = SignupForm


admin.site.register(Signup, adminSignup)


