from msilib.schema import Error
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from experta import *

from .knowledgeForGorgojo import *

from .models import Question, Choices
     

def index(request):
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    question = Question.objects.get(pk = 1)
    return render(request, "questionsRules/index.html",{
        "latest_question_list": latest_question_list,
        "question": question
        });


def prueba(request):
    return render(request, "questionsRules/prueba.html",);
# def detail(request, question_id):
#     question = get_object_or_404(Question,pk= question_id)
#     return render(request, "questionsRules/detail.html", {
#         "question": question
#     });

def rules(request, question_id):
    question = Question.objects.get(pk = question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    # if(question_id == 1 or question_id == 2):
    #     latest_question_list = Question.objects.filter(pk__in=[1,2])
    # if(question_id == 3 or question_id == 4):
    #     latest_question_list = Question.objects.filter(pk__in=[3,4])
    # if(question_id == 5):
    #     latest_question_list = Question.objects.filter(pk__in=[5])
    # if(question_id == 6):
    #     latest_question_list = Question.objects.filter(pk__in=[6,7,8,9,10])
    # if(question_id == 11):
    #     latest_question_list = Question.objects.filter(pk__in=[11,12,13,10,8,14])
    # if(question_id == 15):
    #     latest_question_list = Question.objects.filter(pk__in=[11,12,13,14,15,16,17])
    # if(question_id == 18):
    #     latest_question_list = Question.objects.filter(pk__in=[16,17,18])
    # if(question_id == 19):
    #     latest_question_list = Question.objects.filter(pk__in=[19,20,21,22])
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
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestion(question1=question1, question2=question2))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            
            # if(question1=='No' and question2 == 'No'):
            #     return HttpResponseRedirect(reverse("questionsRules:gorgojoInformation", args=(question.id,)))
            # elif(question1=='Si' and question2 == 'Si'):
            #     return HttpResponseRedirect(reverse("questionsRules:gorgojoInformation", args=(question.id,)))
            # elif(question1=='No' and question2 == 'Si'):
            #     return HttpResponseRedirect(reverse("questionsRules:gorgojoInformation", args=(question.id,)))
            # elif(question1 == 'Si' and question2== 'No' ):
            #     question = get_object_or_404(Question, pk = 3)
            #     return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
            # return render(request, "questionsRules/rules.html", {
            #     "latest_question_list": latest_question_list,
            #     "question": question
            # })
            
        elif(question.id == 3 or question.id == 4):
            latest_question_list = Question.objects.filter(pk__in=[5])
            question1 = request.POST['question3']
            question2 = request.POST['question4']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionTwo(question3=question1, question4=question2))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            # if((question1=='si' and question2 == 'Si') or (question1=='no' and question2=='Si')):
            #     return render(request, "questionsRules/gorgojoInformation.html", {
            #         "latest_question_list": latest_question_list
            #     })
            #     return HttpResponseRedirect(reverse("questionsRules:gorgojoInformation", args=(question.id,)))
            # else:
            #     question = get_object_or_404(Question, pk = 5)
            #     return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
        elif(question.id == 5):
            question1 = request.POST['question5']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionThree(resp=question1))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            # if(question1 == 'Recién planeo empezar mi cultivo'):
            #     question = get_object_or_404(Question, pk = 6)
            # elif(question1 == 'Acabo de sembrar'):
            #     question = get_object_or_404(Question, pk = 11)
            # elif(question1 == 'Mi cultivo de papa, ya esta más de la mitad'):
            #     question = get_object_or_404(Question, pk = 15)
            # elif(question1 == 'Estoy por cosechar mi cultivo'):
            #     question = get_object_or_404(Question, pk = 18)
            # elif(question1 == 'Acabo de cosechar mi cultivo'):
            #     question = get_object_or_404(Question, pk = 19)
        elif(question.id == 6):
            question6 = request.POST['question6']
            question7 = request.POST['question7']
            question8 = request.POST['question8']
            question9 = request.POST['question9']
            question10 = request.POST['question10']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionFor(question6=question6, question7=question7, question8 =question8, question9 = question9, question10= question10))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
        elif(question.id == 11):
            question1 = request.POST['question11']
            question2 = request.POST['question12']
            question3 = request.POST['question13']
            question4 = request.POST['question8']
            question5 = request.POST['question14']
            if(question1 == 'No'):
                return HttpResponseRedirect(reverse("questionsRules:gorgojoInformation", args=(question.id,)))
        elif(question.id == 15):
            question1 = request.POST['question11']
            question2 = request.POST['question12']
            question3 = request.POST['question13']
            question4 = request.POST['question14']
            question5 = request.POST['question15']
            question6 = request.POST['question16']
            question7 = request.POST['question17']
        elif(question.id == 18):
            question1 = request.POST['question16']
            question2 = request.POST['question17']
            question3 = request.POST['question18']
        elif(question.id == 19):
            question1 = request.POST['question19']
            question2 = request.POST['question20']
            question3 = request.POST['question21']
            question4 = request.POST['question22']
                
    except (ValueError, KeyError, Question.DoesNotExist, Choices.DoesNotExist):
        engine = integratedHandling()
        engine.reset()
        engine.declare(QuestionList(questionId=question_id))
        engine.run()
        latest_question_list = engine.listQuestion
        # if(question_id == 1 or question_id == 2):
        #     latest_question_list = Question.objects.filter(pk__in=[1,2])
        # if(question_id == 3 or question_id == 4):
        #     latest_question_list = Question.objects.filter(pk__in=[3,4])
        # if(question_id == 5):
        #     latest_question_list = Question.objects.filter(pk__in=[5])
        # if(question_id == 6):
        #     latest_question_list = Question.objects.filter(pk__in=[6,7,8,9,10])
        # if(question_id == 11):
        #     latest_question_list = Question.objects.filter(pk__in=[11,12,13,8,14])
        # if(question_id == 15):
        #     latest_question_list = Question.objects.filter(pk__in=[11,12,13,14,15,16,17])
        # if(question_id == 18):
        #     latest_question_list = Question.objects.filter(pk__in=[16,17,18])
        # if(question_id == 19):
        #     latest_question_list = Question.objects.filter(pk__in=[19,20,21,22])
        return render(request, "questionsRules/rules.html",{
            "latest_question_list": latest_question_list,
            "error_message": "Debes elegir alguna respuesta",
            "question" : question
        })
    else:
        return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
    
    
