"""
this file tests all functionality of the app.
"""
from django.test import TestCase
from django.utils import timezone
from .models import Signup
from django.core.urlresolvers import reverse
# Create your tests here.

def create_signup(email, full_name, mmr, server, hero, rating, reputation,
                  students, pricerate, coach_id):
    """
    setup.
    """
    return Signup.objects.create(email=email, full_name=full_name, timestamp=timezone.now(),
                                 updated=timezone.now(), mmr=mmr, server=server,
                                 hero=hero, rating=rating, reputation=reputation,
                                 students=students, pricerate=pricerate, id=coach_id)

class SignupMethodTests(TestCase):
    def test_list_of_coaches_with_no_users(self):
        """
        testing that there are no users in databse.
        """
        response = self.client.get(reverse('sideapp:list_of_coaches'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No coaches available.")
        self.assertQuerysetEqual(response.context['coaches'], [])

    def test_list_of_coaches_with_users(self):
        """
        testing that there are users in databse.
        """
        create_signup(email="testemail@mail.com", full_name="testbot", mmr=123,
                      server="LA", hero="myHero", rating=10, reputation=50,
                      students=20, pricerate=30, coach_id=2)
        response = self.client.get(reverse('sideapp:list_of_coaches'))
        self.assertQuerysetEqual(response.context['coaches'][0],
                                 ["u'testbot'", "u'123'", "u'LA'", "u'myHero'",
                                  '10', '50', "u'20'", '30', '2'])

class testPages():
    
    def testHome(self, client):
        response = client.get('/home/')
        assert response.status.code == 200
