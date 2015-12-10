"""this file connects all urls to application when being called."""
from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^signup/', views.signup, name='signup'),
    # url(r'^findcoach/$', views.findcoach, name='findcoach'),
    url(r'^list_of_coaches/', views.list_of_coaches, name='list_of_coaches'),
    url(r'^tutorselected/(?P<tutor_username>[-\w]+)', views.tutorselected, name='tutorselected'),
    url(r'^renderReviews/(?P<tutor_username>[-\w]+)', views.renderReviews, name='renderReviews'),
    url(r'^reviewcoach/(?P<tutor_username>[-\w]+)', views.reviewcoach, name='reviewcoach'),
    url(r'^paymentpage/(?P<tutor_username>[-\w]+)', views.paymentpage, name='paymentpage'),
    url(r'^streampage/(?P<tutor_username>[-\w]+)', views.streampage, name='streampage'),
    url(r'^tutorselected/',RedirectView.as_view(url='/sideapp/list_of_coaches/'), name='redirecttutor'),
    #url(r'^stream/', views.url, name='stream'),
    # url(r'^coachApp/', views.coachApp, name='coachApp'),
    #url(r'^signupCoach/', views.signupCoach, name='signupCoach'),
    #url(r'^player_rank/', views.player_rank, name='player_rank'),

]
