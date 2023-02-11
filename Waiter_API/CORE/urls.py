from django.urls import path
from .views import *

urlpatterns = [
    path('menu/see/', Menu_Viewer.as_view()),
    path('menu/change/', Menu_Edit),
    path('order/', Make_A_Order),
    path('check/', Check_Viewer),
]