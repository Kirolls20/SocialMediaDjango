from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from .models import User
# User = get_user_model()
from blog.models import Blog,Comment

class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/user_profile.html'
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user_blogs'] = Blog.objects.filter(author=self.kwargs['pk'])
        context['user_comments'] = Comment.objects.filter(user=self.kwargs['pk'])
        context['user_likes'] = Blog.objects.filter(likes=self.kwargs['pk'])
        return context



user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
