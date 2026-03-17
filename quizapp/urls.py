from django.urls import path
from . import views


urlpatterns = [
    path('', views.quiz_views),
    path('questions/', views.get_question),
    path('save/', views.save_score)
]
