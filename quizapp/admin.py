from django.contrib import admin
from .models import Question, Score


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'option1', 'option2', 'option3', 'option4')


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('username', 'score')

    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Score, ScoreAdmin)