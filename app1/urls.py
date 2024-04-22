from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('house/',views.house,name='house'),
    path('house_list/',views.house_list,name='house_list'),
    path('create_room/',views.room,name='room'),
    path('room_report/<int:house_pk>/',views.room_report,name='room_report'),
    path('maintenance_report/', views.maintenance_report, name='maintenance_report'),

]