from django.contrib import admin
from .models import Question, Choices, Lottery, LotteryOptions

# admin.site.register(Question)

class ChoicesInline(admin.StackedInline):
    model = Choices
    can_delete = False
    verbose_name_plural = 'choices'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoicesInline,)
    
class LotteryOptionsInline(admin.StackedInline):
    model = LotteryOptions    
    can_delete = False
    verbose_name_plural = 'LotteryOptions'

@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    inlines = (LotteryOptionsInline,)