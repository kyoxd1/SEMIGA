from django.shortcuts import get_object_or_404
from experta import KnowledgeEngine,Rule,Fact, AS, L

from .models import Question

class QuestionList(Fact):
    """Obtendra un valor questionId para determinar cual sera la lista de preguntas
        que debe devolver para que el usuario responda"""
    pass


class GorgojoQuestion(Fact):
    """_summary_
    GORGOJO QUESTION:
    Lanzado para la primera etapa de preguntas del Sistema
    
    Args:
        Fact (question1, question2): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    pass


class GorgojoQuestionTwo(Fact):
    pass


class GorgojoQuestionThree(Fact):
    pass

class GorgojoQuestionFor(Fact):
    pass


class GorgojoQuestionFive(Fact):
    pass


class integratedHandling(KnowledgeEngine):
    question = get_object_or_404(Question, pk =1)
    urlRedirect = "questionsRules:rules"
    listQuestion = Question.objects.filter(pk__in=[1,2])
    
    @Rule(AS.questionList << QuestionList(questionId=L(1) | L(2)))
    def QuestionList_One(self):
        listQuestion = Question.objects.filter(pk__in=[1,2])
        return self.listQuestion
    
    @Rule(AS.questionList << QuestionList(questionId=L(3) | L(4)))
    def QuestionList_Two(self):
        listQuestion = Question.objects.filter(pk__in=[3,4])
        self.listQuestion = listQuestion
        return self.listQuestion
    
    @Rule(QuestionList(questionId =5))
    def QuestionList_Three(self):
        listQuestion = Question.objects.filter(pk__in=[5])
        self.listQuestion = listQuestion
        return self.listQuestion
    
    @Rule(QuestionList(questionId =6))
    def QuestionList_For(self):
        listQuestion = Question.objects.filter(pk__in=[6,7,8,9,10])
        self.listQuestion = listQuestion
        return self.listQuestion
    
    @Rule(QuestionList(questionId =11))
    def QuestionList_Five(self):
        listQuestion = Question.objects.filter(pk__in=[11,12,13,8,10,14])
        self.listQuestion = listQuestion
        return self.listQuestion
    
    @Rule(QuestionList(questionId =15))
    def QuestionList_Six(self):
        listQuestion = Question.objects.filter(pk__in=[11,12,13,14,15,16,17])
        self.listQuestion = listQuestion
        return self.listQuestion
    
    @Rule(QuestionList(questionId =18))
    def QuestionList_Seven(self):
        listQuestion = Question.objects.filter(pk__in=[16,17,18])
        self.listQuestion = listQuestion
        return self.listQuestion
    
    @Rule(QuestionList(questionId =19))
    def QuestionList_Eight(self):
        listQuestion = Question.objects.filter(pk__in=[19,20,21,22])
        self.listQuestion = listQuestion
        return self.listQuestion
    
    
    @Rule(GorgojoQuestion(question1='Si',question2='No'))
    def GorgojoQuestion_rule1(self):
        question = get_object_or_404(Question, pk = 3)
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect

    @Rule(GorgojoQuestion(question1='Si',question2='Si'))
    def GorgojoQuestion_rule2(self):
        question = get_object_or_404(Question, pk = 3)
        urlRedirect = "questionsRules:goodPractices"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect

    @Rule(GorgojoQuestion(question1='No',question2='No'))
    def GorgojoQuestion_rule3(self):
        question = get_object_or_404(Question, pk = 3)
        urlRedirect = "questionsRules:gorgojoInformation"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
        

    @Rule(GorgojoQuestion(question1='No',question2='Si'))
    def GorgojoQuestion_rule4(self):
        question = get_object_or_404(Question, pk = 3)
        urlRedirect = "questionsRules:gorgojoInformationAndGoodPractice"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
        
    @Rule(AS.gorgojoQuestionTwo << GorgojoQuestionTwo(question3=L('Si'), question4=L('No') | L('Si')))
    def seen_numberFive(self):
        question = get_object_or_404(Question, pk = 5)
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionTwo << GorgojoQuestionTwo(question3=L('No'), question4=L('No') | L('Si')))
    def seen_numberSix(self):
        question = get_object_or_404(Question, pk = 5)
        urlRedirect = "questionsRules:preventiveMeasures"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Recién planeo empezar mi cultivo'))
    def GorgojoQuestionThree_1(self):
        question = get_object_or_404(Question, pk =6)
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Acabo de sembrar'))
    def GorgojoQuestionThree_2(self):
        question = get_object_or_404(Question, pk =11)
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Mi cultivo de papa, ya esta más de la mitad'))
    def GorgojoQuestionThree_3(self):
        question = get_object_or_404(Question, pk =15)
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Estoy por cosechar mi cultivo'))
    def GorgojoQuestionThree_4(self):
        question = get_object_or_404(Question, pk =18)
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Acabo de cosechar mi cultivo'))
    def GorgojoQuestionThree_5(self):
        question = get_object_or_404(Question, pk =19)
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
        
    # @Rule(GorgojoQuestionFor(question6='no', question7='no' , question8 =question8, question9 = question9, question10= question10))
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('No'), question7=L('No') | L('Si'), question8=L('No') | L('Si'), question9=L('No') | L('Si'), question10=L('No') | L('Si')))
    def GorgojoQuestionFor_1(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:chemicals"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('No') , question8=L('No') | L('Si'), question9=L('No') | L('Si'), question10=L('No') | L('Si')))
    def GorgojoQuestionFor_2(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:ditches"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('No') , question9=L('No') | L('Si'), question10=L('No') | L('Si')))
    def GorgojoQuestionFor_3(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:plantOtherVegetables"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('No'), question10=L('No') | L('Si')))
    def GorgojoQuestionFor_4(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:plantPickUp"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('Si'), question10=L('No')))
    def GorgojoQuestionFor_5(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:traps"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('Si'), question10=L('Si')))
    def GorgojoQuestionFor_6(self):
        question = get_object_or_404(Question, pk = 5)
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('No'), question12=L('Si') | L('No'), question13=L('Si') | L('No'), question8=L('Si') | L('No'), question14=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_1(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:chemicals"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('No'), question13=L('Si') | L('No'), question8=L('Si') | L('No'), question14=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_2(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:ditches"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('No'), question8=L('Si') | L('No'), question14=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_3(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:culturalWork"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('No'), question14=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_4(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:plantOtherVegetables"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question14=L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_5(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question14=L('Si'), question10=L('No')))
    def GorgojoQuestionFive_6(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:traps"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question14=L('Si'), question10=L('Si')))
    def GorgojoQuestionFive_7(self):
        question = get_object_or_404(Question, pk = 1)
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect