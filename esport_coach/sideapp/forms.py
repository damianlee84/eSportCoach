from django import forms
from .models import Signup 
from datetime import date, datetime
from calendar import monthrange
from .models import Sale

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

class CreditCardField(forms.IntegerField):
    def clean(self, value):
        """Check if given CC number is valid and one of the
           card types we accept"""
        if value and (len(value) < 13 or len(value) > 16):
            raise forms.ValidationError("Please enter in a valid "+\
                "credit card number.")
        return super(CreditCardField, self).clean(value)
    
class expDate(forms.MultiWidget):
    def inExp_date(self, value):
        return [value.month, value.year] if value else [None, None]
 
    def format_output(self, rendered_widgets):
        html = u' / '.join(rendered_widgets)
        return u'<span style="white-space: nowrap;">%s</span>' % html 


