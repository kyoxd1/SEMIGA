from django.contrib import admin
from .models import Question, Choices

# admin.site.register(Question)

class ChoicesInline(admin.StackedInline):
    model = Choices
    can_delete = False
    verbose_name_plural = 'choices'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoicesInline,)