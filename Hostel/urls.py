
from django.urls import path

from .views import *





urlpatterns = [

path("entries/", EntriesList.as_view(), name="entries_list"),

]
