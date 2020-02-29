from django.urls import path

from . import views


app_name = 'manager'
urlpatterns = [
    path('', views.IndexViews.as_view(), name='index'),
]
