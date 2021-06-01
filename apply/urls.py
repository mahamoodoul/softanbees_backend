from django.urls import path
from .views import home_apply


urlpatterns = [
    path('',home_apply,name='apply')
]