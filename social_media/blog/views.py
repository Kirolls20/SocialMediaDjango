from typing import Any
from django.utils import timezone
from datetime import timedelta

from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog,Comment
from social_media.users.models import User
from blog.forms import CreateBlogForm,SearchForm
from django.db import models
from django.db.models import Count, F, ExpressionWrapper
from django.db.models import Q
from taggit.models import Tag

from hitcount.views import HitCountDetailView
class BlogHomeView(TemplateView):
    template_name= 'blog/blog_home.html'

    def get_context_data(self, **kwargs):
      
        context = super().get_context_data(**kwargs)
        context['home_blogs'] = Blog.objects.all().order_by('?')
        context['recent_blogs'] = Blog.objects.all().order_by('-pub_date')[:4]
        # Query to get the most repeated tags for last 7 days
        start_date = timezone.now() - timedelta(days=7)
        most_repeated_tags = Tag.objects.filter(blog__pub_date__gte=start_date).annotate(
            tag_count = Count('blog__tags')).order_by('-tag_count')[:3]
        
        context['trendy_tags'] = most_repeated_tags
        return context

class TrendyTagView(TemplateView):
    template_name = 'blog/trendy_tag.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        tag_name= self.kwargs['tag']
        context['name'] = tag_name
        context['blogs_by_tag'] = Blog.objects.filter(tags__name=tag_name).order_by('-pub_date').all()
        
        return context
    
class CreateBlogView(CreateView):
    template_name = 'blog/create_blog.html'
    model= Blog
    form_class = CreateBlogForm

    def form_valid(self,form ):

        obj= form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        form.save_m2m()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('home')
    
class BlogDetailView(LoginRequiredMixin,HitCountDetailView):
    template_name = 'blog/blog_details.html'
    model = Blog
    context_object_name= 'blog'
    count_hit = True

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        blog= Blog.objects.get(id= self.kwargs['pk'])
        context['blog'] = blog
        context['comments'] = Comment.objects.filter(blog=blog).all
        return context

    def post(self,request,**kwargs):
        blog= Blog.objects.get(id=self.kwargs['pk'])
        if request.method == 'POST':
            comment_data = request.POST['comment']
            form = Comment(user= request.user,comment=comment_data,blog=blog)
            form.save()
            return HttpResponseRedirect(reverse('blog_details',args=(blog.id,)))


class BlogUpdateView(UpdateView):
    template_name = 'blog/blog_update.html'
    model = Blog
    form_class = CreateBlogForm

    def get_success_url(self,**kwargs):
        blog = Blog.objects.get(id = self.kwargs['pk'])
        return reverse('blog_details',args=(blog.id,))

class BlogDeleteView(DeleteView):
    template_name = 'blog/blog_home.html'
    model= Blog
    
    def get_success_url(self):
        return reverse('home')


class CreateCommentView(TemplateView):
    template_name = 'blog/blog_home.html'

    def post(self,request,**kwargs):
        blog= Blog.objects.get(id= self.kwargs['pk'])
        if request.method == 'POST':
            comment_data = request.POST['comment']
            
            form = Comment(user= request.user,comment=comment_data,blog=blog)
            form.save()
            return HttpResponseRedirect(reverse('home'))
 
    
class LikeView(TemplateView):
    template_name= 'blog/blog_details.html'

    def post(self,request,**kwargs):
        blog= Blog.objects.get(id=self.kwargs['pk'])
        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
            return HttpResponseRedirect(reverse('blog_details',args=(blog.id,)))
            liked = False
        else:
            blog.likes.add(request.user)
            liked =True
            return HttpResponseRedirect(reverse('blog_details',args=(blog.id,)))            



class CommentListView(LoginRequiredMixin,TemplateView):
    template_name= 'blog/blog_comments.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        blog= Blog.objects.get(id=self.kwargs['pk'])
        context['blog'] = blog
        context['comments'] = Comment.objects.filter(blog=blog)
        return context

class SearchView(TemplateView):
    template_name= 'blog/blog_search_results.html'
    
    def get(self, *args, **kwargs):
        if self.request.method =='GET':
            input_value = self.request.GET.get('input')
            if input_value:
                qs_results = Blog.objects.filter(
                    Q(tags__name = input_value) | Q(title__icontains=input_value)
                )
                return render(self.request,self.template_name,{'qs_results':qs_results})
            else:
                return reverse('search', args=['', 'all']) 



