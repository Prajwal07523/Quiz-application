from . import views
from django.urls import path, include

urlpatterns = [
    # path('', views.home, name='home'),  # Home page (with login/signup)
    path('', views.index, name='quiz_home'),
    
    path('start/', views.start_quiz, name='start_quiz'),
    path('question/', views.get_question, name='get_question'),
    path('submit/', views.submit_answer, name='submit_answer'),
    path('summary/', views.quiz_summary, name='quiz_summary'),
]
