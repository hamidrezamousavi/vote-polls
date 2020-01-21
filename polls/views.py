from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    content={'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',content)

def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    content={'question':question}
    return render(request,'polls/detail.html',content)

def vote(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,"polls/detail.html",{'question':question,'error_message':'select and choice'})
    else:    
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    return render(request,"polls/results.html",{'question':question})