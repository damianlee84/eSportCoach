"""
this file tests all functionality of the app.
"""
from django.test import TestCase
from django.utils import timezone
from .models import Signup, Reviews
from django.core.urlresolvers import reverse
import urlparse
from mock import Mock, ANY
from django.conf import settings





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
        
class testViews(TestCase):
    def testHome(self):
        response = self.client.get(reverse('sideapp:home'))
        self.assertEqual(response.status_code, 200)

    def testLogout(self):
        response = self.client.get(reverse('sideapp:logout'))
        self.assertEqual(response.status_code, 200)

    def testContact(self):
        response = self.client.get(reverse('sideapp:contact'))
        self.assertEqual(response.status_code, 200)

    def testSignup(self):
        response = self.client.get(reverse('sideapp:signup
        self.assertEqual(response.status_code, 200)

    def testFindCoach(self):
        response = self.client.get(reverse('sideapp:findcoach'))
        self.assertEqual(response.status_code, 200)
                                           
    def testListCoach(self):
        response = self.client.get(reverse('sideapp:list_of_coaches'))
        self.assertEqual(response.status_code, 200)
                                           
    def testTutorSelect(self):
        response = self.client.get(reverse('sideapp:tutorselected'))
        self.assertEqual(response.status_code, 200)
                                        

                
                                    
    



    
    
