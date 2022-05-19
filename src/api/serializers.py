from django.db.models import Model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import Customer
from quiz.models import Choice, Question, Quiz


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "is_staff"]

    def get_first_name(self):
        print(self.initial_data.get("first_name"))
        return self.initial_data.get("first_name")


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ("id", "text", "is_correct")


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "order_number", "text", "choices"]


class QuizSerializer(ModelSerializer):
    level = serializers.CharField(source="get_level_display")

    class Meta:
        model = Quiz
        fields = ["id", "title", "level", "description", "questions_count"]
