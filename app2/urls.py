from app2.views import *
from django.urls import path

app_name='something'
urlpatterns=[
    path('Tsenam/',Tsenam,name='Tsenam'),
]