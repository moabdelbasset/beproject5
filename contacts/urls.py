# Inside your app's urls.py

from django.urls import path
from .views import ContactCreate, ContactList

urlpatterns = [
    path('contacts/', ContactList.as_view(), name='contact-list'),
    path('contacts/create/', ContactCreate.as_view(), name='contact-create'),
]
