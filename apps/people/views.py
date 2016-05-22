from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PersonSerializer, Person


class PersonViewSet(viewsets.ModelViewSet):
    model = Person
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_queryset(self):
        phone = self.request.GET.get('phone')
        if phone:
            qs = Person.objects.filter(phone_number=phone, active=True)
        else:
            qs = Person.objects.none()
        return qs
