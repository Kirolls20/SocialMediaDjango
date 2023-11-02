from django.urls import path
from . import views
from social_media.users.views import (
    user_detail_view,
    user_redirect_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", views.UserUpdateView.as_view() , name="update"),
    path("<str:username>/<int:pk>/", view=user_detail_view, name="detail"),
    path('add/socialMedia/forms/',views.AddSocialMediaLinksView.as_view(),name='social_media_link_form'),
    path('all/',views.UsersListView.as_view(),name='users_list'),
    path('search/<str:input>/all',views.UserSearchView.as_view(),name='search_users')
]
