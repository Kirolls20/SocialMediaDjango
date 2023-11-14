from django.urls import path 
from . import views 

urlpatterns = [
    path('home/',views.QuestionsHomeView.as_view(),name='question_home'),
   path('new/',views.CreateQuestionView.as_view(),name='create_question'),
   path('<int:pk>/update/',views.UpdateQuestionView.as_view(),name='update_question'),
   path('<int:pk>/delete/',views.DeleteQuestionView.as_view(),name='delete_question'),
   path('<int:pk>/details/',views.QuestionDetailView.as_view(),name='question_detail'),
   path('answer/<int:pk>/question/',views.AnswerQuestionView.as_view(),name='answer_question'),
   path('like/<int:pk>/',views.LikeQuestionView.as_view(),name='like_question'),
   path('<int:pk>/repost/',views.RepostQuestionView.as_view(),name='repost_question'),
   

]