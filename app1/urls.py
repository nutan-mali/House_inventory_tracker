from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('house/',views.house,name='house'),
    path('house_list/',views.house_list,name='house_list'),
    path('create_room/',views.room,name='room'),
    # path('house_select/',views.house_select,name='house_select'),
    path('room_report/<int:house_pk>/',views.room_report,name='room_report'),
]