from django.urls import path 

from . import views

urlpatterns = [
    path('home/',views.BlogHomeView.as_view(),name='home'),
    path('create/',views.CreateBlogView.as_view(),name='create_blog'),
    path('blog_info/<int:pk>/',views.BlogDetailView.as_view(),name='blog_details'),
    path('update/<int:pk>/',views.BlogUpdateView.as_view(),name='update_blog'),
    path('delete/<int:pk>/',views.BlogDeleteView.as_view(),name='delete_blog'),
    path('comment/to/<int:pk>/',views.CreateCommentView.as_view(),name='create_comment'),
    path('like/<int:pk>/',views.LikeView.as_view(),name='like'),
]