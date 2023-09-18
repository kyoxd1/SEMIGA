from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import NoReverseMatch, reverse

from .knowledgeForGorgojo import *
import random
# from .knowledgeForGorgojo import *
from .models import Question, Choices, Lottery, LotteryOptions
     

def index(request):
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    question = Question.objects.get(pk = 1)
    return render(request, "questionsRules/index.html",{
        "latest_question_list": latest_question_list,
        "question": question
        });

def objective(request):
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    question = Question.objects.get(pk = 1)
    return render(request, "questionsRules/objective.html",{
        "latest_question_list": latest_question_list,
        "question": question
    });
    
def contact(request):
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    question = Question.objects.get(pk = 1)
    return render(request, "questionsRules/Contact.html",{
        "latest_question_list": latest_question_list,
        "question": question
    });  

def rules(request, question_id):
    try:
        if(question_id == (7 or 8 or 9 or 10 or 12 or 13 or 14 or 16 or 17 or 20 or 21 or 22)):
            response =  render(request, "questionsRules/pagError.html")
            return response
        question = Question.objects.get(pk = question_id)
        engine = integratedHandling()
        engine.reset()
        engine.declare(QuestionList(questionId=question_id))
        engine.run()
        latest_question_list = engine.listQuestion
        if(latest_question_list.count() == 0):
            response =  render(request, "questionsRules/pagError.html")
            return response
        return render(request, "questionsRules/rules.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    except (ValueError, KeyError, Question.DoesNotExist, Choices.DoesNotExist, NoReverseMatch):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    
    
def lotteryRules(request, question_id):
    try:
        question = question_id
        engine = integrateHanlingLottery()
        engine.reset()    
        engine.declare(RandomList(questionId=1))
        engine.run()
        latest_question_list = engine.listQuestion
        question = engine.questionL
        if(latest_question_list.count() == 0):
            response =  render(request, "questionsRules/pagError.html")
            return response
        return render(request, "questionsRules/loteryrules.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    except (ValueError, KeyError, Lottery.DoesNotExist, LotteryOptions.DoesNotExist, NoReverseMatch):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    
## Realizado el response para el sistema experto
def loteryresp(request, question_id):
    try:
        question = question_id
        engine = integrateHanlingLottery()
        if(question==123):
            question1 = request.POST['question1']
            question2 = request.POST['question2']
            question3 = request.POST['question3']
            latest_question_list = Lottery.objects.filter(pk__in=[1,3,4])
            engine.reset()
            engine.declare(GorgojoLottery123(question1=question1, question2=question2, question3=question3))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la: Pregunta 1 ¿Conoce al Gorgojo de Los Andes?: '+question1+', Pregunta 2 ¿Que Hongo se puede poner en el almacen o lugar donde guarda la papa?: '+question2+', y Pregunta 3 Si el Gorgojo de Los Andes aparece en su cultivo ¿Qué es lo primero que haría?:'+question3
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
            
        elif(question==124):
            latest_question_list = Lottery.objects.filter(pk__in=[1,2,4])
            question1 = request.POST['question1']
            question2 = request.POST['question2']
            question4 = request.POST['question4']
            engine.reset()
            engine.declare(GorgojoLottery124(question1=question1, question2=question2, question4=question4))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la: Pregunta 1 ¿Conoce al Gorgojo de Los Andes?: '+question1+', Pregunta 2 ¿Que Hongo se puede poner en el almacen o lugar donde guarda la papa?: '+question2+', y Pregunta 3 ¿En el cultivo de papa es necesario colocar trampas?:'+question4
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        
        elif(question == 125):
            question1 = request.POST['question1']
            question2 = request.POST['question2']
            question5 = request.POST['question5']
            engine.reset()
            engine.declare(GorgojoLottery125(question1=question1,question2=question2,question5=question5))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la: Pregunta 1 ¿Conoce al Gorgojo de Los Andes?: '+question1+', Pregunta 2 ¿Que Hongo se puede poner en el almacen o lugar donde guarda la papa?: '+question2+', y Pregunta 3 ¿Se puede sembrar otros cultivos alrededor de la papa? (Como ser cebada, cebolla, etc.):'+question5
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        
        elif(question == 126):
            question1 = request.POST['question1']
            question2 = request.POST['question2']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery126(question1=question1, question2=question2, question6 =question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la: Pregunta 1 ¿Conoce al Gorgojo de Los Andes?: '+question1+', Pregunta 2 ¿Que Hongo se puede poner en el almacen o lugar donde guarda la papa?: '+question2+', y Pregunta 3 ¿Qué hace usted al momento de recolectar la papa?:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        
        elif(question == 134):
            question1 = request.POST['question1']
            question3 = request.POST['question3']
            question4 = request.POST['question4']
            engine.reset()
            engine.declare(GorgojoLottery134(question1=question1, question3=question3, question4 =question4))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la: Pregunta 1 ¿Conoce al Gorgojo de Los Andes?: '+question1+', Pregunta 2 Si el Gorgojo de Los Andes aparece en su cultivo ¿Qué es lo primero que haría?: '+question3+', y Pregunta 3 ¿En el cultivo de papa es necesario colocar trampas?:'+question4
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 135):
            question1 = request.POST['question1']
            question3 = request.POST['question3']
            question5 = request.POST['question5']
            engine.reset()
            engine.declare(GorgojoLottery135(question1=question1, question3=question3, question5 =question5))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la: Pregunta 1 ¿Conoce al Gorgojo de Los Andes?: '+question1+', Pregunta 2 Si el Gorgojo de Los Andes aparece en su cultivo ¿Qué es lo primero que haría?: '+question3+', y Pregunta 3 ¿Se puede sembrar otros cultivos alrededor de la papa? (Como ser cebada, cebolla, etc.):'+question5
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))  
        
        elif(question == 136):
            question1 = request.POST['question1']
            question3 = request.POST['question3']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery136(question1=question1, question3=question3, question6 =question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la: Pregunta 1 ¿Conoce al Gorgojo de Los Andes?: '+question1+', Pregunta 2 Si el Gorgojo de Los Andes aparece en su cultivo ¿Qué es lo primero que haría?: '+question3+', y Pregunta 3 ¿Qué hace usted al momento de recolectar la papa?:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        
        elif(question == 145):
            question1 = request.POST['question1']
            question4 = request.POST['question4']
            question5 = request.POST['question5']
            engine.reset()
            engine.declare(GorgojoLottery145(question1=question1, question4=question4, question5 =question5))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question1+', Pregunta 2: '+question4+', y Pregunta 3:'+question5
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 146):
            question1 = request.POST['question1']
            question4 = request.POST['question4']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery146(question1=question1, question4=question4, question6 =question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question1+', Pregunta 2: '+question4+', y Pregunta 3:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 156):
            question1 = request.POST['question1']
            question5 = request.POST['question5']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery156(question1=question1, question5=question5, question6 =question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question1+', Pregunta 2: '+question5+', y Pregunta 3:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 234):
            question2 = request.POST['question2']
            question3 = request.POST['question3']
            question4 = request.POST['question4']
            engine.reset()
            engine.declare(GorgojoLottery234(question2=question2, question3=question3, question4 =question4))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question2+', Pregunta 2: '+question3+', y Pregunta 3:'+question4
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 235):
            question2 = request.POST['question2']
            question3 = request.POST['question3']
            question5 = request.POST['question5']
            engine.reset()
            engine.declare(GorgojoLottery235(question2=question2, question3=question3, question5 =question5))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question2+', Pregunta 2: '+question3+', y Pregunta 3:'+question5
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 236):
            question2 = request.POST['question2']
            question3 = request.POST['question3']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery236(question2=question2, question3=question3, question6=question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question2+', Pregunta 2: '+question3+', y Pregunta 3:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 245):
            question2 = request.POST['question2']
            question4 = request.POST['question4']
            question5 = request.POST['question5']
            engine.reset()
            engine.declare(GorgojoLottery245(question2=question2, question4=question4, question5 =question5))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 245'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la Pregunta 1 : '+question2+', Pregunta 2: '+question4+', y Pregunta 3:'+question5
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 246):
            question2 = request.POST['question2']
            question4 = request.POST['question4']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery246(question2=question2, question4=question4, question6=question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question2+', Pregunta 2: '+question4+', y Pregunta 3:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 256):
            question2 = request.POST['question2']
            question5 = request.POST['question5']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery256(question2=question2, question5=question5, question6=question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la Pregunta 1 : '+question2+', Pregunta 2:'+question5+', y Pregunta 3:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 345):
            question3 = request.POST['question3']
            question4 = request.POST['question4']
            question5 = request.POST['question5']
            engine.reset()
            engine.declare(GorgojoLottery345(question3=question3, question4=question4, question5 =question5))
            engine.run()
            urlRedirect = engine.urlRedirect
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la \n Pregunta 1 : '+question3+', Pregunta 2:'+question4+', y Pregunta 3: '+question5
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 346):
            question3 = request.POST['question3']
            question4 = request.POST['question4']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery346(question3=question3, question4=question4, question6=question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas:, Pregunta 1  : '+question3+', Pregunta 2: '+question4+', y Pregunta 3:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 356):
            question3 = request.POST['question3']
            question5 = request.POST['question5']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery356(question3=question3, question5=question5, question6=question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question3+', Pregunta 2: '+question5+', y Pregunta 3:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        elif(question == 456):
            question4 = request.POST['question4']
            question5 = request.POST['question5']
            question6 = request.POST['question6']
            engine.reset()
            engine.declare(GorgojoLottery456(question4=question4, question5=question5, question6=question6))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            tarea = 'Prueba tarea 123'
            sugesstion = engine.sugesstion
            respuestas = 'Según sus respuestas a la </br> Pregunta 1 : '+question4+', Pregunta 2: '+question5+', y Pregunta 3:'+question6
            return HttpResponseRedirect(reverse(urlRedirect, args=(1,tarea,sugesstion,respuestas,)))
        
        
                
    except (ValueError, KeyError, Lottery.DoesNotExist, LotteryOptions.DoesNotExist):
        engine = integrateHanlingLottery()
        engine.reset()
        engine.declare(RandomList(questionId=1))
        engine.run()
        latest_question_list = engine.listQuestion
        question = engine.questionL
        
        return render(request, "questionsRules/loteryrules.html",{
            "latest_question_list": latest_question_list,
            "error_message": "Debes elegir alguna respuesta",
            "question" : question
        })
    else:
        return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
    
def Prueba(request, question_id, tarea, sugesstion,respuestas):
    question = 1
    engine = integrateHanlingLottery()
    engine.reset()
    engine.declare(RandomList(questionId=1))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/Prueba.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "respuestas":respuestas,
        "sugesstion" : sugesstion
    });
        
