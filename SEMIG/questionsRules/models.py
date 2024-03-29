from django.db import models

# Create models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("create date")
    
    def __str__(self):
        return self.question_text
    

class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.choice_text
    
class Lottery(models.Model):
    Lottery_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("create date")
    
    def __str__(self):
        return self.Lottery_text
    

class LotteryOptions(models.Model):
    lottery = models.ForeignKey(Lottery, on_delete= models.CASCADE)
    lottery_options_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.lottery_options_text  
      