from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
from .models import Question
from django.views import View

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    # context maps template variable names to python objects
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "you're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class ShowTimeView(View):

    def get(self, request):
        now = datetime.now()
        html = "<html><body>It is now {}<body></html>".format(now)
        return HttpResponse(html)

