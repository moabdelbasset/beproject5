
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
