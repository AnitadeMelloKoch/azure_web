from django.urls import path
from . import views
# from .views import *

urlpatterns = [
    path('data/', views.user_data_list, name='get_user_data_list'),
    path('predict-actions/', views.predict_actions, name='predict_actions'),
]