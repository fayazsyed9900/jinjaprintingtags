from django.urls import path
from app1.views import *

app_name='something1'

urlpatterns=[
    path('jinja1/',jinja1,name='jinja1'),
]