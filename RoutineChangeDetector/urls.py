from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('other', views.other, name='other'),
    path('posttest', views.posttest, name='posttest')
]