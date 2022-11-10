from django.shortcuts import render
# from django import views

# Create your views here.
from django.http import HttpResponse
from myapp.models   import Question
from myapp.models   import Choice


def index(request):
    return HttpResponse("Hello, world")


def question_1(request):
    questions = Question.objects.all()
    return render(request,"mcq.html",{'questions':questions})

    
    # all_question = Question.objects.all()
    

def option(request,id):
    context={}
    context["beinex"]=Choice.objects.filter(question=id)
    # cho = Choice.objects.get(question=id)
    return render(request,"ans.html",context)
