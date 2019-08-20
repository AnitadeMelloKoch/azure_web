from django.urls import path
from . import views
# from .views import *

urlpatterns = [
    # path('', views.index, name='index'),
    # path('other', views.other, name='other'),
    # path('posttest', views.posttest, name='posttest'),

    # path('data/', GetDataView.as_view(), name='get_data'),
    path('data/', views.user_data_list, name='get_user_data_list'),
    
]