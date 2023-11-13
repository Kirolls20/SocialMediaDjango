from django.urls import path 

from . import views

urlpatterns = [
    path('home/',views.BlogHomeView.as_view(),name='blogs_home'),
    path('create/',views.CreateBlogView.as_view(),name='create_blog'),
    path('blog_info/<int:pk>/',views.BlogDetailView.as_view(),name='blog_details'),
    path('update/<int:pk>/',views.BlogUpdateView.as_view(),name='update_blog'),
    path('delete/<int:pk>/',views.BlogDeleteView.as_view(),name='delete_blog'),
    path('comment/to/<int:pk>/',views.CreateCommentView.as_view(),name='create_comment'),
    path('like/<int:pk>/',views.LikeView.as_view(),name='like'),
    path('comments/for/<int:pk>/post/',views.CommentListView.as_view(),name='comment_list'),
    path('search/<str:input>/all/', views.SearchView.as_view(), name='search'),
    path('tags/<str:tag>',views.TrendyTagView.as_view(),name='trendy_tags'),
    path('<int:pk>/bookmark/',views.AddBookmarkView.as_view(),name='bookmark'),
    path('<int:pk>/repost/',views.RepostView.as_view(),name='repost_blog'),
    
]