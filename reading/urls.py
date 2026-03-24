from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('start/', views.start_session, name='start_session'),
    path('logout/', views.user_logout, name='logout'),
    path('add_note/<int:session_id>/', views.add_note, name='add_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
]