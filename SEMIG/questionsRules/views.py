from msilib.schema import Error
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choices


def index(request):
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/index.html",{
        "latest_question_list": latest_question_list
        });

# class IndexView(generic.ListView):
#     template_name = "questionsRules/index.html"
#     context_object_name = "latest_question_list"
    
#     def get_queryset(self):
#         """Return all questions"""
#         # return Question.objects.all()
#         """Return questions 1er rule"""
#         return Question.objects.filter(pk__in=[1,2]);


# def detail(request, question_id):
#     question = get_object_or_404(Question,pk= question_id)
#     return render(request, "questionsRules/detail.html", {
#         "question": question
#     });

def rules(request):
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/rules.html", {
    "latest_question_list": latest_question_list
    });
    
    
def resp(request):  
    try:
        if('question1' in request.POST and 'question2' in request.POST):
            latest_question_list = Question.objects.filter(pk__in=[3,4])
            question1 = request.POST['question1']
            question2 = request.POST['question2']
            if(question1=='No' and question2 == 'No'):
                return render(request, "questionsRules/gorgojoInformation.html", {
                    "latest_question_list": latest_question_list
                })
            elif(question1=='Si' and question2 == 'Si'):
                return render(request, "questionsRules/gorgojoInformation.html", {
                    "latest_question_list": latest_question_list
                })
            elif(question1=='No' and question2 == 'Si'):
                return render(request, "questionsRules/gorgojoInformation.html", {
                    "latest_question_list": latest_question_list
                })
            else:
                return render(request, "questionsRules/rules.html", {
                    "latest_question_list": latest_question_list
                })       
        elif('question3' in request.POST and 'question4' in request.POST):
            latest_question_list = Question.objects.filter(pk__in=[5])
            question1 = request.POST['question3']
            question2 = request.POST['question4']
            if(question1=='Si' and question2 == 'Si' or question1=='No' and question2=='Si'):
                return render(request, "questionsRules/gorgojoInformation.html", {
                    "latest_question_list": latest_question_list
                })
            else:
                return render(request, "questionsRules/rules.html", {
                    "latest_question_list": latest_question_list
                })
        else:
            return render(request, "questionsRules/rules.html",{
            "latest_question_list": latest_question_list,
            "error_message": "Debes elegir alguna respuesta"
        })
    except (UnboundLocalError, ValueError, KeyError, Question.DoesNotExist, Choices.DoesNotExist):
        if('question1' in request.POST or 'question2' in request.POST):
            latest_question_list = Question.objects.filter(pk__in=[1,2])
        elif('question3' in request.POST or 'question4' in request.POST):
            latest_question_list = Question.objects.filter(pk__in=[3,4])
        else:
            latest_question_list = Question.objects.filter(pk__in=[5]) 
        return render(request, "questionsRules/rules.html",{
            "latest_question_list": latest_question_list,
            "error_message": "Debes elegir alguna respuesta"
        })
    
    
def gorgojoInformation(request, latest_question_list):
    # latest_question_list = Question.objects.filter(pk__in=[3,4])
    return render(request, "questionsRules/gorgojoInformation.html", {
        "latest_question_list": latest_question_list
        });
    
class DetailView(generic.DetailView):
    model = Question
    template_name= "questionsRules/detail.html"


def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choices_set.get(pk = request.POST["choice"])
    except (KeyError, Choices.DoesNotExist):
        return render(request, "questionsRules/detail.html",{
            "question": question,
            "error_message": "No elegiste ninguna respuesta"
        })
    else:
        new_question_id = question_id + selected_choice.id
        return HttpResponseRedirect(reverse("questionsRules:detail", args=(new_question_id,)))