from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, Score
import random

def quiz_views(request):
    return render(request, 'index.html')


def get_question(request):
    questions = list(Question.objects.values())
    random.shuffle(questions)
    return JsonResponse(questions, safe=False)

def save_score(request):
    username = request.GET.get('username')
    score = request.GET.get('score')
    Score.objects.create(username=username, score=score)
    return JsonResponse({'message': 'score saved'})