from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choices


# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request, "questionsRules/index.html", {
#         "latest_question_list": latest_question_list
#         });

class IndexView(generic.ListView):
    template_name = "questionsRules/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        """Return all questions"""
        # return Question.objects.all()
        """Return questions 1er rule"""
        return Question.objects.filter(pk__in=[1,2]);


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
    
    #value=request.POST['TB_sample']
    # value = request.REQUEST.get(request,'TB_sample')
    # value = request.POST.get('TB_sample','')
    latest_question_list = Question.objects.filter(pk__in=[3,4])
    try:
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
        
    except (KeyError, Question.DoesNotExist, Choices.DoesNotExist):
        latest_question_list = Question.objects.filter(pk__in=[1,2])
        return render(request, "questionsRules/rules.html",{
            "latest_question_list": latest_question_list,
            "error_message": "No elegiste ninguna respuesta"
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