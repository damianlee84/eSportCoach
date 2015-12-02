from django.db import models
from django.conf import settings
from datetime import date, datetime
from calendar import monthrange

class Signup(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=50, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now="True")
				
    mmr = models.CharField(max_length=50, blank = False, null=False)
    server = models.CharField(max_length=50, blank = False, null=False)
    hero = models.CharField(max_length=50, blank = False, null=False)
    rating = models.PositiveIntegerField(blank = False, null=False)
    reputation = models.PositiveIntegerField(blank = False, null=False)
    students = models.CharField(max_length=50, blank = False, null=False)
    pricerate = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.full_name


class Reviews(models.Model):
    coach = models.ForeignKey(Signup, on_delete=models.CASCADE)
    skill_stars = models.PositiveIntegerField(blank=False, null=True)
    communication_stars = models.PositiveIntegerField(blank=False, null=True)
    helpfulness_stars = models.PositiveIntegerField(blank=False, null=True)
    comment = models.CharField(max_length=300, blank=False, null=True)


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    email = models.EmailField(blank = False, null = False)
    name = models.CharField(max_length = 100, blank = False, null = False)
    def __str__(self):
        return self.username + " " + self.email + " " + self.name

class Coach(User):
   MMR = models.IntegerField(default=0,  blank=False, null=False)
   hero = models.CharField(max_length = 500, blank = False, null = False)
   server = models.CharField(max_length = 50, blank = False, null = False)
   rating = models.IntegerField(default = 0,  blank = False, null = False)
   hour_rate = models.FloatField(default = 0.00)
   def __str__(self):
        return self.username + " " + self.hero + " " + str(self.rating) + " " + self.server + " " + str(self.hour_rate)

class Tutee(User):
   MMR = models.IntegerField(default=0,  blank = False, null = False)
   def __str__(self):
        return self.username + " " + self.email + " " + self.name





class Register(models.Model):
    username = models.ForeignKey(User)
    rdate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    def __str__(self):
      return self.username + " " + rdate









class transaction(models.Model):
    def __init__(self, *args, **kwargs):
        super(transaction, self).__init__(*args, **kwargs)
        
        import stripe
        stripe.api.key = settings.STRIPE_API_KEY
        self.stripe = stripe
        
    #transaction number    
    transaction_id = models.CharField(max_length = 32)
    transaction_date = models.DateTimeField(auto_now_add = True, auto_now=False)
    
    def charge(self, price_in_cents, number, exp_month, exp_year, cvc):
        if self.transaction_id:
            return False, Exception(message = "Already charged.")
        
        try:
            response = self.stripe.Charge.create(amount = price_in_cents, currency = "usd", card = {"number": number, "exp_month": exp_month, "exp_year": exp_year, "cvc": cvc, "address_line1": self.address1, "address_line2": self.address2, "zip_code": self.zip_code, "state": self.state,}, description = "Thank You, Happy Gaming!")
            self.transcation_id = response.id
        except self.stripe.CardError, ce:
            
            return False, ce
        
        
        return True, response
        
        
        
        
        
        
        
        
    