def resp(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
        engine = integratedHandling()
        if(question.id == 1 or question.id == 2):
            question1 = request.POST['question1']
            question2 = request.POST['question2']
            latest_question_list = Question.objects.filter(pk__in=[3,4])
            engine.reset()
            engine.declare(GorgojoQuestion(question1=question1, question2=question2))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question[0]
            if(engine.sugesstion==''):
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            else:
                tarea = question1+' conoce a la plaga del Gorgojo de Los Andes y de que '+question2+' es su primer cultivo.'
                sugesstion = engine.sugesstion
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,tarea,sugesstion,)))
            
        elif(question.id == 3 or question.id == 4):
            latest_question_list = Question.objects.filter(pk__in=[5])
            question1 = request.POST['question3']
            question2 = request.POST['question4']
            engine.reset()
            engine.declare(GorgojoQuestionTwo(question3=question1, question4=question2))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question[0]
            if(engine.sugesstion==''):
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            else:
                tarea = question1+' tuvo la plaga del gorgojo anteriormente pero '+question2+' vio que su cultivo fue afectado por la plaga.'
                sugesstion = engine.sugesstion
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,tarea,sugesstion,)))
        
        elif(question.id == 5):
            question1 = request.POST['question5']
            engine.reset()
            engine.declare(GorgojoQuestionThree(resp=question1))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question[0]
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
        
        elif(question.id == 6):
            question6 = request.POST['question6']
            question7 = request.POST['question7']
            question8 = request.POST['question8']
            question9 = request.POST['question9']
            question10 = request.POST['question10']
            engine.reset()
            engine.declare(GorgojoQuestionFor(question6=question6, question7=question7, question8 =question8, question9 = question9, question10= question10))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question[0]
            if(engine.sugesstion==''):
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            else:
                tarea = question10 +' conoce las trampas para el cultivo, '+question7+' elaboró zanjas, '+question8+' sabe la barrera vegetal,'+question6+' realizo desinfecciones químicas y '+question9+' removió las k`ipas'
                sugesstion = engine.sugesstion
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,tarea,sugesstion,)))
        elif(question.id == 11):
            question11 = request.POST['question11']
            question12 = request.POST['question12']
            question13 = request.POST['question13']
            question8 = request.POST['question8']
            question14 = request.POST['question14']
            question10 = request.POST['question10']
            engine.reset()
            engine.declare(GorgojoQuestionFive(question11=question11, question12=question12, question13 =question13, question8 = question8, question14= question14, question10= question10))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question[0]
            if(engine.sugesstion==''):
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            else:
                tarea = 'Su cultivo '+question14+' esta a salvo de la plaga, '+question12+' realizó zanjas, '+question10 +' conoce las trampas para el cultivo, '+question13+' elaboró el aporque, '+question11+' conoce productos químicos orgánicos e inorgánicos y '+question8+' sabe la barrera vegetal'
                sugesstion = engine.sugesstion
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,tarea,sugesstion,)))
        elif(question.id == 15):
            question11 = request.POST['question11']
            question12 = request.POST['question12']
            question13 = request.POST['question13']
            question14 = request.POST['question14']
            question15 = request.POST['question15']
            question16 = request.POST['question16']
            question17 = request.POST['question17']
            engine.reset()
            engine.declare(GorgojoQuestionSix(question11=question11, question12=question12, question13 =question13, question14 = question14, question15= question15, question16= question16, question17= question17))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question[0]
            if(engine.sugesstion==''):
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            else:
                tarea = question16 +' realizó la recolección de la plaga, '+'su cultivo '+question14+' esta a salvo de la plaga, '+question12+' realizó zanjas, '+question15 +' conocó las trampas para el cultivo, '+question13+' elaboró el aporque, '+question11+' conoce productos químicos orgánicos e inorgánicos y '
                
                if question17=='No':
                    prueba = 'No pudo detener a la plaga y ahora su cultivo corre peligro!!!!!'
                else:
                    prueba = 'Si pudo detener a la plaga y su cultivo esta a salvo por ahora. '
                
                tarea = tarea + prueba
                sugesstion = engine.sugesstion
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,tarea,sugesstion,)))
        elif(question.id == 18):
            question16 = request.POST['question16']
            question17 = request.POST['question17']
            question18 = request.POST['question18']
            engine.reset()
            engine.declare(GorgojoQuestionSeven(question16=question16, question17=question17, question18 =question18))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question[0]
            if(engine.sugesstion==''):
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            else:
                tarea = question16 +' realizó la recolección de la plaga, '+question18+' sabe en que seleccionar la papa de su cultivo y '
                
                if question17=='No':
                    prueba = 'No pudo detener a la plaga y ahora su cultivo corre peligro!!!!!'
                else:
                    prueba = 'Si pudo detener a la plaga y su cultivo esta a salvo por ahora. '
                
                tarea = tarea + prueba
                sugesstion = engine.sugesstion
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,tarea,sugesstion,)))
        elif(question.id == 19):
            question19 = request.POST['question19']
            question20 = request.POST['question20']
            question21 = request.POST['question21']
            question22 = request.POST['question22']
            engine.reset()
            engine.declare(GorgojoQuestionEight(question19=question19, question20=question20, question21 =question21, question22=question22))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question[0]
            if(engine.sugesstion==''):
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            else:
                tarea = question22 +' conoce la utilidad del Hongo Blanco, '+question19+' removió el suelo de donde recolecto la papa, '+question20+' puso la papa en un almacén y '
                if question21=='No':
                    prueba = 'No cree que su cultivo esta asalvo en un almacén'
                else:
                    prueba = 'Si esta seguro su papa en el almacén'
                
                tarea = tarea + prueba
                sugesstion = engine.sugesstion
                return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,tarea,sugesstion,)))
                
    except (ValueError, KeyError, Question.DoesNotExist, Choices.DoesNotExist):
        engine = integratedHandling()
        engine.reset()
        engine.declare(QuestionList(questionId=question_id))
        engine.run()
        latest_question_list = engine.listQuestion
        return render(request, "questionsRules/rules.html",{
            "latest_question_list": latest_question_list,
            "error_message": "Debes elegir alguna respuesta",
            "question" : question
        })
    else:
        return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
    
    
