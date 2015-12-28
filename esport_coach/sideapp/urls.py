"""this file connects all urls to application when being called."""
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^login/', views.login, name='login'),
    url(r'^authenticateLogin/', views.authenticateLogin, name='authenticateLogin'),
    url(r'^authenticateRegister/', views.authenticateRegister, name='authenticateRegister'),
    url(r'^authenticated/(?P<userid>[-\w]+)', views.authenticated, name='authenticated'),
    url(r'^register/', views.register, name='register'),
    url(r'^list_of_coaches/', views.list_of_coaches, name='list_of_coaches'),
    url(r'^tutorselected/(?P<tutor_username>[-\w]+)', views.tutorselected, name='tutorselected'),
    url(r'^renderReviews/(?P<tutor_username>[-\w]+)', views.renderReviews, name='renderReviews'),
    url(r'^reviewcoach/(?P<tutor_username>[-\w]+)', views.reviewcoach, name='reviewcoach'),
    url(r'^paymentpage/(?P<tutor_username>[-\w]+)', views.paymentpage, name='paymentpage'),
    url(r'^streampage/(?P<tutor_username>[-\w]+)', views.streampage, name='streampage'),
    url(r'^streampage/(?P<tutor_username>[-\w]+)', views.streampage, name='streampage'),
    url(r'^searchCoach/', views.searchCoach, name='searchCoach'),
    url(r'^player_rank/', views.fourOfour, name='player_rank'),

]
