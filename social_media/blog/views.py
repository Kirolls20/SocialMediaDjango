from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView

from blog.models import Blog,Comment,Author
from blog.forms import CreateBlogForm
def index(request):
    return render(request,'blog/blog_home.html',{})

class BlogHomeView(TemplateView):
    template_name= 'blog/blog_home.html'

    def get_context_data(self, **kwargs):
      
        context = super().get_context_data(**kwargs)
        context['home_blogs'] = Blog.objects.all()
        return context
    
class CreateBlogView(CreateView):
    template_name = 'blog/create_blog.html'
    model= Blog
    form_class = CreateBlogForm

    def form_valid(self,form ):

        obj= form.save(commit=False)
        obj.author = Author.objects.get(user=self.request.user)
        obj.save()
        form.save_m2m()
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse('home')
    
class BlogDetailView(DetailView):
    template_name = 'blog/blog_details.html'
    model = Blog
    context_object_name= 'blog'

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
 
    