def gorgojoInformation(request,question_id, tarea,sugesstion):
    if(question_id != 3):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    latest_question_list = Question.objects.filter(pk__in=[3,4])
    question = Question.objects.get(pk = question_id)
    return render(request, "questionsRules/gorgojoInformation.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
        });
    
    
def gorgojoInformationAndGoodPractice(request, question_id, tarea,sugesstion):
    if(question_id != 3):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in=[3,4])
    return render(request, "questionsRules/gorgojoInformationAndGoodPractice.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
        });
    

def goodPractices(request, question_id, tarea,sugesstion):
    if(question_id != 3):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in=[3,4])
    return render(request, "questionsRules/goodPractices.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
        });
    
def preventiveMeasures(request, question_id, tarea, sugesstion):
    if(question_id != 5):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in=[5])
    return render(request, "questionsRules/preventiveMeasures.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
        });
    
    
def chemicals(request, question_id, tarea, sugesstion):
    if(question_id != 6 and question_id != 11 and question_id != 15):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/chemicals.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    });
    
def ditches(request, question_id, tarea, sugesstion):
    if(question_id != 6 and question_id != 11 and question_id != 15):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/ditches.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    });
    
def plantOtherVegetables(request, question_id, tarea, sugesstion):
    if(question_id != 6 and question_id != 11):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/plantOtherVegetables.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    });

