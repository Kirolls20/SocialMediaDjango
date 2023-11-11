from django.shortcuts import render
from django.urls import reverse
from questions.models import Question,Answer
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CreateNewQuestionForm


class QuestionsHomeView(LoginRequiredMixin,TemplateView):
    template_name = 'questions/question_home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all().order_by('?')
        return context

class CreateQuestionView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'questions/create_question.html'
    model = Question
    form_class = CreateNewQuestionForm
    success_message = ('Your Question has been submitted successfully!')
   

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit= False)
            obj.author = self.request.user
            obj.save()
            form.save_m2m()
            return super().form_valid(form)
    def get_success_url(self):
        return reverse('question_home')

class UpdateQuestionView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    template_name = 'questions/update_question.html'
    model = Question
    form_class = CreateNewQuestionForm
    success_message= ('Your Question was Updated!')
    success_url= 'question_home'

class DeleteQuestionView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    template_name = 'questions/question_home.html'
    model = Question
    success_message = ("The Question was successfully deleted.")
    
    def get_success_url(self):
        return reverse('question_home')

