from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='vlog-home'),
    # path('about/', views.about, name='vlog-about'),
     path('', views.index, name='Vlog-home'),
    path('service', views.service, name='Vlog-service'),
    path('about', views.about, name='Vlog-about'),
    path('signup', views.signup, name='Vlog-signup'),
    path('chat', views.chat, name='Vlog-chat'),
    path( 'appointment', views.appointment, name='Vlog-appointment')

]