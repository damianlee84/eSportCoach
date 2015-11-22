from django.test import TestCase
from .models import Signup
from django.core.urlresolvers import reverse
# Create your tests here.

def create_signup(email,full_name,timestamp,updated,mmr,server,hero,rating,reputation,students,pricerate):

    return Signup.objects.create(email=email,full_name=full_name,timestamp=timestamp,
    updated=updated,mmr=mmr,server=server,hero=hero,rating=rating,reputation=reputation,
    students=students,pricerate=pricerate)

class SignupMethodTests(TestCase):
    def test_list_of_coaches(self):
        """
        testing that there are users in databse.
        """
        response = self.client.get(reverse('sideapp:list_of_coaches'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No coaches available.")
        self.assertQuerysetEqual(response.context['coaches'], [])
