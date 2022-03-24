from django.test import TestCase
from django.utils import timezone

from experta import *
from .models import Question

"""
_Test Rules 
"""
class RulesForGorgojoTests(TestCase):
    
    def test_return_list_questions_for_value_one(self):
        """Question: Get wanted question or questions of Model
        retrun False for value is distinct of expected question 
        """
        """
        Return Equals list_question for Fact value Id
        """
        Question.objects.create(question_text="¿Conoces al Gorgojo de Los Andes?", pub_date= timezone.now())
        Question.objects.create(question_text="Es su primer cultivo", pub_date= timezone.now())
        
        class QuestionList(Fact):
            pass
        
        class integratedHandling(KnowledgeEngine):
            urlRedirect = "questionsRules:rules"
            listQuestion = Question.objects.filter(pk__in=[1])
            
            @Rule(AS.questionList << QuestionList(questionId=L(1) | L(2)))
            def QuestionList_One(self):
                self.listQuestion = Question.objects.filter(pk__in=[1,2])
                return self.listQuestion
            
        question_list = Question.objects.filter(pk__in =[1,2])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=1))
        enginer.run()
        latest_question_list = enginer.listQuestion
                   
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
