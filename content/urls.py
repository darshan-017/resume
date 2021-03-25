from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.SignIn, name='signIn'),
    path('personal_detail/', views.personal_detail, name='personal_detail'),
    path('edit_personal/', views.edit_personal, name='edit_personal'),
    path('add_educational/', views.addEducation, name='add_edu'),
    path('edit_edu/<int:pk>/', views.edit_edu, name='edit_edu'),
    path('addexp/', views.addExperience, name='addExp'),
    path('editExp/<int:pk>/', views.editExp, name='editExp'),
    path('addskill/', views.addSkill, name='addskill'),
    path('addskill/<int:pk>/', views.editSkill, name='editSkill'),
    path('logout/', views.signout, name='logout'),
    path('selectResume/', views.selectResume, name='selectResume'),
    path('resume2/', views.resume2, name='resume2'),
    path('weather_app', views.weather, name='weather')

]