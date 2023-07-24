from experta import KnowledgeEngine,Rule,Fact, AS, L

from .models import Question, Lottery
import random
class QuestionList(Fact):
    """Obtendra un valor questionId para determinar cual sera la lista de preguntas
        que debe devolver para que el usuario responda"""
    pass


class RandomList(Fact):
    """Obtendra un valor questionId para determinar cual sera la lista de preguntas
        que debe devolver para que el usuario responda"""
    pass

class GorgojoLottery123(Fact):
    pass

class GorgojoLottery124(Fact):
    pass

class GorgojoLottery125(Fact):
    pass

class GorgojoLottery126(Fact):
    pass

class GorgojoLottery134(Fact):
    pass

class GorgojoLottery135(Fact):
    pass

class GorgojoLottery136(Fact):
    pass

class GorgojoLottery145(Fact):
    pass

class GorgojoLottery146(Fact):
    pass

class GorgojoLottery156(Fact):
    pass

class GorgojoLottery234(Fact):
    pass

class GorgojoLottery235(Fact):
    pass

class GorgojoLottery236(Fact):
    pass

class GorgojoLottery245(Fact):
    pass

class GorgojoLottery246(Fact):
    pass

class GorgojoLottery256(Fact):
    pass

class GorgojoLottery345(Fact):
    pass

class GorgojoLottery346(Fact):
    pass

class GorgojoLottery356(Fact):
    pass

class GorgojoLottery456(Fact):
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


class GorgojoQuestionSix(Fact):
    pass


class GorgojoQuestionSeven(Fact):
    pass


class GorgojoQuestionEight(Fact):
    pass


