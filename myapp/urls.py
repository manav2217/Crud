from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name="index"),
    path('show',views.show , name="show"),
    path('edit/<int:pk>/',views.edit , name="edit"),
    path('edit_user/<int:pk>/',views.edit_user , name="edit_user"),
    path('delete_user/<int:pk>/',views.delete_user , name="delete_user"),
]
