from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<slug:hid>', views.delete , name='delete'),
]
