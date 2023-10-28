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
]
