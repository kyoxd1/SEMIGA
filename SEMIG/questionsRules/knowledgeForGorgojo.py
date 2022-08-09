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


class GorgojoQuestionSix(Fact):
    pass


class GorgojoQuestionSeven(Fact):
    pass


class GorgojoQuestionEight(Fact):
    pass


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
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('No'), question12=L('Si') | L('No'), question13=L('Si') | L('No'), question8=L('Si') | L('No'), question14=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_1(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:chemicals"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Conocer mejor los químicos para su cultivo, tanto los inorgánicos (Karate o Lambdacal) como los orgánicos (Aji, ajo y azufre en poca proporción)"
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('No'), question13=L('Si') | L('No'), question8=L('Si') | L('No'), question14=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_2(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:ditches"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Realizar una zanja podria ser demasiado sencillo para muchos, pero debe saber la profundidad y anchura de la misma, ademas de que la zanja podría ser una gran trampa si se le revistiese con plástico negro."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('No'), question8=L('Si') | L('No'), question14=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_3(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:culturalWork"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Es necesario realizar un buen aporque, no solo para que la planta crezca bien sino porque el aporque protege de gran manera a la planta de la papa de muchas plagas especialmente del Gorgojo de Los Andes."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('No'), question14=L('Si') | L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_4(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:plantOtherVegetables"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "¿Sabia usted que puede cultivar otras plantas vegetales para proteger su cultivo?, las plantas como el Tarwi, Oca, Cebada o Cebolla son una gran barrera para su cultivo de papa."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question14=L('No'), question10=L('Si') | L('No')))
    def GorgojoQuestionFive_5(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:gorgojoMeasures"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Dado que detecto a la plaga del Gorgojo de Los Andes, se le recomienda es estar en alerta poner trampar alrededor de su cultivo, ir a las primeras plantas alrededor de su parcela y verificar las hojas de las plantas donde ahi se ve si el Gorgojo se alimento o no, buscar en lugares húmedos cerca de la parcela, dado que ahi es donde se esconde la plaga."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question14=L('Si'), question10=L('No')))
    def GorgojoQuestionFive_6(self):
        question = Question.objects.filter(pk__in=[11])
        urlRedirect = "questionsRules:traps"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe aprender a realizar trampas para poder minorizar el ingreso de la plaga a su cultivo, existen muchos tipos de trampas caseras las mas recomendadas son: revestir la zanja con plástico negro, usar piedras planas y botella de plástico"
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionFive << GorgojoQuestionFive(question11=L('Si'), question12=L('Si'), question13=L('Si'), question8=L('Si'), question14=L('Si'), question10=L('Si')))
    def GorgojoQuestionFive_7(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:continueStageChoice"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = ""
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('No'), question12=L('Si') | L('No'), question13=L('Si') | L('No'), question14=L('Si') | L('No'), question15=L('Si') | L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_1(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:countherTheGorgojo"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Dado que descubrió en su cultivo a la plaga, no se alarme lo mas recomendable es estar tranquilo y analizar dos puntos que podría realizar, uno es adelantar la cosecha en caso este muy cerca la temporada con esto reduciremos el riesgo de que afecte en gran medidad a nuestro cultivo, si no podemos adelantar la cosecha entonces el segundo punto seria de usar un menor proporcion químicos que ya se vieron anteriormente y los que conoce, tambien de seguir recolectando la plaga con mayor intensidad al igual que las trampas alrededor de la misma. "
        return self.question, self.urlRedirect
        
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question12=L('No'), question13=L('Si') | L('No'), question14=L('Si') | L('No'), question15=L('Si') | L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_2(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:ditches"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "La zanja es lo primero que deberia mejorar para que la plaga no dañe en gran proporción su cultivo, inclusive deberia volverlo una trampa mortal para la plaga revistiendola con plástico negro, con la anchura apropiada esta es una gran defensa contra el Gorgojo de Los Andes. "
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question12=L('Si'), question13=L('No'), question14=L('Si') | L('No'), question15=L('Si') | L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_3(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:culturalWork"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = " El aporque trae grandes beneficios como mejora el riego para el cultivo, ademas ayuda a que la planta de papa crezca de manera recta y tambien es de gran ayuda para combatir a la plaga del Gorgojo de Los Andes, el aporque es la amontonar tierra alrededor de la planta de papa logrando asi todos los beneficios ya mencionados y mas."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question12=L('Si'), question13=L('Si'), question14=L('No'), question15=L('Si') | L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_4(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:gorgojoMeasures"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Dado que detecto a la plaga del Gorgojo de Los Andes, se le recomienda es estar en alerta poner trampar alrededor de su cultivo, ir a las primeras plantas alrededor de su parcela y verificar las hojas de las plantas donde ahi se ve si el Gorgojo se alimento o no, buscar en lugares húmedos cerca de la parcela, dado que ahi es donde se esconde la plaga."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question12=L('Si'), question13=L('Si'), question14=L('Si'), question15=L('No'), question16=L('Si') | L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_5(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:traps"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Elaborar trampas siempre es un gran trabajo, o almenos eso es lo que la mayoria piensa, existen trampas caseras muy buenas y faciles de elaborar para poder combatir a la plaga del Gorgojo de Los Andes, como ser poner piedras planar alrededor de la parcelo o botellas de plástico para atraer a la plaga ahi."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question12=L('Si'), question13=L('Si'), question14=L('Si'), question15=L('Si'), question16=L('No'), question11=L('Si') | L('No')))
    def GorgojoQuestionSix_6(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:gatherGorgojo"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe prácticar esta recolección ya sea visitando las trampas que puso en la parcela, viendo debajo de las plantas de papa o en lugares húmedos donde la plaga del Gorgojo se encuentren. "
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question12=L('Si'), question13=L('Si'), question14=L('Si'), question15=L('Si'), question16=L('Si'), question11=L('No')))
    def GorgojoQuestionSix_7(self):
        question = Question.objects.filter(pk__in=[15])
        urlRedirect = "questionsRules:chemicals"
        self.question = question
        self.urlRedirect = urlRedirect
        self.sugesstion = "Debe saber que no todos los productos químicos son malos para su cultivo, existen productos químicos inorgánicos buenos para su cultivo como el Acaritop a su vez tener en cuenta que tambien puede elaborar productos químicos orgánicos con aji o ajo para proteger su cultivo."
        return self.question, self.urlRedirect
    
    @Rule(AS.gorgojoQuestionSix << GorgojoQuestionSix(question17=L('Si'), question12=L('Si'), question13=L('Si'), question14=L('Si'), question15=L('Si'), question16=L('Si'), question11=L('Si')))
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