def gorgojoInformation(request, question_id):
    # latest_question_list = Question.objects.filter(pk__in=[3,4])
    question = get_object_or_404(Question, pk=question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/gorgojoInformation.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    # if(question_id == 1 or question_id == 2):
    #     latest_question_list = Question.objects.filter(pk__in=[1,2])
    # if(question_id == 3 or question_id == 4):
    #     latest_question_list = Question.objects.filter(pk__in=[3,4])
    # if(question_id == 5):
    #     latest_question_list = Question.objects.filter(pk__in=[5])
    # if(question_id == 6):
    #     latest_question_list = Question.objects.filter(pk__in=[6,7,8,9,10])
    # if(question_id == 11):
    #     latest_question_list = Question.objects.filter(pk__in=[11,12,13,8,14])
    # if(question_id == 15):
    #     latest_question_list = Question.objects.filter(pk__in=[11,12,13,14,15,16,17])
    # if(question_id == 18):
    #     latest_question_list = Question.objects.filter(pk__in=[16,17,18])
    # if(question_id == 19):
    #     latest_question_list = Question.objects.filter(pk__in=[19,20,21,22])
    
def gorgojoInformationAndGoodPractice(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/gorgojoInformationAndGoodPractice.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    

def goodPractices(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/goodPractices.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    
def preventiveMeasures(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[5])
    return render(request, "questionsRules/preventiveMeasures.html", {
        "latest_question_list": latest_question_list,
        "question": question
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