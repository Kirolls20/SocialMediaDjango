from django.urls import path 
from . import views 

urlpatterns = [
    path('home/',views.QuestionsHomeView.as_view(),name='question_home'),
   path('new/',views.CreateQuestionView.as_view(),name='create_question'),
   path('<int:pk>/update/',views.UpdateQuestionView.as_view(),name='update_question'),
   path('<int:pk>/delete/',views.DeleteQuestionView.as_view(),name='delete_question'),
   
]