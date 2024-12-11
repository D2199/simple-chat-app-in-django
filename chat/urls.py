from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('<str:room>/', views.room, name='room'),
    # path('checkview', views.checkview, name='checkview'),
    # path('send', views.send, name='send'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('login/',views.loginView,name='login'),
    path('register/',views.register,name='register'),
    path('chat/<str:to>',views.chat,name='chat'),
    path('logout',views.logoutView,name='logout'),
path('send/',views.addMsg,name='send'),

    path('dashboard/',views.dashboard,name='dashboard')
]