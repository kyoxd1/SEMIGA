from django.test import TestCase
from django.utils import timezone

from experta import *
from .models import Question

"""
_Test Rules 
"""
class RulesForGorgojoTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("Es su primer cultivo")
        Create_Question("¿Tuvo la plaga del Gorgojo de Los Andes anteriormente?")
        Create_Question("¿La plaga del Gorgojo de los Andes afecto su cultivo de papa?")
        Create_Question("¿En qué etapa se encuentra su cultivo?")
        Create_Question("¿Realizó desinfecciones químicas?")
        Create_Question("¿Realizó zanjas alrededor de la parcela para la siembra?")
        Create_Question("¿Sabe usted qué cultivos podría sembrar alrededor de la parcela?")
        Create_Question("¿Removió las plantas (K'ipas) de cosechas anteriores?")
        Create_Question("¿Sabe usted qué trampas podría poner alrededor del cultivo?")
        Create_Question("¿Realizo desinfecciones Químicas antes del Sembrado?")
        Create_Question("¿Realizó zanjas alrededor de la parcela?")
        Create_Question("¿Realizó Aporques alto alrededor de la parcela?")
        Create_Question("¿Sospecha qué en su cultivo tiene al Gorgojo de Los Andes?")
        Create_Question("¿Coloco trampas alrededor de la parcela?")
        Create_Question("¿Realizo la recolección de los Gorgojos Adultos?")
        Create_Question("¿Descubrió una gran cantidad de gorgojos en su parcela?")
        Create_Question("¿Sabe usted en qué seleccionar la papa, para un menor riesgo en el cultivo?")
        Create_Question("¿Removió el suelo de su cultivo?")
        Create_Question("¿Puso la papa en un almacén, o un lugar parecido?")
        Create_Question("¿Cree qué su cultivo de papa esta seguro en el almacén o otro lugar similar?")
        Create_Question("¿Conoce la utilidad del Hongo Blanco?")
    
    def test_return_list_questions_for_value(self):
        """Question: Get wanted question or questions of Model
        retrun False for value is distinct of expected question 
        """
        """
        Return Equals list_question for Fact QuestionList value Id
        """
        class QuestionList(Fact):
            pass
        
        class integratedHandling(KnowledgeEngine):
            urlRedirect = "questionsRules:rules"
            listQuestion = Question.objects.filter(pk__in=[1])
            
            @Rule(AS.questionList << QuestionList(questionId=L(1) | L(2)))
            def QuestionList_One(self):
                self.listQuestion = Question.objects.filter(pk__in=[1,2])
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
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 1
            return: question_list[ question1 , question 2]
        """
        question_list = Question.objects.filter(pk__in =[1,2])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=1))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 2
            return: question_list[ question1 , question 2]
        """
        enginer.reset()
        enginer.declare(QuestionList(questionId=2))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 3
            return: question_list[ question3 , question4]
        """
        question_list = Question.objects.filter(pk__in =[3,4])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=3))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=4))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
        question_list = Question.objects.filter(pk__in =[5])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=5))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        
        question_list = Question.objects.filter(pk__in =[3,4])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=3))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
        question_list = Question.objects.filter(pk__in =[6,7,8,9,10])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=6))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        self.assertEqual(latest_question_list[2].question_text, question_list[2].question_text)
        self.assertEqual(latest_question_list[3].question_text, question_list[3].question_text)
        self.assertEqual(latest_question_list[4].question_text, question_list[4].question_text)

    def test_return_list_questions_for_value_two(self):
        pass

def Create_Question(question_text):
    """Question cretion for unit test"""
    return Question.objects.create(question_text=question_text, pub_date= timezone.now())