def plantPickUp(request, question_id, tarea, sugesstion):
    if(question_id != 6):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in=[6,7,8,9,10])
    return render(request, "questionsRules/plantPickUp.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    });

def traps(request, question_id, tarea, sugesstion):
    if(question_id != 6 and question_id != 11 and question_id != 15):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/traps.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    });
    
    
def continueStageChoice(request, question_id):
    if(question_id != 11 and question_id != 15 and question_id != 18 and question_id != 19):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/continueStageChoice.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });
    
def culturalWork(request, question_id, tarea, sugesstion):
    if(question_id != 11 and question_id != 15):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/culturalWork.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    });
    
def gorgojoMeasures(request, question_id, tarea, sugesstion):
    if(question_id != 11 and question_id != 15):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/gorgojoMeasures.html", {
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    });
    
def gatherGorgojo(request, question_id, tarea, sugesstion):
    if(question_id != 15 and question_id != 18):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/gatherGorgojo.html",{
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    })
    
def countherTheGorgojo(request, question_id, tarea, sugesstion):
    if(question_id != 15 and question_id != 18):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk= question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/countherTheGorgojo.html",{
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    })
    
def potatoSelection(request, question_id, tarea, sugesstion):
    if(question_id != 18):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in = [16,17,18])
    return render(request, "questionsRules/potatoSelection.html",{
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    })
    
def soilRemoval(request, question_id, tarea, sugesstion):
    if(question_id != 19):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in=[19,20,21,22])
    return render(request, "questionsRules/soilRemoval.html",{
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    })
    
def warehousePreparation(request, question_id, tarea, sugesstion):
    if(question_id != 19):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in=[19,20,21,22])
    return render(request, "questionsRules/warehousePreparation.html",{
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    })
    
def dangerIntoWarehouse(request, question_id, tarea, sugesstion):
    if(question_id != 19):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in=[19,20,21,22])
    return render(request, "questionsRules/dangerIntoWarehouse.html",{
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    })
    
def whiteFungus(request, question_id, tarea, sugesstion):
    if(question_id != 19):
        response =  render(request, "questionsRules/pagError.html")
        response.status_code = 404
        return response
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.filter(pk__in=[19,20,21,22])
    return render(request, "questionsRules/whiteFungus.html",{
        "latest_question_list": latest_question_list,
        "question": question,
        "tarea":tarea,
        "sugesstion" : sugesstion
    })
    
def pagError(request):
    response =  render(request,"questionsRules/pagError.html", {})
    response.status_code = 404
    return response
