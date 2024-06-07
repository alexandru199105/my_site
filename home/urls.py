from django.urls import path
from home.views import HomeView
from .views import  ContactFormSubmitView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact_submit/', ContactFormSubmitView.as_view(), name='contact_form_submit'),
]
