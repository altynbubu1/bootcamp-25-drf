from rest_framework import serializers

from main.models import Person, Contact


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('name', 'age', 'position') #'__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

