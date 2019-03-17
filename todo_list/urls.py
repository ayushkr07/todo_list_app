from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<list_id>',views.delete,name="delete"),
    path('cross/<list_id>',views.cross,name="cross"),
    path('un_cross/<list_id>',views.un_cross,name="un_cross"),
]
