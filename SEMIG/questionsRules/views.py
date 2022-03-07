from msilib.schema import Error
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choices


def index(request):
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    question = Question.objects.get(pk = 1)
    return render(request, "questionsRules/index.html",{
        "latest_question_list": latest_question_list,
        "question": question
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

def rules(request, question_id):
    question = Question.objects.get(pk = question_id)
    if(question_id == 1 or question_id == 2):
        latest_question_list = Question.objects.filter(pk__in=[1,2])
    if(question_id == 3 or question_id == 4):
        latest_question_list = Question.objects.filter(pk__in=[3,4])
    if(question_id == 5):
        latest_question_list = Question.objects.filter(pk__in=[5])
    if(question_id == 6):
        latest_question_list = Question.objects.filter(pk__in=[6,7,8,9,10])
    if(question_id == 11):
        latest_question_list = Question.objects.filter(pk__in=[11,12,13,8,14])
    return render(request, "questionsRules/rules.html", {
    "latest_question_list": latest_question_list,
    "question": question
    });
    
    
def resp(request, question_id ):
    try:
        question = get_object_or_404(Question, pk = question_id)
        if(question.id == 1 or question.id == 2):
            question1 = request.POST['question1']
            question2 = request.POST['question2']
            latest_question_list = Question.objects.filter(pk__in=[3,4])
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
            elif(question1 == 'Si' and question2== 'No' ):
                question = get_object_or_404(Question, pk = 3)
                return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
                # return render(request, "questionsRules/rules.html", {
                #     "latest_question_list": latest_question_list,
                #     "question": question
                # })
        elif(question.id == 3 or question.id == 4):
            latest_question_list = Question.objects.filter(pk__in=[5])
            question1 = request.POST['question3']
            question2 = request.POST['question4']
            if((question1=='si' and question2 == 'Si') or (question1=='no' and question2=='Si')):
                return render(request, "questionsRules/gorgojoInformation.html", {
                    "latest_question_list": latest_question_list
                })
            else:
                question = get_object_or_404(Question, pk = 5)
                return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
        elif(question.id == 5):
            question1 = request.POST['question5']
            if(question1 == 'Recién planeo empezar mi cultivo'):
                question = get_object_or_404(Question, pk = 6)
            else:
                question = get_object_or_404(Question, pk = 11)
                
    except (ValueError, KeyError, Question.DoesNotExist, Choices.DoesNotExist):
        if(question_id == 1 or question_id == 2):
            latest_question_list = Question.objects.filter(pk__in=[1,2])
        if(question_id == 3 or question_id == 4):
            latest_question_list = Question.objects.filter(pk__in=[3,4])
        if(question_id == 5):
            latest_question_list = Question.objects.filter(pk__in=[5])
        if(question_id == 6):
            latest_question_list = Question.objects.filter(pk__in=[6,7,8,9,10])
        if(question_id == 11):
            latest_question_list = Question.objects.filter(pk__in=[11,12,13,8,14])
        return render(request, "questionsRules/rules.html",{
            "latest_question_list": latest_question_list,
            "error_message": "Debes elegir alguna respuesta",
            "question" : question
        })
    else:
        return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
    
    
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