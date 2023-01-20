from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.testing),
    path('requestcontent/', views.requestcontent),
    path('pathparameters/<name>/<id>', views.pathparameters, name="pathparameters"),
    path('queryparameters/', views.queryparameters, name ="queryparameters"),
    path('bodyparameters/', views.bodyparameters, name="bodyparameters"),
    path('showform/', views.showform, name="showform"),
    path('error/', views.error, name="error"),
    
]
