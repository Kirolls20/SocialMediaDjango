from django.shortcuts import render,redirect ,HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views import View
from django import forms
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView,DetailView, 
    RedirectView, UpdateView,
    TemplateView,DeleteView)

from .models import User,UserSocialMeiaLink
from .forms import UserUpdateForm,SocialMediaLinkFormSet 
from blog.models import Bookmark as blog_bookmarks
from questions.models import Bookmark as question_bookmarks
# User = get_user_model()
from blog.models import Blog,Comment
from questions.models import Question,Answer

import random

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.all()
        questions = Question.objects.all()
        random_feeds = list(blogs) + list(questions)
        random.shuffle(random_feeds)
        print(random_feeds)
        context['random_feeds'] = random_feeds

        return context

class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/user_profile.html'
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user']= User.objects.get(id=self.kwargs['pk'])
        context['social_media_links'] = UserSocialMeiaLink.objects.filter(user=self.kwargs['pk']).all()
        context['user_blogs'] = Blog.objects.filter(author=self.kwargs['pk']).order_by('-pub_date')
        context['user_comments'] = Comment.objects.filter(user=self.kwargs['pk'])
        context['user_likes'] = Blog.objects.filter(likes=self.kwargs['pk'])
        context['user_questions'] = Question.objects.filter(author=self.kwargs['pk']).order_by('-pub_date')
        context['user_answers'] = Answer.objects.filter(author=self.kwargs['pk']).order_by('-pub_date')
        if len(context['user_blogs']) == 0 :
            context['new_profile'] = 'New Profile\nYou did not published anything yet'
        return context

user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'users/user_update.html'
    model = User
    form_class= UserUpdateForm
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user



class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class AddSocialMediaLinksView(LoginRequiredMixin, View):
    template_name = 'users/social_media_forms.html'

    def get(self, request):
        user = request.user
        SocialMediaLinkFormSet = forms.modelformset_factory(
            UserSocialMeiaLink,
            fields=('platform', 'link'),
            extra=2,  # Number of empty forms displayed
            can_delete=True)
        formset = SocialMediaLinkFormSet(queryset=UserSocialMeiaLink.objects.filter(user=user))
        return render(request, self.template_name, {'formset': formset})

    def post(self, request):
        user = request.user
        SocialMediaLinkFormSet = forms.modelformset_factory(
            UserSocialMeiaLink,
            fields=('platform', 'link'),
            extra=2,  # Number of empty forms displayed
            can_delete=True)    
        formset = SocialMediaLinkFormSet(request.POST, queryset=UserSocialMeiaLink.objects.filter(user=user))

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = user
                instance.save()

                return reverse("users:detail", args=(user,user.id)) # Error here #

        return render(request, self.template_name, {'formset': formset})


class UsersListView(LoginRequiredMixin,TemplateView):
    template_name = 'users/users_list.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(username=self.request.user).all()
        return context

class UserSearchView(LoginRequiredMixin,TemplateView):
    template_name = 'users/search_users_result.html'

    def get(self,*args,**kwargs):
        if self.request.method == 'GET':
            search_input = self.request.GET.get('input')
            if search_input:
                results = User.objects.filter(username=search_input).all()
                return render(self.request,self.template_name,{'results':results})
            else:
                return reverse('search_users',args=['', 'all'])


class BookmarkBlogListView(LoginRequiredMixin,TemplateView):
    template_name = 'users/bookmarks_blogs_list.html' 

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context['bookmarks_blog_list'] = blog_bookmarks.objects.filter(user = self.request.user). \
        all().order_by('-created_date')
        return context      


class BookmarkQuestionListView(LoginRequiredMixin,TemplateView):
    template_name= 'users/bookmarks_questions_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmarks_question_list'] = question_bookmarks.objects.filter(user=self.request.user). \
        all().order_by('-created_date')
        return context

class RemoveBlogBookmarkView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    template_name = 'users/bookmarks_blogs_list.html' 
    model = blog_bookmarks
    success_message = ("Bookmark removed!")
    
    def get_success_url(self):
        return reverse('users:blog_bookmarks')

class RemoveBlogQuestionBookmarkView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    template_name = 'users/bookmarks_questions_list.html'
    model = question_bookmarks
    success_message = ("Bookmark removed!")

    def get_success_url(self):
        return reverse('users:question_bookmarks')