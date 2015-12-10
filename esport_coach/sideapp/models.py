from django.db import models
from django.conf import settings
from datetime import date, datetime
from calendar import monthrange

class Signup(models.Model):
		username = models.CharField(max_length=50, blank=False, null=False)
		name = models.CharField(max_length=50, blank=False, null=False)
		email = models.EmailField(max_length=50, blank=False, null=False)
		skype = models.CharField(max_length=50, blank=False, null=False)
		mmr = models.PositiveIntegerField(default=0,  blank=False, null=False)
		server = models.CharField(max_length=50, blank = False, null=False)
		hero = models.CharField(max_length=50, blank = False, null=False)
		rating = models.PositiveIntegerField(default=0, blank=False, null=False)
		reputation = models.PositiveIntegerField(default=0, blank=False, null=False)
		students = models.PositiveIntegerField(default=0, blank=False, null=False)
		pricerate = models.FloatField(default=0.00, blank=False, null=False)
		def __unicode__(self):
				return self.username + " " + self.email + " " + self.name

class Reviews(models.Model):
		coach = models.ForeignKey(Signup, on_delete=models.CASCADE)
		reviewer = models.CharField(max_length=100, blank=False, null=True)
		skill_stars = models.PositiveIntegerField(blank=False, null=True)
		communication_stars = models.PositiveIntegerField(blank=False, null=True)
		helpfulness_stars = models.PositiveIntegerField(blank=False, null=True)
		comment = models.CharField(max_length=300, blank=False, null=True)








class User(models.Model):
		userid = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
		email = models.EmailField(blank=False, null=False)
		pname = models.CharField(max_length=100, blank=False, null=False)
		MMR = models.IntegerField(default=0,  blank=False, null=False)
		skypeid = models.CharField(max_length=100, blank=False, null=False)
		twitchid = models.CharField(max_length=100, blank=False, null=False)
		def __str__(self):
				return  " " + self.email + " " + self.pname

class Coach(models.Model):
	 userid = models.ForeignKey('User', on_delete=models.CASCADE)
	 server = models.CharField(max_length = 50, blank = False, null = False)
	 champion = models.CharField(max_length = 500, blank = False, null = False)
	 role = models.CharField(max_length = 500, blank = False, null = False)
	 pricerate = models.FloatField(default = 0.00)
	 avatar = models.URLField(blank=False, null=False)
	 rating = models.IntegerField(default = 0,  blank = False, null = False)
	 Overview = models.TextField(blank=True)
	 def __str__(self):
				return  " " + self.champion + " " + str(self.rating) + " " + self.server + " " + str(self.pricerate)

class Coaching(models.Model):
	 coach = models.ForeignKey('Coach', on_delete=models.CASCADE)
	 student = models.ForeignKey('User', on_delete=models.CASCADE)
	 date = models.DateTimeField(auto_now_add = False, auto_now = "True")
	 pricerate = models.FloatField(default = 0, blank = False, null = False)
	 quantity = models.IntegerField(default = 0,  blank = False, null = False)
	 def __str__(self):
				return self.coach + " " + self.student + " " + str(self.date) + " " + str(self.pricerate) + " " + str(self.quantity)

class Blacklist(models.Model):
	 userid = models.ForeignKey('User', on_delete=models.CASCADE)
	 date = models.DateTimeField(auto_now_add = False, auto_now = "True")
	 reason = models.TextField(blank = False, null=False)
	 #should we add another field of admin so taht we know who put these people into the blacklist
	 def __str__(self):
				return self.usr + " " + str(self.date) + " " + self.reason

class reviewing(models.Model):
	 student = models.ForeignKey('User', on_delete=models.CASCADE)
	 coach = models.ForeignKey('Coach', on_delete=models.CASCADE)
	 review = models.TextField(blank=False, null=False)
	 date = models.DateTimeField(auto_now_add=False, auto_now=False)
	 rating = models.IntegerField(default=0, blank=False, null=False)
	 def __str__(self):
			return self.student + " " + self.coach + " " + str(self.rating) + " " + str(self.date) + " " + self.review

class report(models.Model):
	 student = models.ForeignKey('User', on_delete=models.CASCADE)
	 coach = models.ForeignKey('Coach', on_delete=models.CASCADE)
	 reason = models.TextField(blank=False, null=False)
	 date = models.DateTimeField(auto_now_add=False, auto_now=False)
	 def __str__(self):
			return self.student + " " + self.coach + " "  + str(self.date) + " " + self.reason


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