class integrateHanlingLottery(KnowledgeEngine):
    questionL = 123
    question = Lottery.objects.filter(pk__in=[1])
    urlRedirect = "qustionsRules:lotteryrules"
    sugesstion = ""
    listQuestionL = Lottery.objects.filter(pk__in=[1])
    imageL = ""
    
    @Rule(AS.randomList << RandomList(questionId=L(1)))
    def QuestionList_One(self):
        a = random.randrange(1, 6, 1)
        b = random.randrange(1, 6, 1)
        c = random.randrange(1, 6, 1)
        
        while(b==a):
            b = random.randrange(1, 6, 1)
            
        while((c==b) or (c==a)):
            c = random.randrange(1, 6, 1)
        
        if a<b:  # 3<1
            if a <c:  #3<2
                if b<c:
                    respLottery = a*100+b*10+c
                else:
                    respLottery = a*100+c*10+b
            else:
                respLottery = c*100+a*10+b
        else:
            if a<c: #3<2
                respLottery = b*100+a*10+c
            else:
                if b<c: # 1 2
                    respLottery = b*100+c*10+a
                else:
                    respLottery = c*100+b*10+a
                

                   
        questionResult = [a,b,c]
        
        #respLottery= "".join(map(str,questionResult))
        questionL =  int(respLottery) 
        listQuestion = Lottery.objects.filter(pk__in=questionResult)
        self.listQuestion = listQuestion
        self.questionL = questionL
        return self.listQuestion, self.questionL
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery123(question1='No',question2='Hongo blanco',question3='Usar insecticida peligroso'))
    def GorgojoLottery123_1(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='No',question2='Hongo blanco',question3='Correr y gritar'))
    def GorgojoLottery123_2(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='No',question2='Hongo blanco',question3='Adelantar la Cosecha'))
    def GorgojoLottery123_3(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='No',question2='Hongo negro',question3='Usar insecticida peligroso'))
    def GorgojoLottery123_4(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='No',question2='Hongo negro',question3='Correr y gritar'))
    def GorgojoLottery123_5(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='No',question2='Hongo negro',question3='Adelantar la Cosecha'))
    def GorgojoLottery123_6(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='Si',question2='Hongo blanco',question3='Usar insecticida peligroso'))
    def GorgojoLottery123_7(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='Si',question2='Hongo blanco',question3='Correr y gritar'))
    def GorgojoLottery123_8(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='Si',question2='Hongo blanco',question3='Adelantar la Cosecha'))
    def GorgojoLottery123_9(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='Si',question2='Hongo negro',question3='Usar insecticida peligroso'))
    def GorgojoLottery123_10(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='Si',question2='Hongo negro',question3='Correr y gritar'))
    def GorgojoLottery123_11(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery123(question1='Si',question2='Hongo negro',question3='Adelantar la Cosecha'))
    def GorgojoLottery123_12(self):
        question = 123
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery124(question1='No',question2='Hongo negro',question4='No'))
    def GorgojoLottery124_1(self):
        question = 124
        urlRedirect = "questionsRules:Prueba"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery124(question1='No',question2='Hongo negro',question4='Si'))
    def GorgojoLottery124_2(self):
        question = 124
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery124(question1='No',question2='Hongo blanco',question4='Si'))
    def GorgojoLottery124_3(self):
        question = 124
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery124(question1='No',question2='Hongo blanco',question4='No'))
    def GorgojoLottery124_4(self):
        question = 124
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery124(question1='Si',question2='Hongo negro',question4='No'))
    def GorgojoLottery124_5(self):
        question = 124
        urlRedirect = "questionsRules:Prueba"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery124(question1='Si',question2='Hongo negro',question4='Si'))
    def GorgojoLottery124_6(self):
        question = 124
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery124(question1='Si',question2='Hongo blanco',question4='Si'))
    def GorgojoLottery124_7(self):
        question = 124
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery124(question1='Si',question2='Hongo blanco',question4='No'))
    def GorgojoLottery124_8(self):
        question = 124
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery125(question1='No',question2='Hongo negro',question5='No'))
    def GorgojoLottery125_1(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery125(question1='No',question2='Hongo negro',question5='Si'))
    def GorgojoLottery125_2(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery125(question1='No',question2='Hongo blanco',question5='Si'))
    def GorgojoLottery125_3(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery125(question1='No',question2='Hongo blanco',question5='No'))
    def GorgojoLottery125_4(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery125(question1='Si',question2='Hongo negro',question5='No'))
    def GorgojoLottery125_5(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery125(question1='Si',question2='Hongo negro',question5='Si'))
    def GorgojoLottery125_6(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery125(question1='Si',question2='Hongo blanco',question5='Si'))
    def GorgojoLottery125_7(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery125(question1='Si',question2='Hongo blanco',question5='No'))
    def GorgojoLottery125_8(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery126(question1='Si',question2='Hongo blanco',question6='Amontonar en el piso'))
    def GorgojoLottery126_1(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='Si',question2='Hongo blanco',question6='Llevar directo al almacen'))
    def GorgojoLottery126_2(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='Si',question2='Hongo blanco',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery126_3(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='Si',question2='Hongo negro',question6='Amontonar en el piso'))
    def GorgojoLottery126_4(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='Si',question2='Hongo negro',question6='Llevar directo al almacen'))
    def GorgojoLottery126_5(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='Si',question2='Hongo negro',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery126_6(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='No',question2='Hongo blanco',question6='Amontonar en el piso'))
    def GorgojoLottery126_7(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='No',question2='Hongo blanco',question6='Llevar directo al almacen'))
    def GorgojoLottery126_8(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='No',question2='Hongo blanco',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery126_9(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='No',question2='Hongo negro',question6='Amontonar en el piso'))
    def GorgojoLottery126_10(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='No',question2='Hongo negro',question6='Llevar directo al almacen'))
    def GorgojoLottery126_11(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery126(question1='No',question2='Hongo negro',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery126_12(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery134(question1='Si',question3='Usar insecticida peligroso',question4='No'))
    def GorgojoLottery134_1(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='Si',question3='Usar insecticida peligroso',question4='Si'))
    def GorgojoLottery134_2(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='Si',question3='Correr y gritar',question4='Si'))
    def GorgojoLottery134_3(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='Si',question3='Correr y gritar',question4='No'))
    def GorgojoLottery134_4(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='Si',question3='Adelantar la Cosecha',question4='No'))
    def GorgojoLottery134_5(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='Si',question3='Adelantar la Cosecha',question4='Si'))
    def GorgojoLottery134_6(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='No',question3='Usar insecticida peligroso',question4='No'))
    def GorgojoLottery134_7(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='No',question3='Usar insecticida peligroso',question4='Si'))
    def GorgojoLottery134_8(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='No',question3='Correr y gritar',question4='Si'))
    def GorgojoLottery134_9(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='No',question3='Correr y gritar',question4='No'))
    def GorgojoLottery134_10(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery134(question1='No',question3='Adelantar la Cosecha',question4='No'))
    def GorgojoLottery134_11(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe conocer mejor al Gorgojo de Los Andes para que asi tenga un mayor entendimiento del mismo, ya que conociendo a la plaga se hace mejor el entendimienot de como combatir contra el, el gorgojo como todo ser vivo tiene un ciclo si se llegara a reproducir, toda nuestra cosecha corre un gran riesgo, para evitar esto realizaremos una gran vigilancia a nuestro cultivo, podemos hacer varias cosas como rondar alrededor de la parcela para ver las hojas de nuestro cultivo ya que estas para los adultos es su principal alimento. \n Si se ha de Adelantar la cosecha se debe hacer con sumo cuidado, es una gran opcion siempre y cuando estuviese cerca del cultivo ya que si se hace de manera prematura esto puede afectar enormenente su cultivo, sino puede realizar una recoleccion de gorgojos adultos. \n Es necesario siempre colocar trampas en nuestro cultivo, ya que estas ayudaran enormenete a que la plaga no llegue facilmente a nuestro cultivo, existen muchas trampas caseras que podria realizar desde botellas plasticas a la mitas con poca agua alrededor de la parcela hasta zanjas profundas con naylon negro"
        return self.question, self.urlRedirect, self.sugesstion
    
    @Rule(GorgojoLottery134(question1='No',question3='Adelantar la Cosecha',question4='Si'))
    def GorgojoLottery134_12(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery135(question1='Si',question3='Usar insecticida peligroso',question5='No'))
    def GorgojoLottery135_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='Si',question3='Usar insecticida peligroso',question5='Si'))
    def GorgojoLottery135_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='Si',question3='Correr y gritar',question5='Si'))
    def GorgojoLottery135_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='Si',question3='Correr y gritar',question5='No'))
    def GorgojoLottery135_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='Si',question3='Adelantar la Cosecha',question5='No'))
    def GorgojoLottery135_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='Si',question3='Adelantar la Cosecha',question5='Si'))
    def GorgojoLottery135_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='No',question3='Usar insecticida peligroso',question5='No'))
    def GorgojoLottery135_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='No',question3='Usar insecticida peligroso',question5='Si'))
    def GorgojoLottery135_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='No',question3='Correr y gritar',question5='Si'))
    def GorgojoLottery135_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='No',question3='Correr y gritar',question5='No'))
    def GorgojoLottery135_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='No',question3='Adelantar la Cosecha',question5='No'))
    def GorgojoLottery135_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery135(question1='No',question3='Adelantar la Cosecha',question5='Si'))
    def GorgojoLottery135_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery136(question1='Si',question3='Usar insecticida peligroso',question6='Amontonar en el piso'))
    def GorgojoLottery136_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='Si',question3='Usar insecticida peligroso',question6='Llevar directo al almacen'))
    def GorgojoLottery136_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='Si',question3='Usar insecticida peligroso',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery136_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='Si',question3='Correr y gritar',question6='Amontonar en el piso'))
    def GorgojoLottery136_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='Si',question3='Correr y gritar',question6='Llevar directo al almacen'))
    def GorgojoLottery136_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='Si',question3='Correr y gritar',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery136_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='Si',question3='Adelantar la Cosecha',question6='Amontonar en el piso'))
    def GorgojoLottery136_7(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='Si',question3='Adelantar la Cosecha',question6='Llevar directo al almacen'))
    def GorgojoLottery136_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='Si',question3='Adelantar la Cosecha',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery136_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Usar insecticida peligroso',question6='Amontonar en el piso'))
    def GorgojoLottery136_10(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Usar insecticida peligroso',question6='Llevar directo al almacen'))
    def GorgojoLottery136_11(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Usar insecticida peligroso',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery136_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Correr y gritar',question6='Amontonar en el piso'))
    def GorgojoLottery136_13(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Correr y gritar',question6='Llevar directo al almacen'))
    def GorgojoLottery136_14(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Correr y gritar',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery136_15(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Adelantar la Cosecha',question6='Amontonar en el piso'))
    def GorgojoLottery136_16(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Adelantar la Cosecha',question6='Llevar directo al almacen'))
    def GorgojoLottery136_17(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery136(question1='No',question3='Adelantar la Cosecha',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery136_18(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery145(question1='No',question4='No',question5='No'))
    def GorgojoLottery145_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery145(question1='No',question4='No',question5='Si'))
    def GorgojoLottery145_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery145(question1='No',question4='Si',question5='Si'))
    def GorgojoLottery145_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery145(question1='No',question4='Si',question5='No'))
    def GorgojoLottery145_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery145(question1='Si',question4='No',question5='No'))
    def GorgojoLottery145_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery145(question1='Si',question4='No',question5='Si'))
    def GorgojoLottery145_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery145(question1='Si',question4='Si',question5='Si'))
    def GorgojoLottery145_7(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery145(question1='Si',question4='Si',question5='No'))
    def GorgojoLottery145_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect   
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery146(question1='No',question4='No',question6='Amontonar en el piso'))
    def GorgojoLottery146_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='No',question4='No',question6='Llevar directo al almacen'))
    def GorgojoLottery146_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='No',question4='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery146_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='No',question4='Si',question6='Amontonar en el piso'))
    def GorgojoLottery146_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='No',question4='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery146_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='No',question4='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery146_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='Si',question4='No',question6='Amontonar en el piso'))
    def GorgojoLottery146_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='Si',question4='No',question6='Llevar directo al almacen'))
    def GorgojoLottery146_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='Si',question4='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery146_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='Si',question4='Si',question6='Amontonar en el piso'))
    def GorgojoLottery146_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='Si',question4='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery146_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery146(question1='Si',question4='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery146_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery156(question1='No',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery156_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='No',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery156_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='No',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery156_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='No',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery156_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='No',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery156_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='No',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery156_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='Si',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery156_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='Si',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery156_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='Si',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery156_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='Si',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery156_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='Si',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery156_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery156(question1='Si',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery156_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect  
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery234(question2='Hongo negro',question3='Usar insecticida peligroso',question4='No'))
    def GorgojoLottery234_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo negro',question3='Usar insecticida peligroso',question4='Si'))
    def GorgojoLottery234_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo negro',question3='Correr y gritar',question4='Si'))
    def GorgojoLottery234_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo negro',question3='Correr y gritar',question4='No'))
    def GorgojoLottery234_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo negro',question3='Adelantar la Cosecha',question4='No'))
    def GorgojoLottery234_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo negro',question3='Adelantar la Cosecha',question4='Si'))
    def GorgojoLottery234_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo blanco',question3='Usar insecticida peligroso',question4='No'))
    def GorgojoLottery234_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo blanco',question3='Usar insecticida peligroso',question4='Si'))
    def GorgojoLottery234_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo blanco',question3='Correr y gritar',question4='Si'))
    def GorgojoLottery234_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo blanco',question3='Correr y gritar',question4='No'))
    def GorgojoLottery234_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo blanco',question3='Adelantar la Cosecha',question4='No'))
    def GorgojoLottery234_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery234(question2='Hongo blanco',question3='Adelantar la Cosecha',question4='Si'))
    def GorgojoLottery234_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery235(question2='Hongo negro',question3='Usar insecticida peligroso',question5='No'))
    def GorgojoLottery235_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo negro',question3='Usar insecticida peligroso',question5='Si'))
    def GorgojoLottery235_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo negro',question3='Correr y gritar',question5='Si'))
    def GorgojoLottery235_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo negro',question3='Correr y gritar',question5='No'))
    def GorgojoLottery235_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo negro',question3='Adelantar la Cosecha',question5='No'))
    def GorgojoLottery235_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo negro',question3='Adelantar la Cosecha',question5='Si'))
    def GorgojoLottery235_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo blanco',question3='Usar insecticida peligroso',question5='No'))
    def GorgojoLottery235_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo blanco',question3='Usar insecticida peligroso',question5='Si'))
    def GorgojoLottery235_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo blanco',question3='Correr y gritar',question5='Si'))
    def GorgojoLottery235_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo blanco',question3='Correr y gritar',question5='No'))
    def GorgojoLottery235_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo blanco',question3='Adelantar la Cosecha',question5='No'))
    def GorgojoLottery235_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery235(question2='Hongo blanco',question3='Adelantar la Cosecha',question5='Si'))
    def GorgojoLottery235_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect 
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Usar insecticida peligroso',question6='Amontonar en el piso'))
    def GorgojoLottery236_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Usar insecticida peligroso',question6='Llevar directo al almacen'))
    def GorgojoLottery236_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Usar insecticida peligroso',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery236_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Correr y gritar',question6='Amontonar en el piso'))
    def GorgojoLottery236_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Correr y gritar',question6='Llevar directo al almacen'))
    def GorgojoLottery236_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Correr y gritar',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery236_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Adelantar la Cosecha',question6='Amontonar en el piso'))
    def GorgojoLottery236_7(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Adelantar la Cosecha',question6='Llevar directo al almacen'))
    def GorgojoLottery236_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo blanco',question3='Adelantar la Cosecha',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery236_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Usar insecticida peligroso',question6='Amontonar en el piso'))
    def GorgojoLottery236_10(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Usar insecticida peligroso',question6='Llevar directo al almacen'))
    def GorgojoLottery236_11(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Usar insecticida peligroso',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery236_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Correr y gritar',question6='Amontonar en el piso'))
    def GorgojoLottery236_13(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Correr y gritar',question6='Llevar directo al almacen'))
    def GorgojoLottery236_14(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Correr y gritar',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery236_15(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Adelantar la Cosecha',question6='Amontonar en el piso'))
    def GorgojoLottery236_16(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Adelantar la Cosecha',question6='Llevar directo al almacen'))
    def GorgojoLottery236_17(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery236(question2='Hongo negro',question3='Adelantar la Cosecha',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery236_18(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect 
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery245(question2='Hongo negro',question4='No',question5='No'))
    def GorgojoLottery245_1(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery245(question2='Hongo negro',question4='No',question5='Si'))
    def GorgojoLottery245_2(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery245(question2='Hongo negro',question4='Si',question5='Si'))
    def GorgojoLottery245_3(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery245(question2='Hongo negro',question4='Si',question5='No'))
    def GorgojoLottery245_4(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery245(question2='Hongo blanco',question4='No',question5='No'))
    def GorgojoLottery245_5(self):
        urlRedirect = "questionsRules:Prueba"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery245(question2='Hongo blanco',question4='No',question5='Si'))
    def GorgojoLottery245_6(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = "El hongo blanco es la mejor eleccion para proteger la papa en su almacen o lugar donde amontono la papa, debido que este hongo cumple la funcion de adelantar el ciclo de vida del gorgojo de los Andes. \n En el cultivo de papa es necesario colocar trampas debido que con su ayuda podremos evitar que el gorgojo ingrese con facilidad a nuestro cultivo, algunas trampas que podria realizar son poniendo alrededor de la parcela botellas de plastico a la mitad con poca agua o piedras grandes planas humedas para que asi en el dia los gorgojos se aproximen a ellas, tambien zanjas o trampas mas letales son de gran ayuda para proteger nuestro cultivo. \n Tiene toda la razon, se puede poner cualquier tipo de otro cultivo alrededor de nuestro cultivo de papa, ademas que nos proporciona una barrera vegetal para proteger nuestra papa, para esto procuramos sembrar productos que tengan plantas grandes y gruesas con el fin de evitar que el gorgojo pase con facilidad a nuestra parcela de papa, algunas plantas pueden ser la Cebolla, Cebada, etc."
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery245(question2='Hongo blanco',question4='Si',question5='Si'))
    def GorgojoLottery245_7(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery245(question2='Hongo blanco',question4='Si',question5='No'))
    def GorgojoLottery245_8(self):
        urlRedirect = "questionsRules:Prueba"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect 
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery246(question2='Hongo negro',question4='No',question6='Amontonar en el piso'))
    def GorgojoLottery246_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo negro',question4='Si',question6='Amontonar en el piso'))
    def GorgojoLottery246_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo negro',question4='No',question6='Llevar directo al almacen'))
    def GorgojoLottery246_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo negro',question4='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery246_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo negro',question4='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery246_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo negro',question4='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery246_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo blanco',question4='No',question6='Amontonar en el piso'))
    def GorgojoLottery246_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo blanco',question4='Si',question6='Amontonar en el piso'))
    def GorgojoLottery246_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo blanco',question4='No',question6='Llevar directo al almacen'))
    def GorgojoLottery246_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo blanco',question4='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery246_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo blanco',question4='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery246_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery246(question2='Hongo blanco',question4='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery246_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery256(question2='Hongo negro',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery256_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo negro',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery256_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo negro',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery256_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo negro',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery256_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo negro',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery256_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo negro',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery256_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo blanco',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery256_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo blanco',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery256_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo blanco',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery256_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo blanco',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery256_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo blanco',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery256_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery256(question2='Hongo blanco',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery256_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery345(question3='Usar insecticida peligroso',question4='No',question5='No'))
    def GorgojoLottery345_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Usar insecticida peligroso',question4='No',question5='Si'))
    def GorgojoLottery345_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Usar insecticida peligroso',question4='Si',question5='No'))
    def GorgojoLottery345_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Usar insecticida peligroso',question4='Si',question5='Si'))
    def GorgojoLottery345_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Correr y gritar',question4='No',question5='No'))
    def GorgojoLottery345_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Correr y gritar',question4='No',question5='Si'))
    def GorgojoLottery345_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Correr y gritar',question4='Si',question5='Si'))
    def GorgojoLottery345_7(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Correr y gritar',question4='Si',question5='No'))
    def GorgojoLottery345_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Adelantar la Cosecha',question4='No',question5='No'))
    def GorgojoLottery345_9(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Adelantar la Cosecha',question4='No',question5='Si'))
    def GorgojoLottery345_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Adelantar la Cosecha',question4='Si',question5='Si'))
    def GorgojoLottery345_11(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery345(question3='Adelantar la Cosecha',question4='Si',question5='No'))
    def GorgojoLottery345_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect 
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery346(question3='Usar insecticida peligroso',question4='No',question6='Amontonar en el piso'))
    def GorgojoLottery346_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Usar insecticida peligroso',question4='Si',question6='Amontonar en el piso'))
    def GorgojoLottery346_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Usar insecticida peligroso',question4='No',question6='Llevar directo al almacen'))
    def GorgojoLottery346_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Usar insecticida peligroso',question4='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery346_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Usar insecticida peligroso',question4='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery346_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Usar insecticida peligroso',question4='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery346_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Correr y gritar',question4='No',question6='Amontonar en el piso'))
    def GorgojoLottery346_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Correr y gritar',question4='Si',question6='Amontonar en el piso'))
    def GorgojoLottery346_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Correr y gritar',question4='No',question6='Llevar directo al almacen'))
    def GorgojoLottery346_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Correr y gritar',question4='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery346_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Correr y gritar',question4='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery346_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Correr y gritar',question4='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery346_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Adelantar la Cosecha',question4='No',question6='Amontonar en el piso'))
    def GorgojoLottery346_13(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Adelantar la Cosecha',question4='Si',question6='Amontonar en el piso'))
    def GorgojoLottery346_14(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Adelantar la Cosecha',question4='No',question6='Llevar directo al almacen'))
    def GorgojoLottery346_15(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Adelantar la Cosecha',question4='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery346_16(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Adelantar la Cosecha',question4='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery346_17(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery346(question3='Adelantar la Cosecha',question4='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery346_18(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery356(question3='Usar insecticida peligroso',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery356_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Usar insecticida peligroso',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery356_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Usar insecticida peligroso',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery356_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Usar insecticida peligroso',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery356_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Usar insecticida peligroso',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery356_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Usar insecticida peligroso',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery356_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Correr y gritar',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery356_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Correr y gritar',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery356_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Correr y gritar',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery356_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Correr y gritar',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery356_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Correr y gritar',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery356_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Correr y gritar',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery356_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Adelantar la Cosecha',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery356_13(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Adelantar la Cosecha',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery356_14(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Adelantar la Cosecha',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery356_15(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Adelantar la Cosecha',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery356_16(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Adelantar la Cosecha',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery356_17(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery356(question3='Adelantar la Cosecha',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery356_18(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect 
    
    """_summary_
    Gordojo Lottery:
    Lanzado para la seccion de reglas y respuestas
    
    Args:
        Fact (questionX, questionY, questionZ): Son las respuestas del usuario lo cual determinara
        que vista debe ser lanzada para que el usuario pueda seguirlo
    """
    
    @Rule(GorgojoLottery456(question4='No',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery456_1(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='No',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery456_2(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='No',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery456_3(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='No',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery456_4(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='No',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery456_5(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='No',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery456_6(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='Si',question5='No',question6='Amontonar en el piso'))
    def GorgojoLottery456_7(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='Si',question5='Si',question6='Amontonar en el piso'))
    def GorgojoLottery456_8(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='Si',question5='No',question6='Llevar directo al almacen'))
    def GorgojoLottery456_9(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='Si',question5='Si',question6='Llevar directo al almacen'))
    def GorgojoLottery456_10(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='Si',question5='No',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery456_11(self):
        urlRedirect = "questionsRules:chemicals"
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(GorgojoLottery456(question4='Si',question5='Si',question6='Recolectarlo encima de una sabana(aguayo)'))
    def GorgojoLottery456_12(self):
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect 
    
    

class integratedHandling(KnowledgeEngine):
    question = Question.objects.filter(pk__in=[1])
    urlRedirect = "questionsRules:rules"
    sugesstion = "NA"
    listQuestion = Question.objects.filter(pk__in=[0])
    
    @Rule(AS.questionList << QuestionList(questionId=L(1) | L(2)))
    def QuestionList_One(self):
        listQuestion = Question.objects.filter(pk__in=[1,2])
        self.listQuestion = listQuestion
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
        question = Question.objects.filter(pk__in=[3])
        urlRedirect = "questionsRules:rules"
        self.sugesstion = ""
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect

    @Rule(GorgojoQuestion(question1='Si',question2='Si'))
    def GorgojoQuestion_rule2(self):
        question = Question.objects.filter(pk__in=[3])
        urlRedirect = "questionsRules:goodPractices"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Saber mas sobre buenas practicas, el descanso del suelo donde no es recomendable que todos los años cultive papa debido a que la tierra debe descansar, la barrera vegetal donde las plantas de Oca y Cebada son las mejores para proteger su cultivo"
        return self.question, self.urlRedirect

    @Rule(GorgojoQuestion(question1='No',question2='No'))
    def GorgojoQuestion_rule3(self):
        question = Question.objects.filter(pk__in=[3])
        urlRedirect = "questionsRules:gorgojoInformation"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Saber mas sobre la plaga del Gorgojo, sus 4 etapas donde la etapa de Larva es mas vulnerable de esta plaga"
        return self.question, self.urlRedirect
        

    @Rule(GorgojoQuestion(question1='No',question2='Si'))
    def GorgojoQuestion_rule4(self):
        question = Question.objects.filter(pk__in=[3])
        urlRedirect = "questionsRules:gorgojoInformationAndGoodPractice"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Saber mas sobre la plaga del Gorgojo, sus 4 etapas y en qué la etapa de larva es mas vulnerable; Además de saber buenas prácticas como barrera vegetal con plantas de Cebada y Oca alrededor de su parcela, etc."
        return self.question, self.urlRedirect
        
    @Rule(AS.gorgojoQuestionTwo << GorgojoQuestionTwo(question3=L('Si') | L('No'), question4=L('No')))
    def seen_numberFive(self):
        question = Question.objects.filter(pk__in=[5])
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = ""
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionTwo << GorgojoQuestionTwo(question3=L('No') | L('Si'), question4=L('Si')))
    def seen_numberSix(self):
        question = Question.objects.filter(pk__in=[5])
        urlRedirect = "questionsRules:preventiveMeasures"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Saber las medidas preventivas para evitar que la plaga vuelva a dañar su cultivo de papa, usando algunos insecticidas orgánicos e inorgánicos."
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Recién planeo empezar mi cultivo'))
    def GorgojoQuestionThree_1(self):
        question = Question.objects.filter(pk__in=[6])
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Acabo de sembrar'))
    def GorgojoQuestionThree_2(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Mi cultivo de papa, ya esta más de la mitad'))
    def GorgojoQuestionThree_3(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Estoy por cosechar mi cultivo'))
    def GorgojoQuestionThree_4(self):
        question = Question.objects.filter(pk__in=[18])
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
    @Rule(GorgojoQuestionThree(resp='Acabo de cosechar mi cultivo'))
    def GorgojoQuestionThree_5(self):
        question = Question.objects.filter(pk__in=[19])
        urlRedirect = "questionsRules:rules"
        self.question = question
        self.urlRedirect = urlRedirect
        return self.question, self.urlRedirect
    
        
    # @Rule(GorgojoQuestionFor(question6='no', question7='no' , question8 =question8, question9 = question9, question10= question10))
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('No'), question7=L('No') | L('Si'), question8=L('No') | L('Si'), question9=L('No') | L('Si'), question10=L('No') | L('Si')))
    def GorgojoQuestionFor_1(self):
        question = Question.objects.filter(pk__in=[6])
        urlRedirect = "questionsRules:chemicals"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('No') , question8=L('No') | L('Si'), question9=L('No') | L('Si'), question10=L('No') | L('Si')))
    def GorgojoQuestionFor_2(self):
        question = Question.objects.filter(pk__in=[6])
        urlRedirect = "questionsRules:ditches"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Realizar una zanja podria ser demasiado sencillo para muchos, pero debe saber la profundidad y anchura de la misma, ademas de que la zanja podría ser una gran trampa si se le revistiese con plástico negro."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('No') , question9=L('No') | L('Si'), question10=L('No') | L('Si')))
    def GorgojoQuestionFor_3(self):
        question = Question.objects.filter(pk__in=[6])
        urlRedirect = "questionsRules:plantOtherVegetables"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "¿Sabia usted que puede cultivar otras plantas vegetales para proteger su cultivo?, las plantas como el Tarwi, Oca, Cebada o Cebolla son una gran barrera para su cultivo de papa."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('No'), question10=L('No') | L('Si')))
    def GorgojoQuestionFor_4(self):
        question = Question.objects.filter(pk__in=[6])
        urlRedirect = "questionsRules:plantPickUp"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Si anteriormente se realizo un cultivo en el mismo lugar donde esta cultivando actualmente, entonces asegurese de recoger las plantas voluntarias o K'ipas dado que ahi es donde la plaga del gorgojo de Los Andes deja huevos, etc."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('Si'), question10=L('No')))
    def GorgojoQuestionFor_5(self):
        question = Question.objects.filter(pk__in=[6])
        urlRedirect = "questionsRules:traps"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe aprender a realizar trampas para poder minorizar el ingreso de la plaga a su cultivo, existen muchos tipos de trampas caseras las mas recomendadas son: revestir la zanja con plástico negro, usar piedras planas y botella de plástico."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFor << GorgojoQuestionFor(question6=L('Si'), question7=L('Si') , question8=L('Si'), question9=L('Si'), question10=L('Si')))
    def GorgojoQuestionFor_6(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = ""
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question14=L('No'), question12=L('Si') | L('No'), question13=L('Si') | L('No'), question8=L('Si') | L('No'), question11=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_1(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:gorgojoMeasures"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Dado que detecto a la plaga del Gorgojo de Los Andes, se le recomienda es estar en alerta poner trampar alrededor de su cultivo, ir a las primeras plantas alrededor de su parcela y verificar las hojas de las plantas donde ahi se ve si el Gorgojo se alimento o no, buscar en lugares húmedos cerca de la parcela, dado que ahi es donde se esconde la plaga."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question14=L('Si'), question12=L('No'), question13=L('Si') | L('No'), question8=L('Si') | L('No'), question11=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_2(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:ditches"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Realizar una zanja podria ser demasiado sencillo para muchos, pero debe saber la profundidad y anchura de la misma, ademas de que la zanja podría ser una gran trampa si se le revistiese con plástico negro."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question14=L('Si'), question12=L('Si'), question13=L('No'), question8=L('Si') | L('No'), question11=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_3(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:culturalWork"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Es necesario realizar un buen aporque, no solo para que la planta crezca bien sino porque el aporque protege de gran manera a la planta de la papa de muchas plagas especialmente del Gorgojo de Los Andes."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question14=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('No'), question11=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_4(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:plantOtherVegetables"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "¿Sabia usted que puede cultivar otras plantas vegetales para proteger su cultivo?, las plantas como el Tarwi, Oca, Cebada o Cebolla son una gran barrera para su cultivo de papa."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question14=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question11=L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_5(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:chemicals"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question14=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question11=L('Si'), question10=L('No')))
    def GorgojoQuestionFive_6(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:traps"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe aprender a realizar trampas para poder minorizar el ingreso de la plaga a su cultivo, existen muchos tipos de trampas caseras las mas recomendadas son: revestir la zanja con plástico negro, usar piedras planas y botella de plástico"
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question14=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question11=L('Si'), question10=L('Si')))
    def GorgojoQuestionFive_7(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = ""
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('No'), question14=L('Si') | L('No'), question13=L('Si') | L('No'), question12=L('Si') | L('No'), question15=L('Si') | L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_1(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:countherTheGorgojo"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Dado que descubrió en su cultivo a la plaga, no se alarme lo mas recomendable es estar tranquilo y analizar dos puntos que podría realizar, uno es adelantar la cosecha en caso este muy cerca la temporada con esto reduciremos el riesgo de que afecte en gran medidad a nuestro cultivo, si no podemos adelantar la cosecha entonces el segundo punto seria de usar un menor proporcion químicos que ya se vieron anteriormente y los que conoce, tambien de seguir recolectando la plaga con mayor intensidad al igual que las trampas alrededor de la misma. "
        return self.question, self.urlRedirect
        
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question14=L('No'), question13=L('Si') | L('No'), question12=L('Si') | L('No'), question15=L('Si') | L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_2(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:gorgojoMeasures"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Dado que detecto a la plaga del Gorgojo de Los Andes, se le recomienda es estar en alerta poner trampar alrededor de su cultivo, ir a las primeras plantas alrededor de su parcela y verificar las hojas de las plantas donde ahi se ve si el Gorgojo se alimento o no, buscar en lugares húmedos cerca de la parcela, dado que ahi es donde se esconde la plaga."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question14=L('Si'), question13=L('No'), question12=L('Si') | L('No'), question15=L('Si') | L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_3(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:culturalWork"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = " El aporque trae grandes beneficios como mejora el riego para el cultivo, ademas ayuda a que la planta de papa crezca de manera recta y tambien es de gran ayuda para combatir a la plaga del Gorgojo de Los Andes, el aporque es la amontonar tierra alrededor de la planta de papa logrando asi todos los beneficios ya mencionados y mas."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question14=L('Si'), question13=L('Si'), question12=L('No'), question15=L('Si') | L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_4(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:ditches"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "La zanja es lo primero que deberia mejorar para que la plaga no dañe en gran proporción su cultivo, inclusive deberia volverlo una trampa mortal para la plaga revistiendola con plástico negro, con la anchura apropiada esta es una gran defensa contra el Gorgojo de Los Andes. "
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question14=L('Si'), question13=L('Si'), question12=L('Si'), question15=L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_5(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:traps"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Elaborar trampas siempre es un gran trabajo, o almenos eso es lo que la mayoria piensa, existen trampas caseras muy buenas y faciles de elaborar para poder combatir a la plaga del Gorgojo de Los Andes, como ser poner piedras planar alrededor de la parcelo o botellas de plástico para atraer a la plaga ahi."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question14=L('Si'), question13=L('Si'), question12=L('Si'), question15=L('Si'), question16=L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_6(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:gatherGorgojo"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe prácticar esta recolección ya sea visitando las trampas que puso en la parcela, viendo debajo de las plantas de papa o en lugares húmedos donde la plaga del Gorgojo se encuentren. "
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question14=L('Si'), question13=L('Si'), question12=L('Si'), question15=L('Si'), question16=L('Si'), question11=L('No')))
    def GorgojoQuestionSix_7(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:chemicals"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe saber que no todos los productos químicos son malos para su cultivo, existen productos químicos inorgánicos buenos para su cultivo como el Acaritop a su vez tener en cuenta que tambien puede elaborar productos químicos orgánicos con aji o ajo para proteger su cultivo."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question14=L('Si'), question13=L('Si'), question12=L('Si'), question15=L('Si'), question16=L('Si'), question11=L('Si')))
    def GorgojoQuestionSix_8(self):
        question = Question.objects.filter(pk__in=[18])
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = ""
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSeven << GorgojoQuestionSeven(question17=L('No'), question16=L('Si') | L('No'), question18= L('Si') | L('No')))
    def GorgojoQuestionSeven_1(self):
        question = Question.objects.filter(pk__in=[18])
        urlRedirect = "questionsRules:countherTheGorgojo"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Dado que descubrió en su cultivo a la plaga, no se alarme lo mas recomendable es estar tranquilo y analizar dos puntos que podría realizar, uno es adelantar la cosecha en caso este muy cerca la temporada con esto reduciremos el riesgo de que afecte en gran medidad a nuestro cultivo, si no podemos adelantar la cosecha entonces el segundo punto seria de usar un menor proporcion químicos que ya se vieron anteriormente y los que conoce, tambien de seguir recolectando la plaga con mayor intensidad al igual que las trampas alrededor de la misma. "
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSeven << GorgojoQuestionSeven(question17=L('Si'), question16=L('No'), question18= L('Si') | L('No')))
    def GorgojoQuestionSeven_2(self):
        question = Question.objects.filter(pk__in=[18])
        urlRedirect = "questionsRules:gatherGorgojo"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe prácticar esta recolección ya sea visitando las trampas que puso en la parcela, viendo debajo de las plantas de papa o en lugares húmedos donde la plaga del Gorgojo se encuentren. "
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSeven << GorgojoQuestionSeven(question17=L('Si'), question16=L('Si'), question18= L('No')))
    def GorgojoQuestionSeven_3(self):
        question = Question.objects.filter(pk__in=[18])
        urlRedirect = "questionsRules:potatoSelection"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "El saber donde recolectar la papa es muy importante, dado que si se toma a la ligera y se lo recolecta en el suelo, las larvas que estan en la papa podrian llegar a la tierra entrar a fondo y completar su ciclo de vida y a futuro ese lugar tener una gran cantidad de plaga, por eso se recomienda el recojo con algun mantel, etc. inclusive poner alrededor gallinas para que ellas eliminen a las larvas que se encuentren en la papa."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSeven << GorgojoQuestionSeven(question16=L('Si'), question17=L('Si'), question18= L('Si')))
    def GorgojoQuestionSeven_4(self):
        question = Question.objects.filter(pk__in=[19])
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion =""
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionEight << GorgojoQuestionEight(question19=L('No'), question20=L('Si') | L('No'), question21= L('Si') | L('No'), question22=L('Si') | L('No')))
    def GorgojoQuestionEight_1(self):
        question = Question.objects.filter(pk__in=[19])
        urlRedirect = "questionsRules:soilRemoval"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion ="El remover el suelo donde amontono la papa es de gran importancia, puede que apesar de poner la papa sobre el mantel y traer a las gallinar cerca, algunas larvas pudiesen aver ingresado a la tierra con el fin de completar su ciclo de vida y reproducirse aun mas en su cultivo, para eso debemos remover la tierra y asi evitar futuras reproducciones de la plaga. "
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionEight << GorgojoQuestionEight(question19=L('Si'), question20=L('No'), question21= L('Si') | L('No'), question22=L('Si') | L('No')))
    def GorgojoQuestionEight_2(self):
        question = Question.objects.filter(pk__in=[19])
        urlRedirect = "questionsRules:warehousePreparation"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion ="Sin duda la papa debe estar en algun lugar como ser un almacén, con el fin de estar mas aslvo de alguna plaga, pero no se confunda esto no hara que sea imposible que alguna plaga llegue ahi. Este alerta!!"
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionEight << GorgojoQuestionEight(question19=L('Si'), question20=L('Si'), question21= L('No'), question22=L('Si') | L('No')))
    def GorgojoQuestionEight_3(self):
        question = Question.objects.filter(pk__in=[19])
        urlRedirect = "questionsRules:dangerIntoWarehouse"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion ="El hecho de que pusiera la papa de su cultivo en algun almacén o lugar seguro no impide que la papa corra peligro es mas cuando la papa es muy vulnerable a la plaga del Gorgojo de Los Andes y debe tomar medidas necesarias para poder evitar que esta plaga llegue donde puso la papa. "
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionEight << GorgojoQuestionEight(question19=L('Si'), question20=L('Si'), question21= L('Si'), question22=L('No')))
    def GorgojoQuestionEight_4(self):
        question = Question.objects.filter(pk__in=[19])
        urlRedirect = "questionsRules:whiteFungus"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion ="La utilidad del hongo blando es cortar el ciclo de vida de la plaga del Gorgojo de Los Andes con el fin de evitar futuras poblaciones de la misma, y asi proteger nuestro cultivo de esta plaga, se recomienda poner el hongo blanco en el almacen o lugar donde amontonara la papa una semana antes para asi surja efecto y evite el ingreso del Gorgojo."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionEight << GorgojoQuestionEight(question19=L('Si'), question20=L('Si'), question21= L('Si'), question22=L('Si')))
    def GorgojoQuestionEight_5(self):
        question = Question.objects.filter(pk__in=[1])
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion =""
        return self.question, self.urlRedirect