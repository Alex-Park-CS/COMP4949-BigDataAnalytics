# pages/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('firstName/', firstNamePageView, name='firstName'),
    path('homePost/', homePost, name='homePost'),
    path('<int:choice>/results/', results, name='results'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),

]
