from rest_framework.viewsets import ModelViewSet
from main.models import Person, Contact
from main.serializers import PersonSerializer, ContactSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



# CRUD
# create, read, update, delete
# post,  get, put, delete