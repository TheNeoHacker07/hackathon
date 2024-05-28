from django.shortcuts import render
from .models import User
from .serializer import UserSerilizer
from rest_framework.generics import ListAPIView,RetrieveAPIView


class GetPeople(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerilizer

class GetPerson(RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerilizer
    lookup_field='id'    














# Create your views here.
