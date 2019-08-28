from django.urls import path
from . import views
# from .views import *

urlpatterns = [
    path('data/', views.user_data_list, name='get_user_data_list'),
    path('predict-actions/', views.predict_actions, name='predict_actions'),
    path('detect-anomalies/', views.detect_anomalies, name='detect_anomalies'),
    path('get-anomalies/', views.get_user_anomalies, name='get_user_anomalies'),
    path('get-num-user-records/', views.get_user_record_num, name='get_num_user_records'),
    path('update-classification/', views.update_classification_info, name='update_classification_info'),
    path('detect-one-anomaly/', views.detect_one_anomaly, name="detect_one_anomaly"),
    # path('import-fake-data/', views.import_fake_data, name='import_fake_data'),
]