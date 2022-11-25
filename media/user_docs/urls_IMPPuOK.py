from django.urls import path
from . import views

urlpatterns = [
path('anonymizer/forms/model_form_upload', views.model_form_upload, name='model_form_upload'), 
]