from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView,DetailView,View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
#Internal imports 
from questions.models import Question,Answer
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

class QuestionDetailView(LoginRequiredMixin,DetailView):
    template_name = 'questions/question_details.html'
    model = Question
    context_object_name = 'question'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = Question.objects.get(id= self.kwargs['pk'])
        context['answers'] = Answer.objects.filter(question=context['question'])

        return context


class AnswerQuestionView(LoginRequiredMixin,SuccessMessageMixin,TemplateView):
    template_name = 'questions/question_home.html'

    def post(self,request,**kwargs):
        question = Question.objects.get(id=self.kwargs['pk'])
        user = self.request.user
        if request.method == 'POST':
            answer = request.POST['answer']
            obj = Answer(author=user,question=question,answer=answer)
            obj.save()
            messages.success(self.request,'Thanks for answering the question')
            return redirect('question_home')


# @method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class LikeQuestionView(LoginRequiredMixin,View):
    def post(self, request, **kwargs):
        question = Question.objects.get(id=self.kwargs['pk'])
        try:
            print('Entring the post')
            if question.likes.filter(id=request.user.id).exists():
                question.likes.remove(request.user)
                liked = False
            else:
                question.likes.add(request.user)
                liked = True
            return JsonResponse({'liked': liked, 'likes_count': question.likes.count()})
        except Exception as e :
            print(f'Error : {e}')
