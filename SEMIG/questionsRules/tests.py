from django.test import TestCase

from .models import Question

"""
_Test Question Model_
"""
class QuestionModelTests(TestCase):
    
    def test_get_wanted_question_or_questions(self):
        """Question: Get wanted question or questions of Model
        retrun False for value is distinct of expected question 
        """
        question = Question.objects.get(pk = 1)
        text_question = "¿Conoces al Gorgojo de Los Andes?" 
        self.assertEqual(question.question_text, text_question)