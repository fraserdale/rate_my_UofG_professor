from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('index', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('recent/', views.recent, name='recent'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('professors/', views.professors, name='professors'),
    path('professor/<slug:professor_name_slug>', views.show_professor, name='show_professor'),
    path('myreviews/', views.show_myreviews, name='show_myreviews'),
    path('professor/<slug:professor_name_slug>/add_review', views.add_review, name='add_review'),
    path('myreviews/delete', views.delete, name='delete'),
    path('logout/', views.user_logout, name='logout'),
    #path('professor/<slug:professor_name_slug>/review', views.professor_review, name='professor_review')

]
