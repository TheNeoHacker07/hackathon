from django.urls import path
from .views import RegisterView,ActivationView

urlpatterns=[
    path('registers/',RegisterView.as_view()),
    path('active/<str:email>/<str:activation_code>/',ActivationView.as_view(),name='activate'),
    
]