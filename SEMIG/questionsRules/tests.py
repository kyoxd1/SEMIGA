from django.test import TestCase
from django.utils import timezone

from experta import *

from .knowledgeForGorgojo import *
from .models import Question

"""
    TEST ALL RULES FOR FACT
"""

class Gorgojo_Rules_For_Facts_Tests(TestCase):
    """
        CREATION QUESTION FOR RULES TEST
    """
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

def Create_Question(question_text):
    """Question cretion for unit test"""
    return Question.objects.create(question_text=question_text, pub_date= timezone.now())
