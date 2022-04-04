from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from experta import *

from .knowledgeForGorgojo import *
from .models import Question


def Create_Question(question_text):
    """Question cretion for unit test"""
    return Question.objects.create(question_text=question_text, pub_date= timezone.now())



"""
    TEST ALL RULES FOR FACT
"""
class Gorgojo_Rules_For_Facts_Tests(TestCase):
    """
        CREATION QUESTION FOR RULES TEST
    """
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
    
    """
        Test For Fact = QuestionsList
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
    """
    def test_return_fact_questions_list_for_def_questionListOne(self):
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 1
            def:
                QuestionList_One
            return: question_list[ question1 , question 2]
            test: latest_question_list[question1, question2] == question_list[ question1, question2]
        """
        question_list = Question.objects.filter(pk__in =[1,2])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=1))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        self.assertEqual(latest_question_list[0].question_text, "¿Conoces al Gorgojo de Los Andes?")
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 2
            def:
                QuestionList_One
            return: question_list[ question1 , question 2]
            test: latest_question_list[question1, question2] == question_list[ question1, question2]
        """
        enginer.reset()
        enginer.declare(QuestionList(questionId=2))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
    def test_return_fact_questions_list_for_def_questionListTwo(self):
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 3
            def:
                QuestionList_Two
            return: question_list[ question3 , question4]
            test: latest_question_list[question3, question4] == question_list[ question3, question4]
        """
        question_list = Question.objects.filter(pk__in =[3,4])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=3))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 4
            def:
                QuestionList_Two
            return: question_list[ question3 , question4]
            test: latest_question_list[question3, question4] == question_list[ question3, question4]
        """
        enginer.reset()
        enginer.declare(QuestionList(questionId=4))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
        
    def test_return_fact_questions_list_for_def_questionListThree(self):
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 5
            def:
                QuestionList_Three
            return: question_list[ question5]
            test: latest_question_list[question5] == question_list[ question5]
        """
        question_list = Question.objects.filter(pk__in =[5])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=5))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertQuerysetEqual(latest_question_list, question_list)
           
                
    def test_return_fact_questions_list_for_def_questionListFor(self):
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 6
            def:
                QuestionList_For
            return: question_list[ question6 , question7, question8, question9, question10]
            test: latest_question_list[question6, question7, question8, question9, question10] == question_list[ question6, question7, question8, question9, question10]
        """
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
        
        
    def test_return_fact_questions_list_for_def_questionListFive(self):
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 11
            def:
                QuestionList_Five
            return: question_list[question8 , question10, question11, question12, question13, question14]
            test: latest_question_list[question8 , question10, question11, question12, question13, question14] == question_list[ question8 , question10, question11, question12, question13, question14]
        """
        question_list = Question.objects.filter(pk__in =[8, 10, 11, 12, 13, 14])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=11))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        self.assertEqual(latest_question_list[2].question_text, question_list[2].question_text)
        self.assertEqual(latest_question_list[3].question_text, question_list[3].question_text)
        self.assertEqual(latest_question_list[4].question_text, question_list[4].question_text)
        self.assertEqual(latest_question_list[5].question_text, question_list[5].question_text)
        
        
    def test_return_fact_questions_list_for_def_questionListSix(self):
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 15
            def:
                QuestionList_Six
            return: question_list[ question11 , question12, question13, question14, question15, question16, question17]
            test: latest_question_list[question11 , question12, question13, question14, question15, question16, question17] == question_list[question11 , question12, question13, question14, question15, question16, question17]
        """
        question_list = Question.objects.filter(pk__in =[11, 12, 13, 14, 15, 16, 17])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=15))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        self.assertEqual(latest_question_list[2].question_text, question_list[2].question_text)
        self.assertEqual(latest_question_list[3].question_text, question_list[3].question_text)
        self.assertEqual(latest_question_list[4].question_text, question_list[4].question_text)
        self.assertEqual(latest_question_list[5].question_text, question_list[5].question_text)
        self.assertEqual(latest_question_list[6].question_text, question_list[6].question_text)
        
        
    def test_return_fact_questions_list_for_def_questionListSeven(self):
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 18
            def:
                QuestionList_Seven
            return: question_list[ question16, question 17, question18]
            test: latest_question_list[question16, question 17, question18] == question_list[question16, question 17, question18]
        """
        question_list = Question.objects.filter(pk__in =[16, 17, 18])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=18))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        self.assertEqual(latest_question_list[2].question_text, question_list[2].question_text)
        
        
    def test_return_fact_questions_list_for_def_questionListEigth(self):
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 19
            def:
                QuestionList_Eigth
            return: question_list[question19 , question20, question21, question22]
            test: latest_question_list[question19 , question20, question21, question22] == question_list[question19 , question20, question21, question22]
        """
        question_list = Question.objects.filter(pk__in =[19, 20, 21, 22])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=19))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        self.assertEqual(latest_question_list[2].question_text, question_list[2].question_text)
        self.assertEqual(latest_question_list[3].question_text, question_list[3].question_text)

    """
        Test For Fact = GorgojoQuestion
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
    """
    def test_return_fact_gorgojoQuestion_for_def_gorgojoQuestionOne(self):
        """
            Rule Test of:
                Fac: GorgojoQuestion(question1 = value1, question2 = value2)
                Value1: Si
                Value2: Si
            def:
                GorgojoQuestion_1
            return: question_list[ question3], urlRedirect='questionsRules:goodPractices'
        """
        question_list = Question.objects.filter(pk__in =[3])
        url = "questionsRules:goodPractices"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestion(question1='Si', question2='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_gorgojoQuestion_for_def_gorgojoQuestionTwo(self):
        """
            Rule Test of:
                Fac: GorgojoQuestion(question1 = value1, question2 = value2)
                Value1: Si
                Value2: No
            def:
                GorgojoQuestion_2
            return: question_list[ question3], urlRedirect='questionsRules:rules'
        """
        question_list = Question.objects.filter(pk__in =[3])
        url = "questionsRules:rules"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestion(question1='Si', question2='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_gorgojoQuestion_for_def_gorgojoQuestionThree(self):
        """
            Rule Test of:
                Fac: GorgojoQuestion(question1 = value1, question2 = value2)
                Value1: No
                Value2: Si
            def:
                GorgojoQuestion_3
            return: question_list[ question3], urlRedirect='questionsRules:gorgojoInformationAndGoodPractice'
        """
        question_list = Question.objects.filter(pk__in =[3])
        url = "questionsRules:gorgojoInformationAndGoodPractice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestion(question1='No', question2='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_gorgojoQuestion_for_def_gorgojoQuestionFor(self):
        """
            Rule Test of:
                Fac: GorgojoQuestion(question1 = value1, question2 = value2)
                Value1: No
                Value2: No
            def:
                GorgojoQuestion_4
            return: question_list[ question3], urlRedirect='questionsRules:gorgojoInformation'
        """
        question_list = Question.objects.filter(pk__in =[3])
        url = "questionsRules:gorgojoInformation"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestion(question1='No', question2='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    """
        Test For Fact = GorgojoQuestionTwo
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
    """
    def test_return_fact_gorgojoQuestionTwo_for_def_gorgojoQuestionTwo1(self):    
        """
            Rule Test of:
                Fac: GorgojoQuestionTwo(question3 = value1, question4 = value2)
                Value1: Si
                Value2: Si
            def:
                GorgojoQuestionTwo_1
            return: question_list[ question5], urlRedirect='questionsRules:preventiveMeasures'
        """
        question_list = Question.objects.filter(pk__in =[5])
        url = "questionsRules:preventiveMeasures"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionTwo(question3='Si', question4='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestionTwo(question3 = value1, question4 = value2)
                Value1: No
                Value2: Si
            def:
                GorgojoQuestionTwo_1
            return: question_list[ question5], urlRedirect='questionsRules:preventiveMeasures'
        """
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionTwo(question3='No', question4='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_gorgojoQuestionTwo_for_def_gorgojoQuestionTwo2(self):    
        """
            Rule Test of:
                Fac: GorgojoQuestionTwo(question3 = value1, question4 = value2)
                Value1: Si
                Value2: No
            def:
                GorgojoQuestionTwo_2
            return: question_list[ question5], urlRedirect='questionsRules:rules'
        """
        question_list = Question.objects.filter(pk__in =[5])
        url = "questionsRules:rules"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionTwo(question3='Si', question4='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestionTwo(question3 = value1, question4 = value2)
                Value1: No
                Value2: No
            def:
                GorgojoQuestionTwo_2
            return: question_list[ question5], urlRedirect='questionsRules:rules'
        """
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionTwo(question3='No', question4='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
    
    """
        Test For Fact = GorgojoQuestionThree
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
    """
    def test_return_fact_GorgojoQuestionThree_for_GorgojoQuestionThree1(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
                Def: GorgojoQuestionThree_1
                Value: 'Recién planeo empezar mi cultivo'
            return: question_list[ question6], urlRedirect='questionsRules:rules'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:rules"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionThree(resp='Recién planeo empezar mi cultivo'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
    def test_return_fact_GorgojoQuestionThree_for_GorgojoQuestionThree2(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
                Def: GorgojoQuestionThree_2
                Value: 'Acabo de sembrar'
            return: question_list[ question11], urlRedirect='questionsRules:rules'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:rules"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionThree(resp='Acabo de sembrar'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionThree_for_GorgojoQuestionThree3(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
                Def: GorgojoQuestionThree_3
                Value: 'Mi cultivo de papa, ya esta más de la mitad'
            return: question_list[ question15], urlRedirect='questionsRules:rules'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:rules"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionThree(resp='Mi cultivo de papa, ya esta más de la mitad'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionThree_for_GorgojoQuestionThree4(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
                Def: GorgojoQuestionThree_4
                Value: 'Estoy por cosechar mi cultivo'
            return: question_list[ question18], urlRedirect='questionsRules:rules'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:rules"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionThree(resp='Estoy por cosechar mi cultivo'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionThree_for_GorgojoQuestionThree5(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
                Def: GorgojoQuestionThree_5
                Value: 'Acabo de cosechar mi cultivo'
            return: question_list[ question19], urlRedirect='questionsRules:rules'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:rules"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionThree(resp='Acabo de cosechar mi cultivo'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
    """
    Test For Fact = GorgojoQuestionFor
        
    Verification return to rules if the response is equals to expected

    Returns:
        QuerySet: returned queryset with the question five.
        String : returned to string per url
    """
    def test_return_fact_GorgojoQuestionFor_for_def_GorgojoQuestionFor1(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: No
                Value2: No
                Value3: No
                Value4: No
                Value5: No
                Rule: def GorgojoQuestionFor_1
            return: question_list[question6], urlRedirect='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='No', question7='No', question8='No', question9='No', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: No
                Value2: No
                Value3: No
                Value4: No
                Value5: Si
                Rule: def GorgojoQuestionFor_1
            return: question_list[question6], urlRedirect='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='No', question7='No', question8='No', question9='No', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: No
                Value2: Si
                Value3: No
                Value4: No
                Value5: Si
                Rule: def GorgojoQuestionFor_1
            return: question_list[question6], urlRedirect='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='No', question7='Si', question8='No', question9='No', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionFor_for_def_GorgojoQuestionFor2(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: No
                Value3: No
                Value4: No
                Value5: Si
                Rule: def GorgojoQuestionFor_2
            return: question_list[question6], urlRedirect='questionsRules:ditches'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:ditches"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='No', question8='No', question9='No', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: No
                Value2: No
                Value3: Si
                Value4: Si
                Value5: Si
                Rule: def GorgojoQuestionFor_2
            return: latest_question_list[question6], urlRedirect='questionsRules:chemicals'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:chemicals' != url='questionsRules:ditches'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:ditches"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='No', question7='No', question8='Si', question9='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: No
                Value3: Si
                Value4: Si
                Value5: Si
                Rule: def GorgojoQuestionFor_2
            return: latest_question_list[question6], urlRedirect='questionsRules:ditches'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:ditches' == url='questionsRules:ditches'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:ditches"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='No', question8='Si', question9='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionFor_for_def_GorgojoQuestionFor3(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: Si
                Value5: Si
                Rule: def GorgojoQuestionFor_3
            return: latest_question_list[question6], urlRedirect='questionsRules:plantOtherVegetables'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:plantOtherVegetables' == url='questionsRules:plantOtherVegetables'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:plantOtherVegetables"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='Si', question8='No', question9='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: No
                Value2: Si
                Value3: No
                Value4: Si
                Value5: Si
                Rule: def GorgojoQuestionFor_3
            return: latest_question_list[question6], urlRedirect='questionsRules:chemicals'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:chemicals' != url='questionsRules:plantOtherVegetables'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:plantOtherVegetables"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='No', question7='Si', question8='No', question9='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: No
                Value3: No
                Value4: Si
                Value5: Si
                Rule: def GorgojoQuestionFor_3
            return: latest_question_list[question6], urlRedirect='questionsRules:ditches'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:ditches' != url='questionsRules:plantOtherVegetables'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:plantOtherVegetables"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='No', question8='No', question9='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionFor_for_def_GorgojoQuestionFor4(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: No
                Value5: No
                Rule: def GorgojoQuestionFor_4
            return: latest_question_list[question6], urlRedirect='questionsRules:plantPickUp'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:plantPickUp' == url='questionsRules:plantPickUp'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:plantPickUp"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='Si', question8='Si', question9='No', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: No
                Value5: Si
                Rule: def GorgojoQuestionFor_4
            return: latest_question_list[question6], urlRedirect='questionsRules:plantPickUp'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:plantPickUp' == url='questionsRules:plantPickUp'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:plantPickUp"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='Si', question8='Si', question9='No', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: No
                Value2: Si
                Value3: Si
                Value4: No
                Value5: Si
                Rule: def GorgojoQuestionFor_4
            return: latest_question_list[question6], urlRedirect='questionsRules:chemical'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:chemical' != url='questionsRules:plantPickUp'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:plantPickUp"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='No', question7='Si', question8='Si', question9='No', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionFor_for_def_GorgojoQuestionFor5(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: No
                Rule: def GorgojoQuestionFor_5
            return: latest_question_list[question6], urlRedirect='questionsRules:traps'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:traps' == url='questionsRules:traps'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:traps"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='Si', question8='Si', question9='Si', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: Si
                Value5: No
                Rule: def GorgojoQuestionFor_5
            return: latest_question_list[question6], urlRedirect='questionsRules:plantOtherVegetables'
            test: latest_question_list[question6] == question_list[question6]
            test: urlRedirect='questionsRules:plantOtherVegetables' != url='questionsRules:traps'
        """
        question_list = Question.objects.filter(pk__in =[6])
        url = "questionsRules:traps"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='Si', question8='No', question9='Si', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionFor_for_def_GorgojoQuestionFor6(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFor(question6=value1, question7=value2, question8=value3, question9=value4, question10=value5)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Rule: def GorgojoQuestionFor_6
            return: latest_question_list[question11], urlRedirect='questionsRules:continueStageChoice'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:continueStageChoice' == url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFor(question6='Si', question7='Si', question8='Si', question9='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
    
    
    """
    Test For Fact = GorgojoQuestionTwo
        
    Verification return to rules if the response is equals to expected

    Returns:
        QuerySet: returned queryset with the question five.
        String : returned to string per url
    """
    def test_return_fact_GorgojoQuestionFive_for_def_GorgojoQuestionFive1(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: No
                Value2: No
                Value3: No
                Value4: No
                Value5: No
                Value6: No
                Rule: def GorgojoQuestionFive_1
            return: latest_question_list[question11], urlRedirect='questionsRules:chemicals'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:chemicals' == url='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='No', question12='No', question13='No', question8='No', question14='No', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: No
                Value2: Si
                Value3: No
                Value4: Si
                Value5: No
                Value6: Si
                Rule: def GorgojoQuestionFive_1
            return: latest_question_list[question11], urlRedirect='questionsRules:chemicals'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:chemicals' == url='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='No', question12='Si', question13='No', question8='Si', question14='No', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: No
                Value2: No
                Value3: Si
                Value4: No
                Value5: Si
                Value6: No
                Rule: def GorgojoQuestionFive_1
            return: latest_question_list[question11], urlRedirect='questionsRules:chemicals'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:chemicals' == url='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='No', question12='No', question13='Si', question8='No', question14='Si', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionFive_for_def_GorgojoQuestionFive2(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: No
                Value3: No
                Value4: No
                Value5: No
                Value6: No
                Rule: def GorgojoQuestionFive_2
            return: latest_question_list[question11], urlRedirect='questionsRules:ditches'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:ditches' == url='questionsRules:ditches'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:ditches"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='No', question13='No', question8='No', question14='No', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: No
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: Si
                Rule: def GorgojoQuestionFive_2
            return: latest_question_list[question11], urlRedirect='questionsRules:ditches'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:ditches' == url='questionsRules:ditches'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:ditches"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='No', question13='Si', question8='Si', question14='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionFive_for_def_GorgojoQuestionFive3(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: No
                Value5: No
                Value6: No
                Rule: def GorgojoQuestionFive_3
            return: latest_question_list[question11], urlRedirect='questionsRules:culturalWork'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:culturalWork' == url='questionsRules:culturalWork'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:culturalWork"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='No', question8='No', question14='No', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: Si
                Value5: Si
                Value6: Si
                Rule: def GorgojoQuestionFive_3
            return: latest_question_list[question11], urlRedirect='questionsRules:culturalWork'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:culturalWork' == url='questionsRules:culturalWork'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:culturalWork"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='No', question8='Si', question14='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionFive_for_def_GorgojoQuestionFive4(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: No
                Value5: No
                Value6: No
                Rule: def GorgojoQuestionFive_4
            return: latest_question_list[question11], urlRedirect='questionsRules:plantOtherVegetables'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:plantOtherVegetables' == url='questionsRules:plantOtherVegetables'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:plantOtherVegetables"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='Si', question8='No', question14='No', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: No
                Value5: Si
                Value6: Si
                Rule: def GorgojoQuestionFive_4
            return: latest_question_list[question11], urlRedirect='questionsRules:plantOtherVegetables'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:plantOtherVegetables' == url='questionsRules:plantOtherVegetables'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:plantOtherVegetables"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='Si', question8='No', question14='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
    
    def test_return_fact_GorgojoQuestionFive_for_def_GorgojoQuestionFive5(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: No
                Value6: No
                Rule: def GorgojoQuestionFive_5
            return: latest_question_list[question11], urlRedirect='questionsRules:gorgojoMeasures'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:gorgojoMeasures' == url='questionsRules:gorgojoMeasures'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:gorgojoMeasures"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='Si', question8='Si', question14='No', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: No
                Value6: Si
                Rule: def GorgojoQuestionFive_5
            return: latest_question_list[question11], urlRedirect='questionsRules:gorgojoMeasures'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:gorgojoMeasures' == url='questionsRules:gorgojoMeasures'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:gorgojoMeasures"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='Si', question8='Si', question14='No', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: Si
                Value5: No
                Value6: No
                Rule: def GorgojoQuestionFive_5
            return: latest_question_list[question11], urlRedirect='questionsRules:culturalWork'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:culturalWork' != url='questionsRules:gorgojoMeasures'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:gorgojoMeasures"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='No', question8='Si', question14='No', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
        
    
    def test_return_fact_GorgojoQuestionFive_for_def_GorgojoQuestionFive6(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: No
                Rule: def GorgojoQuestionFive_6
            return: latest_question_list[question11], urlRedirect='questionsRules:traps'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:traps' == url='questionsRules:traps'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:traps"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='Si', question8='Si', question14='Si', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: No
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: No
                Rule: def GorgojoQuestionFive_6
            return: latest_question_list[question11], urlRedirect='questionsRules:ditches'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:ditches' != url='questionsRules:traps'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:traps"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='No', question13='Si', question8='Si', question14='Si', question10='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
        
    
    def test_return_fact_GorgojoQuestionFive_for_def_GorgojoQuestionFive7(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: Si
                Rule: def GorgojoQuestionFive_7
            return: latest_question_list[question15], urlRedirect='questionsRules:continueStageChoice'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:continueStageChoice' == url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='Si', question13='Si', question8='Si', question14='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionFive(question11=value1, question12=value2, question13=value3, question8=value4, question14=value5, question10=value6)
                Value1: Si
                Value2: No
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: Si
                Rule: def GorgojoQuestionFive_7
            return: latest_question_list[question11], urlRedirect='questionsRules:ditches'
            test: latest_question_list[question11] == question_list[question11]
            test: urlRedirect='questionsRules:ditches' != url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[11])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionFive(question11='Si', question12='No', question13='Si', question8='Si', question14='Si', question10='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
    
    
    """
    Test For Fact = GorgojoQuestionSix
        
    Verification return to rules if the response is equals to expected

    Returns:
        QuerySet: returned queryset with the question five.
        String : returned to string per url
    """
    def test_return_fact_GorgojoQuestionSix_for_def_GorgojoQuestionSix1(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: No
                Value2: No
                Value3: No
                Value4: No
                Value5: No
                Value6: No
                Value7: No
                Rule: def GorgojoQuestionSix_1
            return: latest_question_list[question15], urlRedirect='questionsRules:chemicals'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:chemicals' == url='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='No', question12='No', question13='No', question14='No', question15='No', question16='No', question17='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: No
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: Si
                Value7: Si
                Rule: def GorgojoQuestionSix_1
            return: latest_question_list[question15], urlRedirect='questionsRules:chemicals'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:chemicals' == url='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='No', question12='Si', question13='Si', question14='Si', question15='Si', question16='Si', question17='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: No
                Value2: Si
                Value3: No
                Value4: Si
                Value5: No
                Value6: Si
                Value7: No
                Rule: def GorgojoQuestionSix_1
            return: latest_question_list[question15], urlRedirect='questionsRules:chemicals'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:chemicals' == url='questionsRules:chemicals'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:chemicals"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='No', question12='Si', question13='No', question14='Si', question15='No', question16='Si', question17='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
    
    def test_return_fact_GorgojoQuestionSix_for_def_GorgojoQuestionSix2(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: No
                Value3: No
                Value4: No
                Value5: No
                Value6: No
                Value7: No
                Rule: def GorgojoQuestionSix_2
            return: latest_question_list[question15], urlRedirect='questionsRules:ditches'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:ditches' == url='questionsRules:ditches'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:ditches"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='No', question13='No', question14='No', question15='No', question16='No', question17='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: No
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: Si
                Value7: Si
                Rule: def GorgojoQuestionSix_2
            return: latest_question_list[question15], urlRedirect='questionsRules:ditches'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:ditches' == url='questionsRules:ditches'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:ditches"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='No', question13='Si', question14='Si', question15='Si', question16='Si', question17='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionSix_for_def_GorgojoQuestionSix3(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: No
                Value5: No
                Value6: No
                Value7: No
                Rule: def GorgojoQuestionSix_3
            return: latest_question_list[question15], urlRedirect='questionsRules:culturalWork'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:culturalWork' == url='questionsRules:culturalWork'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:culturalWork"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='No', question14='No', question15='No', question16='No', question17='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: Si
                Value5: Si
                Value6: Si
                Value7: Si
                Rule: def GorgojoQuestionSix_3
            return: latest_question_list[question15], urlRedirect='questionsRules:culturalWork'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:culturalWork' == url='questionsRules:culturalWork'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:culturalWork"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='No', question14='Si', question15='Si', question16='Si', question17='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
    
    def test_return_fact_GorgojoQuestionSix_for_def_GorgojoQuestionSix4(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: No
                Value5: No
                Value6: No
                Value7: No
                Rule: def GorgojoQuestionSix_4
            return: latest_question_list[question15], urlRedirect='questionsRules:gorgojoMeasures'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:gorgojoMeasures' == url='questionsRules:gorgojoMeasures'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:gorgojoMeasures"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='Si', question14='No', question15='No', question16='No', question17='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: No
                Value5: Si
                Value6: Si
                Value7: Si
                Rule: def GorgojoQuestionSix_4
            return: latest_question_list[question15], urlRedirect='questionsRules:gorgojoMeasures'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:gorgojoMeasures' == url='questionsRules:gorgojoMeasures'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:gorgojoMeasures"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='Si', question14='No', question15='Si', question16='Si', question17='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionSix_for_def_GorgojoQuestionSix5(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: No
                Value6: No
                Value7: No
                Rule: def GorgojoQuestionSix_5
            return: latest_question_list[question15], urlRedirect='questionsRules:traps'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:traps' == url='questionsRules:traps'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:traps"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='Si', question14='Si', question15='No', question16='No', question17='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: No
                Value6: Si
                Value7: Si
                Rule: def GorgojoQuestionSix_5
            return: latest_question_list[question15], urlRedirect='questionsRules:traps'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:traps' == url='questionsRules:traps'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:traps"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='Si', question14='Si', question15='No', question16='Si', question17='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionSix_for_def_GorgojoQuestionSix6(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: No
                Value7: No
                Rule: def GorgojoQuestionSix_6
            return: latest_question_list[question15], urlRedirect='questionsRules:gatherGorgojo'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:gatherGorgojo' == url='questionsRules:gatherGorgojo'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:gatherGorgojo"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='Si', question14='Si', question15='Si', question16='No', question17='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: No
                Value7: Si
                Rule: def GorgojoQuestionSix_6
            return: latest_question_list[question15], urlRedirect='questionsRules:gatherGorgojo'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:gatherGorgojo' == url='questionsRules:gatherGorgojo'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:gatherGorgojo"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='Si', question14='Si', question15='Si', question16='No', question17='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionSix_for_def_GorgojoQuestionSix7(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: Si
                Value7: No
                Rule: def GorgojoQuestionSix_7
            return: latest_question_list[question15], urlRedirect='questionsRules:countherTheGorgojo'
            test: latest_question_list[question15] == question_list[question15]
            test: urlRedirect='questionsRules:countherTheGorgojo' == url='questionsRules:countherTheGorgojo'
        """
        question_list = Question.objects.filter(pk__in =[15])
        url = "questionsRules:countherTheGorgojo"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='Si', question14='Si', question15='Si', question16='Si', question17='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionSix_for_def_GorgojoQuestionSix8(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value, question12=value, question13=value, question14=value, question15=value, question16=value, question17=value)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: Si
                Value7: Si
                Rule: def GorgojoQuestionSix_8
            return: latest_question_list[question18], urlRedirect='questionsRules:continueStageChoice'
            test: latest_question_list[question18] == question_list[question18]
            test: urlRedirect='questionsRules:continueStageChoice' == url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='Si', question12='Si', question13='Si', question14='Si', question15='Si', question16='Si', question17='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSix(question11=value1, question12=value2, question13=value3, question14=value4, question15=value5, question16=value6, question17=value7)
                Value1: No
                Value2: Si
                Value3: Si
                Value4: Si
                Value5: Si
                Value6: Si
                Value7: Si
                Rule: def GorgojoQuestionSix_8
            return: latest_question_list[question15], urlRedirect='questionsRules:chemical'
            test: latest_question_list[question15] != question_list[question18]
            test: urlRedirect='questionsRules:chemical' != url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSix(question11='No', question12='Si', question13='Si', question14='Si', question15='Si', question16='Si', question17='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertNotEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertNotEqual(urlRedirect, url)
    
    
    """
    Test For Fact = GorgojoQuestionSeven
        
    Verification return to rules if the response is equals to expected

    Returns:
        QuerySet: returned queryset with the question five.
        String : returned to string per url
    """
    def test_return_fact_GorgojoQuestionSeven_for_def_GorgojoQuestionSeven1(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSeven(question16=value1, question17=value2, question18= value3)
                Value1: No
                Value2: No
                Value3: No
                Rule: def GorgojoQuestionSeven_1
            return: latest_question_list[question18], urlRedirect='questionsRules:gatherGorgojo'
            test: latest_question_list[question18] == question_list[question18]
            test: urlRedirect='questionsRules:gatherGorgojo' == url='questionsRules:gatherGorgojo'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:gatherGorgojo"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSeven(question16='No', question17='No', question18= 'No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSeven(question16=value1, question17=value2, question18= value3)
                Value1: No
                Value2: Si
                Value3: Si
                Rule: def GorgojoQuestionSeven_1
            return: latest_question_list[question18], urlRedirect='questionsRules:gatherGorgojo'
            test: latest_question_list[question18] == question_list[question18]
            test: urlRedirect='questionsRules:gatherGorgojo' == url='questionsRules:gatherGorgojo'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:gatherGorgojo"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSeven(question16='No', question17='Si', question18= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionSeven_for_def_GorgojoQuestionSeven2(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSeven(question16=value1, question17=value2, question18= value3)
                Value1: Si
                Value2: No
                Value3: No
                Rule: def GorgojoQuestionSeven_2
            return: latest_question_list[question18], urlRedirect='questionsRules:countherTheGorgojo'
            test: latest_question_list[question18] == question_list[question18]
            test: urlRedirect='questionsRules:countherTheGorgojo' == url='questionsRules:countherTheGorgojo'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:countherTheGorgojo"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSeven(question16='Si', question17='No', question18= 'No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSeven(question16=value1, question17=value2, question18= value3)
                Value1: Si
                Value2: No
                Value3: Si
                Rule: def GorgojoQuestionSeven_2
            return: latest_question_list[question18], urlRedirect='questionsRules:countherTheGorgojo'
            test: latest_question_list[question18] == question_list[question18]
            test: urlRedirect='questionsRules:countherTheGorgojo' == url='questionsRules:countherTheGorgojo'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:countherTheGorgojo"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSeven(question16='Si', question17='No', question18= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionSeven_for_def_GorgojoQuestionSeven3(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSeven(question16=value1, question17=value2, question18= value3)
                Value1: Si
                Value2: Si
                Value3: No
                Rule: def GorgojoQuestionSeven_3
            return: latest_question_list[question18], urlRedirect='questionsRules:potatoSelection'
            test: latest_question_list[question18] == question_list[question18]
            test: urlRedirect='questionsRules:potatoSelection' == url='questionsRules:potatoSelection'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:potatoSelection"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSeven(question16='Si', question17='Si', question18= 'No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionSeven_for_def_GorgojoQuestionSeven4(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionSeven(question16=value1, question17=value2, question18= value3)
                Value1: Si
                Value2: Si
                Value3: Si
                Rule: def GorgojoQuestionSeven_4
            return: latest_question_list[question19], urlRedirect='questionsRules:continueStageChoice'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:continueStageChoice' == url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSeven(question16='Si', question17='Si', question18= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionSeven(question16=value1, question17=value2, question18= value3)
                Value1: Si
                Value2: Si
                Value3: Si
                Rule: def GorgojoQuestionSeven_4
            return: latest_question_list[question19], urlRedirect='questionsRules:continueStageChoice'
            test: latest_question_list[question19] != question_list[question18]
            test: urlRedirect='questionsRules:continueStageChoice' == url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[18])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionSeven(question16='Si', question17='Si', question18= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertNotEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
    
    
    """
    Test For Fact = GorgojoQuestionEigth
        
    Verification return to rules if the response is equals to expected

    Returns:
        QuerySet: returned queryset with the question five.
        String : returned to string per url
    """
    def test_return_fact_GorgojoQuestionEight_for_def_GorgojoQuestionEight1(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: No
                Value2: No
                Value3: No
                Value4: No
                Rule: def GorgojoQuestionEight_1
            return: latest_question_list[question19], urlRedirect='questionsRules:soilRemoval'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:soilRemoval' == url='questionsRules:soilRemoval'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:soilRemoval"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='No', question20='No', question21= 'No', question22= 'No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: No
                Value2: Si
                Value3: Si
                Value4: Si
                Rule: def GorgojoQuestionEight_1
            return: latest_question_list[question19], urlRedirect='questionsRules:soilRemoval'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:soilRemoval' == url='questionsRules:soilRemoval'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:soilRemoval"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='No', question20='Si', question21= 'Si', question22= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        
    def test_return_fact_GorgojoQuestionEight_for_def_GorgojoQuestionEight2(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: Si
                Value2: No
                Value3: No
                Value4: No
                Rule: def GorgojoQuestionEight_2
            return: latest_question_list[question19], urlRedirect='questionsRules:warehousePreparation'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:warehousePreparation' == url='questionsRules:warehousePreparation'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:warehousePreparation"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='Si', question20='No', question21= 'No', question22= 'No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: Si
                Value2: No
                Value3: Si
                Value4: Si
                Rule: def GorgojoQuestionEight_2
            return: latest_question_list[question19], urlRedirect='questionsRules:warehousePreparation'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:warehousePreparation' == url='questionsRules:warehousePreparation'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:warehousePreparation"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='Si', question20='No', question21= 'Si', question22= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
    def test_return_fact_GorgojoQuestionEight_for_def_GorgojoQuestionEight3(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: No
                Rule: def GorgojoQuestionEight_3
            return: latest_question_list[question19], urlRedirect='questionsRules:dangerIntoWarehouse'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:dangerIntoWarehouse' == url='questionsRules:dangerIntoWarehouse'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:dangerIntoWarehouse"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='Si', question20='Si', question21= 'No', question22= 'No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: Si
                Value2: Si
                Value3: No
                Value4: Si
                Rule: def GorgojoQuestionEight_3
            return: latest_question_list[question19], urlRedirect='questionsRules:dangerIntoWarehouse'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:dangerIntoWarehouse' == url='questionsRules:dangerIntoWarehouse'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:dangerIntoWarehouse"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='Si', question20='Si', question21= 'No', question22= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
    def test_return_fact_GorgojoQuestionEight_for_def_GorgojoQuestionEight4(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: No
                Rule: def GorgojoQuestionEight_4
            return: latest_question_list[question19], urlRedirect='questionsRules:whiteFungus'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:whiteFungus' == url='questionsRules:whiteFungus'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:whiteFungus"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='Si', question20='Si', question21= 'Si', question22= 'No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: Si
                Value2: No
                Value3: Si
                Value4: No
                Rule: def GorgojoQuestionEight_4
            return: latest_question_list[question19], urlRedirect='questionsRules:warehousePreparation'
            test: latest_question_list[question19] == question_list[question19]
            test: urlRedirect='questionsRules:warehousePreparation' != url='questionsRules:whiteFungus'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:whiteFungus"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='Si', question20='No', question21= 'Si', question22= 'No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertNotEqual(urlRedirect, url)
        
    
    def test_return_fact_GorgojoQuestionEight_for_def_GorgojoQuestionEight5(self):
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Rule: def GorgojoQuestionEight_5
            return: latest_question_list[question1], urlRedirect='questionsRules:continueStageChoice'
            test: latest_question_list[question1] == question_list[question1]
            test: urlRedirect='questionsRules:continueStageChoice' == url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[1])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='Si', question20='Si', question21= 'Si', question22= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertQuerysetEqual(latest_question_list, question_list)
        self.assertEqual(urlRedirect, url)
        
        """
            Rule Test of:
                Fac: GorgojoQuestionEigth(question19=value1, question20=value2, question21= value3, question22=value4)
                Value1: Si
                Value2: Si
                Value3: Si
                Value4: Si
                Rule: def GorgojoQuestionEight_5
            return: latest_question_list[question1], urlRedirect='questionsRules:continueStageChoice'
            test: latest_question_list[question1] != question_list[question19]
            test: urlRedirect='questionsRules:continueStageChoice' == url='questionsRules:continueStageChoice'
        """
        question_list = Question.objects.filter(pk__in =[19])
        url = "questionsRules:continueStageChoice"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionEight(question19='Si', question20='Si', question21= 'Si', question22= 'Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        self.assertNotEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)

class QuestionsRules_RulesViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_rulesView_for_questionid_1(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 1

        questions = [Question1, Question2]
        question3 = Question3

        View return: latest_questions_list[question1, question2]

        Test: if status code to View Rules is equal '200'
        Test: if latest_questions_list is equals questions
        Test: if question3 isn't contains in response to View Rules
        """
        question3 = Question.objects.get(pk = 3)
        questions = Question.objects.filter(pk__in =[1,2]).order_by("id")
        url = reverse("questionsRules:rules", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question3.question_text)
        
    def test_rulesView_for_questionid_2(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 2

        questions = [Question1, Question2]
        question3 = Question3

        View return: latest_questions_list[question1, question2]

        Test: if status code to View Rules is equal '200'
        Test: if latest_questions_list is equals questions
        Test: if question3 isn't contains in response to View Rules
        """
        question3 = Question.objects.get(pk = 3)
        questions = Question.objects.filter(pk__in =[1,2]).order_by("id")
        url = reverse("questionsRules:rules", args=(2,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question3.question_text)
        
    def test_rulesView_for_questionid_3(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 3

        questions = [Question3, Question4]
        question5 = Question5

        View retunr: latest_questions_list[question3, question4]

        Test: if status code to View Rules is equal '200'
        Test: if of RulesView response.latest_question_list[question3,question4] is equals questions
        Test: if question5 isn't contains in response to View Rules
        """
        question5 = Question.objects.get(pk = 5)
        questions = Question.objects.filter(pk__in =[3,4]).order_by("id")
        url = reverse("questionsRules:rules", args=(3,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question5.question_text)
        
    def test_rulesView_for_questionid_4(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 4

        questions = [Question3, Question4]
        question5 = Question5

        View retunr: latest_questions_list[question3, question4]

        Test: if status code to View Rules is equal '200'
        Test: if of RulesView response.latest_question_list[question3,question4] is equals questions
        Test: if question5 isn't contains in response to View Rules
        """
        question5 = Question.objects.get(pk = 5)
        questions = Question.objects.filter(pk__in =[3,4]).order_by("id")
        url = reverse("questionsRules:rules", args=(4,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question5.question_text)
        
        
    def test_rulesView_for_questionid_5(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 5

        question4 = Question4
        questions = [Question5]
        question6 = Question6

        View return: latest_questions_list[question5]

        Test: if status code to View Rules is equal '200'
        Test: if latest_questions_list is equals questions
        Test: if question4 isn't contains in response to View Rules
        Test: if question6 isn't contains in response to View Rules
        """
        question4 = Question.objects.get(pk = 4)
        question6 = Question.objects.get(pk = 6)
        questions = Question.objects.filter(pk__in =[5]).order_by("id")
        url = reverse("questionsRules:rules", args=(5,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question4.question_text)
        self.assertNotContains(response, question6.question_text)
        
        
    def test_rulesView_for_questionid_6(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 6

        question5 = Question8
        questions = [Question6, Question7, Question8, Quesiton9, Question10]
        question7 = Question7

        View return: latest_questions_list[question6, question7, question8, quesiton9, question10]

        Test: if status code to View Rules is equal '200'
        Test: if latest_questions_list is equals questions
        Test: if question5 isn't contains in response to View Rules
        Test: if question7 is contains in response to View Rules
        """
        question5 = Question.objects.get(pk = 5)
        question7 = Question.objects.get(pk = 7)
        questions = Question.objects.filter(pk__in =[6,7,8,9,10]).order_by("id")
        url = reverse("questionsRules:rules", args=(6,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question5.question_text)
        self.assertContains(response, question7.question_text)
        
        
    def test_rulesView_for_questionid_7(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 7

        question6 = Question6
        question7 = Question7
        question8 = Question8

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question6 isn't contains in response to View Rules
        Test: if question7 isn't contains in response to View Rules
        Test: if question8 isn't contains in response to View Rules
        """
        question6 = Question.objects.get(pk = 6)
        question7 = Question.objects.get(pk = 7)
        question8 = Question.objects.get(pk = 8)
        url = reverse("questionsRules:rules", args=(7,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question6.question_text)
        self.assertNotContains(response, question7.question_text)
        self.assertNotContains(response, question8.question_text)
        
        
    def test_rulesView_for_questionid_8(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 8

        question7 = Question7
        question8 = Question8
        question9 = Question9

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question7 isn't contains in response to View Rules
        Test: if question8 isn't contains in response to View Rules
        Test: if question9 isn't contains in response to View Rules
        """
        question7 = Question.objects.get(pk = 7)
        question8 = Question.objects.get(pk = 8)
        question9 = Question.objects.get(pk = 9)
        url = reverse("questionsRules:rules", args=(8,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question7.question_text)
        self.assertNotContains(response, question8.question_text)
        self.assertNotContains(response, question9.question_text)
        
        
    def test_rulesView_for_questionid_9(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 9

        question8 = Question8
        question9 = Question9
        question10 = Question10

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question8 isn't contains in response to View Rules
        Test: if question9 isn't contains in response to View Rules
        Test: if question10 isn't contains in response to View Rules
        """
        question8 = Question.objects.get(pk = 8)
        question9 = Question.objects.get(pk = 9)
        question10 = Question.objects.get(pk = 10)
        url = reverse("questionsRules:rules", args=(9,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question8.question_text)
        self.assertNotContains(response, question9.question_text)
        self.assertNotContains(response, question10.question_text)
        
        
    def test_rulesView_for_questionid_10(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 10

        question9 = Question9
        question10 = Question10
        question11 = Question11

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question9 isn't contains in response to View Rules
        Test: if question10 isn't contains in response to View Rules
        Test: if question11 isn't contains in response to View Rules
        """
        question9 = Question.objects.get(pk = 9)
        question10 = Question.objects.get(pk = 10)
        question11 = Question.objects.get(pk = 11)
        url = reverse("questionsRules:rules", args=(10,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question9.question_text)
        self.assertNotContains(response, question10.question_text)
        self.assertNotContains(response, question11.question_text)
        
        
    def test_rulesView_for_questionid_11(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 11

        question10 = Question10
        questions = [Question8, Question10, Question11, Quesiton12, Question13, Question14]
        question12 = Question12

        View return: latest_questions_list[question8, question10, question11, quesiton12, question13, question14]

        Test: if status code to View Rules is equal '200'
        Test: if latest_questions_list is equals questions
        Test: if question10 is contains in response to View Rules
        Test: if question12 is contains in response to View Rules
        """
        question10 = Question.objects.get(pk = 10)
        questions = Question.objects.filter(pk__in =[8,10,11,12,13,14]).order_by("id")
        question12 = Question.objects.get(pk = 12)
        url = reverse("questionsRules:rules", args=(11,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertContains(response, question10.question_text)
        self.assertContains(response, question12.question_text)
        
        
    def test_rulesView_for_questionid_12(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 12

        question11 = Question11
        question12 = Question12
        question13 = Question13

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question11 isn't contains in response to View Rules
        Test: if question12 isn't contains in response to View Rules
        Test: if question13 isn't contains in response to View Rules
        """
        question11 = Question.objects.get(pk = 11)
        question12 = Question.objects.get(pk = 12)
        question13 = Question.objects.get(pk = 13)
        url = reverse("questionsRules:rules", args=(12,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question11.question_text)
        self.assertNotContains(response, question12.question_text)
        self.assertNotContains(response, question13.question_text)
        
        
    def test_rulesView_for_questionid_13(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 13

        question12 = Question12
        question13 = Question13
        question14 = Question14

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question12 isn't contains in response to View Rules
        Test: if question13 isn't contains in response to View Rules
        Test: if question14 isn't contains in response to View Rules
        """
        question12 = Question.objects.get(pk = 12)
        question13 = Question.objects.get(pk = 13)
        question14 = Question.objects.get(pk = 14)
        url = reverse("questionsRules:rules", args=(13,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question12.question_text)
        self.assertNotContains(response, question13.question_text)
        self.assertNotContains(response, question14.question_text)
        
    
    def test_rulesView_for_questionid_14(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 14

        question13 = Question13
        question14 = Question14
        question15 = Question15

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question13 isn't contains in response to View Rules
        Test: if question14 isn't contains in response to View Rules
        Test: if question15 isn't contains in response to View Rules
        """
        question13 = Question.objects.get(pk = 13)
        question14 = Question.objects.get(pk = 14)
        question15 = Question.objects.get(pk = 15)
        url = reverse("questionsRules:rules", args=(14,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question13.question_text)
        self.assertNotContains(response, question14.question_text)
        self.assertNotContains(response, question15.question_text)
        
        
    def test_rulesView_for_questionid_15(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 15

        question10 = Question10
        questions = [Question11, Quesiton12, Question13, Question14, Question15, Question16, Question17]
        question18 = Question18

        View return: latest_questions_list[question11, question12, question13, question14, question15, question16, question17]

        Test: if status code to View Rules is equal '200'
        Test: if latest_questions_list is equals questions
        Test: if question14 isn't contains in response to View Rules
        Test: if question16 isn't contains in response to View Rules
        """
        question10 = Question.objects.get(pk = 10)
        questions = Question.objects.filter(pk__in=[11,12,13,14,15,16,17]).order_by("id")
        question18 = Question.objects.get(pk = 18)
        url = reverse("questionsRules:rules", args=(15,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question10.question_text)
        self.assertNotContains(response, question18.question_text)
        
        
    def test_rulesView_for_questionid_16(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 16

        question15 = Question15
        question16 = Question16
        question17 = Question17

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question15 isn't contains in response to View Rules
        Test: if question16 isn't contains in response to View Rules
        Test: if question17 isn't contains in response to View Rules
        """
        question15 = Question.objects.get(pk = 15)
        question16 = Question.objects.get(pk = 16)
        question17 = Question.objects.get(pk = 17)
        url = reverse("questionsRules:rules", args=(16,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question15.question_text)
        self.assertNotContains(response, question16.question_text)
        self.assertNotContains(response, question17.question_text)
        
    
    def test_rulesView_for_questionid_17(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 17

        question16 = Question16
        question17 = Question17
        question18 = Question18

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question16 isn't contains in response to View Rules
        Test: if question17 isn't contains in response to View Rules
        Test: if question18 isn't contains in response to View Rules
        """
        question16 = Question.objects.get(pk = 16)
        question17 = Question.objects.get(pk = 17)
        question18 = Question.objects.get(pk = 18)
        url = reverse("questionsRules:rules", args=(17,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        self.assertNotContains(response, question16.question_text)
        self.assertNotContains(response, question17.question_text)
        self.assertNotContains(response, question18.question_text)
        
        
    def test_rulesView_for_questionid_18(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 18

        question15 = Question15
        questions = [Question16, Question17, Question18]
        question19 = Question19

        View return: latest_questions_list[question16, question17, question18]

        Test: if status code to View Rules is equal '200'
        Test: if latest_questions_list is equals questions
        Test: if question15 isn't contains in response to View Rules
        Test: if question19 isn't contains in response to View Rules
        """
        question15 = Question.objects.get(pk = 15)
        questions = Question.objects.filter(pk__in=[16,17,18]).order_by("id")
        question19 = Question.objects.get(pk = 19)
        url = reverse("questionsRules:rules", args=(18,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question15.question_text)
        self.assertNotContains(response, question19.question_text)
        
        
    def test_rulesView_for_questionid_19(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 19

        question18 = Question18
        questions = [Question19, Question20, Question21, Question22]
        question22 = Question22

        View return: latest_questions_list[question19, question20, question21, question22]

        Test: if status code to View Rules is equal '200'
        Test: if latest_questions_list is equals questions
        Test: if question18 isn't contains in response to View Rules
        Test: if question22 is contains in response to View Rules
        """
        question18 = Question.objects.get(pk = 18)
        questions = Question.objects.filter(pk__in=[19,20,21,22]).order_by("id")
        question22 = Question.objects.get(pk = 22)
        url = reverse("questionsRules:rules", args=(19,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question18.question_text)
        self.assertContains(response, question22.question_text)
        
        
    def test_rulesView_for_questionid_20(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 20

        question19 = Question19
        question20 = Question20
        question21 = Question21

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question19 isn't contains in response to View Rules
        Test: if question20 isn't contains in response to View Rules
        Test: if question21 isn't contains in response to View Rules
        """
        questions = Question.objects.filter(pk__in = [19, 20, 21])
        url = reverse("questionsRules:rules", args=(20,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        for question in questions:
            self.assertNotContains(response, question.question_text)
            
            
    def test_rulesView_for_questionid_21(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 21

        question20 = Question20
        question21 = Question21
        question22 = Question22

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question20 isn't contains in response to View Rules
        Test: if question21 isn't contains in response to View Rules
        Test: if question22 isn't contains in response to View Rules
        """
        questions = Question.objects.filter(pk__in = [22, 20, 21])
        url = reverse("questionsRules:rules", args=(21,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        for question in questions:
            self.assertNotContains(response, question.question_text)
        
        
    def test_rulesView_for_questionid_22(self):
        """
        Verificate if the request for parameters, is the questions expected

        View Test: Rules.html
        Parameters: question = 22

        question20 = Question20
        question21 = Question21
        question22 = Question22

        View return: latest_questions_list[]

        Test: if status code to View Rules is equal '200'
        Test: if "Question Error!!" is contains in response to Vies Rules
        Test: if latest_questions_list is equals to []
        Test: if question20 isn't contains in response to View Rules
        Test: if question21 isn't contains in response to View Rules
        Test: if question22 isn't contains in response to View Rules
        """
        questions = Question.objects.filter(pk__in = [20, 21, 22])
        url = reverse("questionsRules:rules", args=(22,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # self.assertNotContains(response, "Question error!!")
        # self.assertQuerysetEqual(response.context["latest_question_list"], [])
        for question in questions:
            self.assertNotContains(response, question.question_text)
            
            
class QuestionsRules_IndexViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
        Create_Question("¿Tuvo la plaga del Gorgojo de Los Andes anteriormente?")
        
        
    def test_indexView_for_response(self):
        """
        Verificate if the request of the view is expected

        View Test: Index.html

        questions = [Question1, Question2]
        question3 = Question3

        View return: latest_questions_list[question1, question2]

        Test: if status code to View index is equal '200'
        Test: if latest_questions_list is equals to questions
        Test: if question3 isn't contains in response to View Index
        """
        questions = Question.objects.filter(pk__in = [1, 2]).order_by("id")
        question3 = Question.objects.get(pk = 3)
        url = reverse("questionsRules:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertNotContains(response, question3.question_text)
        
        
class QuestionsRules_GorgojoInformationViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
        Create_Question("¿Tuvo la plaga del Gorgojo de Los Andes anteriormente?")
        Create_Question("¿La plaga del Gorgojo de los Andes afecto su cultivo de papa?")
        Create_Question("¿En qué etapa se encuentra su cultivo?")
        
    def test_gorgojoInformationView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 3 the status code is 404
        
        Test: arg =1, status_code = 404
        Test: arg =2, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:gorgojoInformation", args=[1,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:gorgojoInformation", args=[2,]))
        self.assertEqual(response.status_code, 404)
        
    def test_gorgojoInformationView_for_response(self):
        """
        Verificate if the request of the view is expected

        View Test: GorgojoInformation.html
        parameters: 3

        questions = [Question3, Question4]
        question5 = Question5

        View return: latest_questions_list[question3, question4]

        Test: if status code to View gorgojoInformation is equal '200'
        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 3
        Test: if question5 isn't contains in response to View Index
        """
        questions = Question.objects.filter(pk__in = [3,4]).order_by("id")
        question5 = Question.objects.get(pk = 5)
        response = self.client.get(reverse("questionsRules:gorgojoInformation", args=[3,]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 3)
        self.assertNotContains(response, question5.question_text)
        

class QuestionsRules_GorgojoInformationAndGoodPracticeViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
        Create_Question("¿Tuvo la plaga del Gorgojo de Los Andes anteriormente?")
        Create_Question("¿La plaga del Gorgojo de los Andes afecto su cultivo de papa?")
        Create_Question("¿En qué etapa se encuentra su cultivo?")
        
    def test_gorgojoInformationAndGoodPracticeView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 3 the status code is 404
        
        Test: arg =1, status_code = 404
        Test: arg =2, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:gorgojoInformationAndGoodPractice", args=[1,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:gorgojoInformationAndGoodPractice", args=[2,]))
        self.assertEqual(response.status_code, 404)
        
    def test_gorgojoInformationAndGoodPracticeView_for_response(self):
        """
        Verificate if the request of the view is expected

        View Test: gorgojoInformationAndGoodPractice.html
        parameters: 3

        questions = [Question3, Question4]
        question5 = Question5

        View return: latest_questions_list[question3, question4]

        Test: if status code to View gorgojoInformationAndGoodPractice is equal '200'
        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 3
        Test: if question5 isn't contains in response to View Index
        """
        questions = Question.objects.filter(pk__in = [3,4]).order_by("id")
        question5 = Question.objects.get(pk = 5)
        response = self.client.get(reverse("questionsRules:gorgojoInformationAndGoodPractice", args=[3,]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 3)
        self.assertNotContains(response, question5.question_text)
        

class QuestionsRules_GoodPracticesViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
        Create_Question("¿Tuvo la plaga del Gorgojo de Los Andes anteriormente?")
        Create_Question("¿La plaga del Gorgojo de los Andes afecto su cultivo de papa?")
        Create_Question("¿En qué etapa se encuentra su cultivo?")
    
    def test_goodPracticesView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 3 the status code is 404
        
        Test: arg =1, status_code = 404
        Test: arg =2, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:goodPractices", args=[1,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:goodPractices", args=[2,]))
        self.assertEqual(response.status_code, 404)
        
    def test_goodPracticesView_for_response(self):
        """
        Verificate if the request of the view is expected

        View Test: goodPractices.html
        parameters: 3

        questions = [Question3, Question4]
        question5 = Question5

        View return: latest_questions_list[question3, question4]

        Test: if status code to View goodPractices is equal '200'
        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 3
        Test: if question5 isn't contains in response to View preventiveMeasures
        """
        questions = Question.objects.filter(pk__in = [3,4]).order_by("id")
        question5 = Question.objects.get(pk = 5)
        response = self.client.get(reverse("questionsRules:goodPractices", args=[3,]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 3)
        self.assertNotContains(response, question5.question_text)
        
        

class QuestionsRules_PreventiveMeasuresViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
        Create_Question("¿Tuvo la plaga del Gorgojo de Los Andes anteriormente?")
        Create_Question("¿La plaga del Gorgojo de los Andes afecto su cultivo de papa?")
        Create_Question("¿En qué etapa se encuentra su cultivo?")
        Create_Question("¿Realizó desinfecciones químicas?")
        
    def test_preventiveMeasuresView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 3 the status code is 404
        
        Test: arg =1, status_code = 404
        Test: arg =2, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:preventiveMeasures", args=[3,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:preventiveMeasures", args=[6,]))
        self.assertEqual(response.status_code, 404)
        
          
    def test_preventiveMeasuresView_for_response(self):
        """
        Verificate if the request of the view is expected

        View Test: preventiveMeasures.html
        parameters: 5

        questions = [Question5]
        question6 = Question6

        View return: latest_questions_list[question5]

        Test: if status code to View preventiveMeasures is equal '200'
        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 5
        Test: if question5 isn't contains in response to View preventiveMeasures
        """
        questions = Question.objects.filter(pk__in = [5]).order_by("id")
        question6 = Question.objects.get(pk = 6)
        response = self.client.get(reverse("questionsRules:preventiveMeasures", args=[5,]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 5)
        self.assertNotContains(response, question6.question_text)
        
        
class QuestionsRules_ChemicalsViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_chemicalsView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 6 the status code is 404
        if args != 11 the status code is 404
        if args != 15 the status code is 404
        
        Test: arg =6, status_code = 200
        Test: arg =11, status_code = 200
        Test: arg 15, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:chemicals", args=[6,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:chemicals", args=[11,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:chemicals", args=[15,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:chemicals", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:chemicals", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
    def test_chemicalsView_for_response_value6(self):
        """
        Verificate if the request of the view is expected

        View Test: chemicals.html
        parameters: 6

        questions = [question6, question7, question8, question9, question10]
        question7 = Question7

        View return: latest_questions_list[question6, question7, question8, question9, question10]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 6
        Test: if question7 isn't contains in response to View chemicals
        """
        questions = Question.objects.filter(pk__in = [6,7,8,9,10]).order_by("id")
        question7 = Question.objects.get(pk = 7)
        response = self.client.get(reverse("questionsRules:chemicals", args=[6,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 6)
        self.assertNotContains(response, question7.question_text)
        
    def test_chemicalsView_for_response_value11(self):        
        """
        Verificate if the request of the view is expected

        View Test: chemicals.html
        parameters: 11

        questions = [question8,question10,question11,question12,question13,question14]
        question12 = Question12

        View return: latest_questions_list[question8,question10,question11,question12,question13,question14]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 11
        Test: if question7 isn't contains in response to View chemicals
        """
        questions = Question.objects.filter(pk__in = [8,10,11,12,13,14]).order_by("id")
        question12 = Question.objects.get(pk = 12)
        response = self.client.get(reverse("questionsRules:chemicals", args=[11,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 11)
        self.assertNotContains(response, question12.question_text)
        
    def test_chemicalsView_for_response_value15(self):        
        """
        Verificate if the request of the view is expected

        View Test: chemicals.html
        parameters: 15

        questions = [question11,question12,question13,question14,question15,question16,question17]
        question16 = Question16

        View return: latest_questions_list[question11,question12,question13,question14,question15,question16,question17]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 15
        Test: if question16 isn't contains in response to View chemicals
        """
        questions = Question.objects.filter(pk__in = [11,12,13,14,15,16,17]).order_by("id")
        question16 = Question.objects.get(pk = 16)
        response = self.client.get(reverse("questionsRules:chemicals", args=[15,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 15)
        self.assertNotContains(response, question16.question_text)
        
        
class QuestionsRules_DitchesViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_ditchesView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 6 the status code is 404
        if args != 11 the status code is 404
        if args != 15 the status code is 404
        
        Test: arg =6, status_code = 200
        Test: arg =11, status_code = 200
        Test: arg 15, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:ditches", args=[6,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:ditches", args=[11,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:ditches", args=[15,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:ditches", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:ditches", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
    def test_ditchesView_for_response_value6(self):
        """
        Verificate if the request of the view is expected

        View Test: ditches.html
        parameters: 6

        questions = [question6, question7, question8, question9, question10]
        question7 = Question7

        View return: latest_questions_list[question6, question7, question8, question9, question10]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 6
        Test: if question7 isn't contains in response to View ditches
        """
        questions = Question.objects.filter(pk__in = [6,7,8,9,10]).order_by("id")
        question7 = Question.objects.get(pk = 7)
        response = self.client.get(reverse("questionsRules:ditches", args=[6,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 6)
        self.assertNotContains(response, question7.question_text)
        
    def test_ditchesView_for_response_value11(self):        
        """
        Verificate if the request of the view is expected

        View Test: ditches.html
        parameters: 11

        questions = [question8,question10,question11,question12,question13,question14]
        question12 = Question12

        View return: latest_questions_list[question8,question10,question11,question12,question13,question14]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 11
        Test: if question7 isn't contains in response to View ditches
        """
        questions = Question.objects.filter(pk__in = [8,10,11,12,13,14]).order_by("id")
        question12 = Question.objects.get(pk = 12)
        response = self.client.get(reverse("questionsRules:ditches", args=[11,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 11)
        self.assertNotContains(response, question12.question_text)
        
    def test_ditchesView_for_response_value15(self):        
        """
        Verificate if the request of the view is expected

        View Test: ditches.html
        parameters: 15

        questions = [question11,question12,question13,question14,question15,question16,question17]
        question16 = Question16

        View return: latest_questions_list[question11,question12,question13,question14,question15,question16,question17]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 15
        Test: if question16 isn't contains in response to View ditches
        """
        questions = Question.objects.filter(pk__in = [11,12,13,14,15,16,17]).order_by("id")
        question16 = Question.objects.get(pk = 16)
        response = self.client.get(reverse("questionsRules:ditches", args=[15,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 15)
        self.assertNotContains(response, question16.question_text)
        
        
class QuestionsRules_PlantOtherVegetablesViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_ditchesView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 6 the status code is 404
        if args != 11 the status code is 404
        
        Test: arg =6, status_code = 200
        Test: arg =11, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[6,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[11,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
    def test_plantOtherVegetablesView_for_response_value6(self):
        """
        Verificate if the request of the view is expected

        View Test: plantOtherVegetables.html
        parameters: 6

        questions = [question6, question7, question8, question9, question10]
        question7 = Question7

        View return: latest_questions_list[question6, question7, question8, question9, question10]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 6
        Test: if question7 isn't contains in response to View plantOtherVegetables
        """
        questions = Question.objects.filter(pk__in = [6,7,8,9,10]).order_by("id")
        question7 = Question.objects.get(pk = 7)
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[6,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 6)
        self.assertNotContains(response, question7.question_text)
        
    def test_plantOtherVegetablesView_for_response_value11(self):        
        """
        Verificate if the request of the view is expected

        View Test: plantOtherVegetables.html
        parameters: 11

        questions = [question8,question10,question11,question12,question13,question14]
        question12 = Question12

        View return: latest_questions_list[question8,question10,question11,question12,question13,question14]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 11
        Test: if question7 isn't contains in response to View plantOtherVegetables
        """
        questions = Question.objects.filter(pk__in = [8,10,11,12,13,14]).order_by("id")
        question12 = Question.objects.get(pk = 12)
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[11,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 11)
        self.assertNotContains(response, question12.question_text)
        
        
class QuestionsRules_PlantPickUpViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
        Create_Question("¿Tuvo la plaga del Gorgojo de Los Andes anteriormente?")
        Create_Question("¿La plaga del Gorgojo de los Andes afecto su cultivo de papa?")
        Create_Question("¿En qué etapa se encuentra su cultivo?")
        Create_Question("¿Realizó desinfecciones químicas?")
        Create_Question("¿Realizó zanjas alrededor de la parcela para la siembra?")
        Create_Question("¿Sabe usted qué cultivos podría sembrar alrededor de la parcela?")
        Create_Question("¿Removió las plantas (K'ipas) de cosechas anteriores?")
        Create_Question("¿Sabe usted qué trampas podría poner alrededor del cultivo?")
        
    def test_ditchesView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 6 the status code is 404
        
        Test: arg =6, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =5, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[6,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:plantOtherVegetables", args=[5,]))
        self.assertEqual(response.status_code, 404)
        
    def test_plantPickUpView_for_response_value6(self):
        """
        Verificate if the request of the view is expected

        View Test: plantPickUp.html
        parameters: 6

        questions = [question6, question7, question8, question9, question10]
        question7 = Question7

        View return: latest_questions_list[question6, question7, question8, question9, question10]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 6
        Test: if question7 isn't contains in response to View plantPickUp
        """
        questions = Question.objects.filter(pk__in = [6,7,8,9,10]).order_by("id")
        question7 = Question.objects.get(pk = 7)
        response = self.client.get(reverse("questionsRules:plantPickUp", args=[6,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 6)
        self.assertNotContains(response, question7.question_text)
        

class QuestionsRules_TrapsViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_trapsView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 6 the status code is 404
        if args != 11 the status code is 404
        if args != 15 the status code is 404
        
        Test: arg =6, status_code = 200
        Test: arg =11, status_code = 200
        Test: arg 15, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:traps", args=[6,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:traps", args=[11,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:traps", args=[15,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:traps", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:traps", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
    def test_ditchesView_for_response_value6(self):
        """
        Verificate if the request of the view is expected

        View Test: traps.html
        parameters: 6

        questions = [question6, question7, question8, question9, question10]
        question7 = Question7

        View return: latest_questions_list[question6, question7, question8, question9, question10]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 6
        Test: if question7 isn't contains in response to View traps
        """
        questions = Question.objects.filter(pk__in = [6,7,8,9,10]).order_by("id")
        question7 = Question.objects.get(pk = 7)
        response = self.client.get(reverse("questionsRules:traps", args=[6,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 6)
        self.assertNotContains(response, question7.question_text)
        
    def test_trapsView_for_response_value11(self):        
        """
        Verificate if the request of the view is expected

        View Test: traps.html
        parameters: 11

        questions = [question8,question10,question11,question12,question13,question14]
        question12 = Question12

        View return: latest_questions_list[question8,question10,question11,question12,question13,question14]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 11
        Test: if question7 isn't contains in response to View traps
        """
        questions = Question.objects.filter(pk__in = [8,10,11,12,13,14]).order_by("id")
        question12 = Question.objects.get(pk = 12)
        response = self.client.get(reverse("questionsRules:traps", args=[11,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 11)
        self.assertNotContains(response, question12.question_text)
        
    def test_trapsView_for_response_value15(self):        
        """
        Verificate if the request of the view is expected

        View Test: traps.html
        parameters: 15

        questions = [question11,question12,question13,question14,question15,question16,question17]
        question16 = Question16

        View return: latest_questions_list[question11,question12,question13,question14,question15,question16,question17]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 15
        Test: if question16 isn't contains in response to View traps
        """
        questions = Question.objects.filter(pk__in = [11,12,13,14,15,16,17]).order_by("id")
        question16 = Question.objects.get(pk = 16)
        response = self.client.get(reverse("questionsRules:traps", args=[15,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 15)
        self.assertNotContains(response, question16.question_text)


class QuestionsRules_ContinueStageChoiceViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_continueStageChoiceView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 11 the status code is 404
        if args != 15 the status code is 404
        if args != 18 the status code is 404
        if args != 19 the status code is 404
        
        Test: arg =11, status_code = 200
        Test: arg =15, status_code = 200
        Test: arg =18, status_code = 200
        Test: arg =19, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[11,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[15,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[18,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[19,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_continueStageChoiceView_for_response_value11(self):        
        """
        Verificate if the request of the view is expected

        View Test: continueStageChoice.html
        parameters: 11

        questions = [question8,question10,question11,question12,question13,question14]
        question12 = Question12

        View return: latest_questions_list[question8,question10,question11,question12,question13,question14]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 11
        Test: if question7 isn't contains in response to View continueStageChoice
        """
        questions = Question.objects.filter(pk__in = [8,10,11,12,13,14]).order_by("id")
        question12 = Question.objects.get(pk = 12)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[11,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 11)
        self.assertNotContains(response, question12.question_text)
        
    def test_continueStageChoiceView_for_response_value15(self):        
        """
        Verificate if the request of the view is expected

        View Test: continueStageChoice.html
        parameters: 15

        questions = [question11,question12,question13,question14,question15,question16,question17]
        question16 = Question16

        View return: latest_questions_list[question11,question12,question13,question14,question15,question16,question17]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 15
        Test: if question16 isn't contains in response to View continueStageChoice
        """
        questions = Question.objects.filter(pk__in = [11,12,13,14,15,16,17]).order_by("id")
        question16 = Question.objects.get(pk = 16)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[15,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 15)
        self.assertNotContains(response, question16.question_text)
        
    def test_continueStageChoiceView_for_response_value18(self):        
        """
        Verificate if the request of the view is expected

        View Test: continueStageChoice.html
        parameters: 18

        questions = [question16,question17,question18]
        question19 = Question19

        View return: latest_questions_list[question16,question17,question18]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 18
        Test: if question19 isn't contains in response to View continueStageChoice
        """
        questions = Question.objects.filter(pk__in = [16,17,18]).order_by("id")
        question19 = Question.objects.get(pk = 19)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[18,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 18)
        self.assertNotContains(response, question19.question_text)
        
    def test_continueStageChoiceView_for_response_value19(self):        
        """
        Verificate if the request of the view is expected

        View Test: continueStageChoice.html
        parameters: 19

        questions = [question19,question20,question21,question22]
        question1 = Question1

        View return: latest_questions_list[question19,question20,question21,question22]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 19
        Test: if question1 isn't contains in response to View continueStageChoice
        """
        questions = Question.objects.filter(pk__in = [19,20,21,22]).order_by("id")
        question1 = Question.objects.get(pk = 1)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[19,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 19)
        self.assertNotContains(response, question1.question_text)
        
        
class QuestionsRules_CulturalWorkViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_culturalWorkView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 11 the status code is 404
        if args != 15 the status code is 404
        
        Test: arg =11, status_code = 200
        Test: arg =15, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:culturalWork", args=[11,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:culturalWork", args=[15,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:culturalWork", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:culturalWork", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_culturalWorkView_for_response_value11(self):        
        """
        Verificate if the request of the view is expected

        View Test: culturalWork.html
        parameters: 11

        questions = [question8,question10,question11,question12,question13,question14]
        question12 = Question12

        View return: latest_questions_list[question8,question10,question11,question12,question13,question14]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 11
        Test: if question7 isn't contains in response to View culturalWork
        """
        questions = Question.objects.filter(pk__in = [8,10,11,12,13,14]).order_by("id")
        question12 = Question.objects.get(pk = 12)
        response = self.client.get(reverse("questionsRules:culturalWork", args=[11,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 11)
        self.assertNotContains(response, question12.question_text)
        
    def test_culturalWorkView_for_response_value15(self):        
        """
        Verificate if the request of the view is expected

        View Test: culturalWork.html
        parameters: 15

        questions = [question11,question12,question13,question14,question15,question16,question17]
        question16 = Question16

        View return: latest_questions_list[question11,question12,question13,question14,question15,question16,question17]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 15
        Test: if question16 isn't contains in response to View culturalWork
        """
        questions = Question.objects.filter(pk__in = [11,12,13,14,15,16,17]).order_by("id")
        question16 = Question.objects.get(pk = 16)
        response = self.client.get(reverse("questionsRules:culturalWork", args=[15,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 15)
        self.assertNotContains(response, question16.question_text)
        
        
class QuestionsRules_GorgojoMeasuresViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_gorgojoMeasuresView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 11 the status code is 404
        if args != 15 the status code is 404
        
        Test: arg =11, status_code = 200
        Test: arg =15, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:gorgojoMeasures", args=[11,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:gorgojoMeasures", args=[15,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:gorgojoMeasures", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:gorgojoMeasures", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_gorgojoMeasuresView_for_response_value11(self):        
        """
        Verificate if the request of the view is expected

        View Test: gorgojoMeasures.html
        parameters: 11

        questions = [question8,question10,question11,question12,question13,question14]
        question12 = Question12

        View return: latest_questions_list[question8,question10,question11,question12,question13,question14]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 11
        Test: if question7 isn't contains in response to View gorgojoMeasures
        """
        questions = Question.objects.filter(pk__in = [8,10,11,12,13,14]).order_by("id")
        question12 = Question.objects.get(pk = 12)
        response = self.client.get(reverse("questionsRules:gorgojoMeasures", args=[11,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 11)
        self.assertNotContains(response, question12.question_text)
        
    def test_gorgojoMeasuresView_for_response_value15(self):        
        """
        Verificate if the request of the view is expected

        View Test: gorgojoMeasures.html
        parameters: 15

        questions = [question11,question12,question13,question14,question15,question16,question17]
        question16 = Question16

        View return: latest_questions_list[question11,question12,question13,question14,question15,question16,question17]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 15
        Test: if question16 isn't contains in response to View gorgojoMeasures
        """
        questions = Question.objects.filter(pk__in = [11,12,13,14,15,16,17]).order_by("id")
        question16 = Question.objects.get(pk = 16)
        response = self.client.get(reverse("questionsRules:gorgojoMeasures", args=[15,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 15)
        self.assertNotContains(response, question16.question_text)
        
        
class QuestionsRules_GatherGorgojoViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_gatherGorgojoView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 15 the status code is 404
        if args != 18 the status code is 404
        
        Test: arg =15, status_code = 200
        Test: arg =18, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[15,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[18,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:continueStageChoice", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_gatherGorgojoView_for_response_value15(self):        
        """
        Verificate if the request of the view is expected

        View Test: gatherGorgojo.html
        parameters: 15

        questions = [question11,question12,question13,question14,question15,question16,question17]
        question16 = Question16

        View return: latest_questions_list[question11,question12,question13,question14,question15,question16,question17]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 15
        Test: if question16 isn't contains in response to View gatherGorgojo
        """
        questions = Question.objects.filter(pk__in = [11,12,13,14,15,16,17]).order_by("id")
        question16 = Question.objects.get(pk = 16)
        response = self.client.get(reverse("questionsRules:gatherGorgojo", args=[15,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 15)
        self.assertNotContains(response, question16.question_text)
        
    def test_gatherGorgojoView_for_response_value18(self):        
        """
        Verificate if the request of the view is expected

        View Test: gatherGorgojo.html
        parameters: 18

        questions = [question16,question17,question18]
        question19 = Question19

        View return: latest_questions_list[question16,question17,question18]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 18
        Test: if question19 isn't contains in response to View gatherGorgojo
        """
        questions = Question.objects.filter(pk__in = [16,17,18]).order_by("id")
        question19 = Question.objects.get(pk = 19)
        response = self.client.get(reverse("questionsRules:gatherGorgojo", args=[18,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 18)
        self.assertNotContains(response, question19.question_text)
        
        
class QuestionsRules_CountherTheGorgojoViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_countherTheGorgojoView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 15 the status code is 404
        if args != 18 the status code is 404
        
        Test: arg =15, status_code = 200
        Test: arg =18, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =10, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:countherTheGorgojo", args=[15,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:countherTheGorgojo", args=[18,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:countherTheGorgojo", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:countherTheGorgojo", args=[10,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_countherTheGorgojoView_for_response_value15(self):        
        """
        Verificate if the request of the view is expected

        View Test: countherTheGorgojo.html
        parameters: 15

        questions = [question11,question12,question13,question14,question15,question16,question17]
        question16 = Question16

        View return: latest_questions_list[question11,question12,question13,question14,question15,question16,question17]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 15
        Test: if question16 isn't contains in response to View countherTheGorgojo
        """
        questions = Question.objects.filter(pk__in = [11,12,13,14,15,16,17]).order_by("id")
        question16 = Question.objects.get(pk = 16)
        response = self.client.get(reverse("questionsRules:countherTheGorgojo", args=[15,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 15)
        self.assertNotContains(response, question16.question_text)
        
    def test_countherTheGorgojoView_for_response_value18(self):        
        """
        Verificate if the request of the view is expected

        View Test: countherTheGorgojo.html
        parameters: 18

        questions = [question16,question17,question18]
        question19 = Question19

        View return: latest_questions_list[question16,question17,question18]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 18
        Test: if question19 isn't contains in response to View countherTheGorgojo
        """
        questions = Question.objects.filter(pk__in = [16,17,18]).order_by("id")
        question19 = Question.objects.get(pk = 19)
        response = self.client.get(reverse("questionsRules:countherTheGorgojo", args=[18,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 18)
        self.assertNotContains(response, question19.question_text)
        
        
class QuestionsRules_PotatoSelectionViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_potatoSelectionView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 18 the status code is 404
        
        Test: arg =18, status_code = 200
        Test: arg =7, status_code = 404
        Test: arg =19, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:potatoSelection", args=[18,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:potatoSelection", args=[7,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:potatoSelection", args=[19,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_potatoSelectionView_for_response_value18(self):        
        """
        Verificate if the request of the view is expected

        View Test: potatoSelection.html
        parameters: 18

        questions = [question16,question17,question18]
        question19 = Question19

        View return: latest_questions_list[question16,question17,question18]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 18
        Test: if question19 isn't contains in response to View potatoSelection
        """
        questions = Question.objects.filter(pk__in = [16,17,18]).order_by("id")
        question19 = Question.objects.get(pk = 19)
        response = self.client.get(reverse("questionsRules:potatoSelection", args=[18,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 18)
        self.assertNotContains(response, question19.question_text)
        
        
class QuestionsRules_SoilRemovalViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_soilRemovalView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 19 the status code is 404
        
        Test: arg =19, status_code = 200
        Test: arg =18, status_code = 404
        Test: arg =20, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:soilRemoval", args=[19,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:soilRemoval", args=[18,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:soilRemoval", args=[20,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_soilRemovalView_for_response_value18(self):        
        """
        Verificate if the request of the view is expected

        View Test: soilRemoval.html
        parameters: 19

        questions = [question19,question20,question21,question22]
        question18 = Question18

        View return: latest_questions_list[question19,question20,question21,question22]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 19
        Test: if question18 isn't contains in response to View soilRemoval
        """
        questions = Question.objects.filter(pk__in = [19,20,21,22]).order_by("id")
        question18 = Question.objects.get(pk = 18)
        response = self.client.get(reverse("questionsRules:soilRemoval", args=[19,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 19)
        self.assertNotContains(response, question18.question_text)
        
        
class QuestionsRules_WarehousePreparationViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_warehousePreparationView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 19 the status code is 404
        
        Test: arg =19, status_code = 200
        Test: arg =18, status_code = 404
        Test: arg =20, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:warehousePreparation", args=[19,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:warehousePreparation", args=[18,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:warehousePreparation", args=[20,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_warehousePreparationView_for_response_value18(self):        
        """
        Verificate if the request of the view is expected

        View Test: warehousePreparation.html
        parameters: 19

        questions = [question19,question20,question21,question22]
        question18 = Question18

        View return: latest_questions_list[question19,question20,question21,question22]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 19
        Test: if question18 isn't contains in response to View warehousePreparation
        """
        questions = Question.objects.filter(pk__in = [19,20,21,22]).order_by("id")
        question18 = Question.objects.get(pk = 18)
        response = self.client.get(reverse("questionsRules:warehousePreparation", args=[19,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 19)
        self.assertNotContains(response, question18.question_text)
        
        
class QuestionsRules_DangerIntoWarehouseViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_dangerIntoWarehouseView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 19 the status code is 404
        
        Test: arg =19, status_code = 200
        Test: arg =18, status_code = 404
        Test: arg =20, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:dangerIntoWarehouse", args=[19,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:dangerIntoWarehouse", args=[18,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:dangerIntoWarehouse", args=[20,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_dangerIntoWarehouseView_for_response_value18(self):        
        """
        Verificate if the request of the view is expected

        View Test: dangerIntoWarehouse.html
        parameters: 19

        questions = [question19,question20,question21,question22]
        question18 = Question18

        View return: latest_questions_list[question19,question20,question21,question22]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 19
        Test: if question18 isn't contains in response to View dangerIntoWarehouse
        """
        questions = Question.objects.filter(pk__in = [19,20,21,22]).order_by("id")
        question18 = Question.objects.get(pk = 18)
        response = self.client.get(reverse("questionsRules:dangerIntoWarehouse", args=[19,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 19)
        self.assertNotContains(response, question18.question_text)
        
        
class QuestionsRules_WhiteFungusViewTests(TestCase):
    def setUp(self):
        Create_Question("¿Conoces al Gorgojo de Los Andes?")
        Create_Question("¿Es su primer cultivo?")
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
        
    def test_whiteFungusView_for_response404(self):
        """
        Test for pag_not_found 404
        if args != 19 the status code is 404
        
        Test: arg =19, status_code = 200
        Test: arg =18, status_code = 404
        Test: arg =20, status_code = 404
        """
        response = self.client.get(reverse("questionsRules:whiteFungus", args=[19,]))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("questionsRules:whiteFungus", args=[18,]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("questionsRules:whiteFungus", args=[20,]))
        self.assertEqual(response.status_code, 404)
        
        
    def test_whiteFungusView_for_response_value18(self):        
        """
        Verificate if the request of the view is expected

        View Test: whiteFungus.html
        parameters: 19

        questions = [question19,question20,question21,question22]
        question18 = Question18

        View return: latest_questions_list[question19,question20,question21,question22]

        Test: if latest_questions_list is equals to questions
        Test: if question.id is equals to 19
        Test: if question18 isn't contains in response to View whiteFungus
        """
        questions = Question.objects.filter(pk__in = [19,20,21,22]).order_by("id")
        question18 = Question.objects.get(pk = 18)
        response = self.client.get(reverse("questionsRules:whiteFungus", args=[19,]))
        self.assertQuerysetEqual(response.context["latest_question_list"].order_by("id"), questions)
        self.assertEqual(response.context["question"].id, 19)
        self.assertNotContains(response, question18.question_text)
        