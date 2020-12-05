from django.urls import path
from . import views

# add all routes/path here
urlpatterns = [
    path('', views.index),
    path('result', views.process),

]