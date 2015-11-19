from django import forms
from .models import Signup

class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['full_name', 'email', 'mmr', 'pricerate', 'server', 'hero', 'reputation', 'rating', 'students']
        
    
    def valid_email(self):
        email = self.validated_data.get('email')
        return email
        
    def valid_name(self):
        full_name = self.validated_data.get('full_name')
        return full_name
    

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
