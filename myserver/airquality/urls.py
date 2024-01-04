from django.urls import path

from .views import *

app_name = 'airquality'

urlpatterns = [
    path('api/indoor-buildthing/', indoorBuildthing, name='indoor-buildthing'),

]