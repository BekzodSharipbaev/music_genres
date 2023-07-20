from django.urls import path

from .views import show_singers, show_singer

app_name = 'hiphop'

urlpatterns = [
    path('', show_singers, name='home'),
    path('singer<slug:slug>/', show_singer, name='singer'),
]
