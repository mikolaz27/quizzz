from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import Customer
from quiz.models import Category, Question, Quiz


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.quiz = Quiz.objects.create(
            level=1, title="test", category=Category.objects.create(name="name"), description="TEST"
        )
        self.question = Question.objects.create(quiz=self.quiz, order_number=1)

    def test_quiz_list(self):
        user = Customer.objects.create(email="admin@admin.com", password="admin")
        self.client.force_authenticate(user=user)

        result = self.client.get(
            reverse("api:question_details", kwargs={"uuid": self.quiz.uuid, "order": self.question.order_number})
        )
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, {"id": 1, "order_number": 1, "text": "", "choices": []})

    def test_quiz_list_wrong_user(self):
        result = self.client.get(
            reverse("api:question_details", kwargs={"uuid": self.quiz.uuid, "order": self.question.order_number})
        )
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)
