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
    def decompress(self, value):
        return [value.month, value.year] if value else [None, None]
 
    def format_output(self, rendered_widgets):
        html = u' / '.join(rendered_widgets)
        return u'<span style="white-space: nowrap;">%s</span>' % html 

    
"""code snippet from STRIPE documentation """
"""user can select the months and years from the given selection in the selection boxes"""
class expDateInput(forms.MultiValueField):
    EXP_MONTH = [(x, x) for x in xrange(1, 13)]
    EXP_YEAR = [(x, x) for x in xrange(date.today().year,
                                       date.today().year + 15)]
    default_error_messages = {
        'invalid_month': u'Enter a valid month.',
        'invalid_year': u'Enter a valid year.',
    }
 
    def __init__(self, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        fields = (
            forms.ChoiceField(choices=self.EXP_MONTH,
                error_messages={'invalid': errors['invalid_month']}),
            forms.ChoiceField(choices=self.EXP_YEAR,
                error_messages={'invalid': errors['invalid_year']}),
        )
        super(CCExpField, self).__init__(fields, *args, **kwargs)
        self.widget = CCExpWidget(widgets =
            [fields[0].widget, fields[1].widget])
 
    def clean(self, value):
        exp = super(CCExpField, self).clean(value)
        if date.today() > exp:
            raise forms.ValidationError(
            "The expiration date you entered is in the past.")
        return exp
 
    def compress(self, data_list):
        if data_list:
            if data_list[1] in forms.fields.EMPTY_VALUES:
                error = self.error_messages['invalid_year']
                raise forms.ValidationError(error)
            if data_list[0] in forms.fields.EMPTY_VALUES:
                error = self.error_messages['invalid_month']
                raise forms.ValidationError(error)
            year = int(data_list[1])
            month = int(data_list[0])
            # find last day of the month
            day = monthrange(year, month)[1]
            return date(year, month, day)
        return None
    
