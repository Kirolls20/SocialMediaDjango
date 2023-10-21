from django.urls import path 

from . import views

urlpatterns = [
    path('home/',views.BlogHomeView.as_view(),name='home'),
    path('create/',views.CreateBlogView.as_view(),name='create_blog'),
    path('blog_info/<int:pk>/',views.BlogDetailView.as_view(),name='blog_details'),
]