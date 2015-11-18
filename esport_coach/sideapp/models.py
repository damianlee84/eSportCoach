from django.db import models

class Signup(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=50, blank = False, null = False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = "True")

    mmr = models.CharField(max_length=50, blank = False, null = False)
    server = models.CharField(max_length=50, blank = False, null = False)
    hero = models.CharField(max_length=50, blank = False, null = False)
    rating = models.PositiveIntegerField(max_length=50, blank = False, null = False)
    reputation = models.PositiveIntegerField(max_length=50, blank = False, null = False)
    students = models.CharField(max_length=50, blank = False, null = False)
    pricerate = models.PositiveIntegerField(max_length=50, blank = False, null = False)

    def __unicode__(self):
        return self.full_name


