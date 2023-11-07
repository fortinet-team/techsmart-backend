from django.urls import path
from .api_handler import list_question, list_choice, getquestionByid, getchoiceByid

urlpatterns = [
    path('question', list_question, name = "list_question"),
    path('question/<int:question_id>', getquestionByid, name = "getquestionByid"),
    path('choice', list_choice, name = "list_choice" ),
    path('choice/<int:choice_id>', getchoiceByid, name = "getchoiceByid")
]
