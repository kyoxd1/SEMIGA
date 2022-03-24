from django.test import TestCase
from django.utils import timezone

from experta import *
from .models import Question

"""
    TEST ALL RULES FOR FACT
"""

class Gorgojo_Rules_For_Facts_Tests(TestCase):
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
    
    def test_return_fact_questions_list_for_value(self):
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
        
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 4
            return: question_list[ question3 , question4]
        """
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=4))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(latest_question_list[1].question_text, question_list[1].question_text)
        
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 5
            return: question_list[ question5]
        """
        question_list = Question.objects.filter(pk__in =[5])
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(QuestionList(questionId=5))
        enginer.run()
        latest_question_list = enginer.listQuestion
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
           
                
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 6
            return: question_list[ question6 , question7, question8, question9, question10]
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
        
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 11
            return: question_list[ question8 , question10, question11, question12, question13, question14]
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
        
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 15
            return: question_list[ question11 , question12, question13, question14, question15, question16, question17]
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
        
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 18
            return: question_list[ question16, question 17, question18]
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
        
        
        """
            Rule Test of:
                Fac: QuestionList(questionId = value)
                Value: 19
            return: question_list[ question19 , question20, question21, question22]
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

    def test_return_fact_gorgojo_question_value(self):
        class GorgojoQuestion(Fact):
            pass
        
        class integratedHandling(KnowledgeEngine):
            @Rule(GorgojoQuestion(question1='Si',question2='No'))
            def GorgojoQuestion_rule1(self):
                question = Question.objects.filter(pk__in=[3])
                urlRedirect = "questionsRules:rules"
                self.question = question
                self.urlRedirect = urlRedirect
                return self.question, self.urlRedirect

            @Rule(GorgojoQuestion(question1='Si',question2='Si'))
            def GorgojoQuestion_rule2(self):
                question = Question.objects.filter(pk__in=[3])
                urlRedirect = "questionsRules:goodPractices"
                self.question = question
                self.urlRedirect = urlRedirect
                return self.question, self.urlRedirect

            @Rule(GorgojoQuestion(question1='No',question2='No'))
            def GorgojoQuestion_rule3(self):
                question = Question.objects.filter(pk__in=[3])
                urlRedirect = "questionsRules:gorgojoInformation"
                self.question = question
                self.urlRedirect = urlRedirect
                return self.question, self.urlRedirect
                

            @Rule(GorgojoQuestion(question1='No',question2='Si'))
            def GorgojoQuestion_rule4(self):
                question = Question.objects.filter(pk__in=[3])
                urlRedirect = "questionsRules:gorgojoInformationAndGoodPractice"
                self.question = question
                self.urlRedirect = urlRedirect
                return self.question, self.urlRedirect
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestion(question1 = value1, question2 = value2)
                Value1: Si
                Value2: Si
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
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestion(question1 = value1, question2 = value2)
                Value1: Si
                Value2: No
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
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestion(question1 = value1, question2 = value2)
                Value1: No
                Value2: Si
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
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestion(question1 = value1, question2 = value2)
                Value1: No
                Value2: No
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
        
    
    def test_return_fact_gorgojo_questionTwo_value(self):
        """
        Test For Fact = GorgojoQuestionTwo
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
        """
        class GorgojoQuestionTwo(Fact):
            pass
        class integratedHandling(KnowledgeEngine):
            question = Question.objects.filter(pk__in=[3])
            urlRedirect= "questionsRules:404"
            @Rule(AS.gorgojoQuestionTwo << GorgojoQuestionTwo(question3=L('Si') | L('No'), question4=L('No')))
            def seen_numberFive(self):
                question = Question.objects.filter(pk__in=[5])
                urlRedirect = "questionsRules:rules"
                self.question = question
                self.urlRedirect = urlRedirect
                return self.question, self.urlRedirect
            
            @Rule(AS.gorgojoQuestionTwo << GorgojoQuestionTwo(question3=L('No') | L('Si'), question4=L('Si')))
            def seen_numberSix(self):
                question = Question.objects.filter(pk__in=[5])
                urlRedirect = "questionsRules:preventiveMeasures"
                self.question = question
                self.urlRedirect = urlRedirect
                return self.question, self.urlRedirect
            
            
        """
            Rule Test of:
                Fac: GorgojoQuestionTwo(question3 = value1, question4 = value2)
                Value1: Si
                Value2: Si
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
            return: question_list[ question5], urlRedirect='questionsRules:preventiveMeasures'
        """
        question_list = Question.objects.filter(pk__in =[5])
        url = "questionsRules:preventiveMeasures"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionTwo(question3='No', question4='Si'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestionTwo(question3 = value1, question4 = value2)
                Value1: Si
                Value2: No
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
            return: question_list[ question5], urlRedirect='questionsRules:rules'
        """
        question_list = Question.objects.filter(pk__in =[5])
        url = "questionsRules:rules"
        enginer = integratedHandling()
        enginer.reset()
        enginer.declare(GorgojoQuestionTwo(question3='No', question4='No'))
        enginer.run()
        latest_question_list = enginer.question
        urlRedirect = enginer.urlRedirect
        
        self.assertEqual(latest_question_list[0].question_text, question_list[0].question_text)
        self.assertEqual(urlRedirect, url)
        
    
    def test_return_fact_gorgojo_questionThree_value(self):
        """
        Test For Fact = GorgojoQuestionThree
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
        """
        class GorgojoQuestionThree(Fact):
            pass
        class integratedHandling(KnowledgeEngine):
            urlRedirect = "questionsRules:rules"
            @Rule(GorgojoQuestionThree(resp='Recién planeo empezar mi cultivo'))
            def GorgojoQuestionThree_1(self):
                question = Question.objects.filter(pk__in=[6])
                self.question = question
                return self.question, self.urlRedirect
            
            @Rule(GorgojoQuestionThree(resp='Acabo de sembrar'))
            def GorgojoQuestionThree_2(self):
                question = Question.objects.filter(pk__in=[11])
                self.question = question
                return self.question, self.urlRedirect
            
            @Rule(GorgojoQuestionThree(resp='Mi cultivo de papa, ya esta más de la mitad'))
            def GorgojoQuestionThree_3(self):
                question = Question.objects.filter(pk__in=[15])
                self.question = question
                return self.question, self.urlRedirect
            
            @Rule(GorgojoQuestionThree(resp='Estoy por cosechar mi cultivo'))
            def GorgojoQuestionThree_4(self):
                question = Question.objects.filter(pk__in=[18])
                self.question = question
                return self.question, self.urlRedirect
            
            @Rule(GorgojoQuestionThree(resp='Acabo de cosechar mi cultivo'))
            def GorgojoQuestionThree_5(self):
                question = Question.objects.filter(pk__in=[19])
                self.question = question
                return self.question, self.urlRedirect
           
            
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
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
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
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
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
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
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
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
        
        
        """
            Rule Test of:
                Fac: GorgojoQuestionThree(resp=value)
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
        
    
    def test_return_fact_gorgojo_questionFor_value(self):
        """
        Test For Fact = GorgojoQuestionTwo
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
        """
        
        class GorgojoQuestionFor(Fact):
            pass
        
        @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('No'), question7=L('No') | L('Si'), question8=L('No') | L('Si'), question9=L('No') | L('Si'), question10=L('No') | L('Si')))
        def GorgojoQuestionFor_1(self):
            question = Question.objects.filter(pk__in=[1])
            urlRedirect = "questionsRules:chemicals"
            self.question = question
            self.urlRedirect = urlRedirect
            return self.question, self.urlRedirect
        
        @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('No') , question8=L('No') | L('Si'), question9=L('No') | L('Si'), question10=L('No') | L('Si')))
        def GorgojoQuestionFor_2(self):
            question = Question.objects.filter(pk__in=[1])
            urlRedirect = "questionsRules:ditches"
            self.question = question
            self.urlRedirect = urlRedirect
            return self.question, self.urlRedirect
        
        @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('No') , question9=L('No') | L('Si'), question10=L('No') | L('Si')))
        def GorgojoQuestionFor_3(self):
            question = Question.objects.filter(pk__in=[1])
            urlRedirect = "questionsRules:plantOtherVegetables"
            self.question = question
            self.urlRedirect = urlRedirect
            return self.question, self.urlRedirect
        
        @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('No'), question10=L('No') | L('Si')))
        def GorgojoQuestionFor_4(self):
            question = Question.objects.filter(pk__in=[1])
            urlRedirect = "questionsRules:plantPickUp"
            self.question = question
            self.urlRedirect = urlRedirect
            return self.question, self.urlRedirect
        
        @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('Si'), question10=L('No')))
        def GorgojoQuestionFor_5(self):
            question = Question.objects.filter(pk__in=[1])
            urlRedirect = "questionsRules:traps"
            self.question = question
            self.urlRedirect = urlRedirect
            return self.question, self.urlRedirect
        
        @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('Si'), question10=L('Si')))
        def GorgojoQuestionFor_6(self):
            question = Question.objects.filter(pk__in=[1])
            urlRedirect = "questionsRules:continueStageChoice"
            self.question = question
            self.urlRedirect = urlRedirect
            return self.question, self.urlRedirect
    
    
    def test_return_fact_gorgojo_questionFive_value(self):
        """
        Test For Fact = GorgojoQuestionTwo
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
        """
        pass
    
    
    def test_return_fact_gorgojo_questionSix_value(self):
        """
        Test For Fact = GorgojoQuestionTwo
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
        """
        pass
    
    
    def test_return_fact_gorgojo_questionSeven_value(self):
        """
        Test For Fact = GorgojoQuestionTwo
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
        """
        pass
    
    
    def test_return_fact_gorgojo_questionEigth_value(self):
        """
        Test For Fact = GorgojoQuestionTwo
        
        Verification return to rules if the response is equals to expected

        Returns:
            QuerySet: returned queryset with the question five.
            String : returned to string per url
        """
        pass

def Create_Question(question_text):
    """Question cretion for unit test"""
    return Question.objects.create(question_text=question_text, pub_date= timezone.now())