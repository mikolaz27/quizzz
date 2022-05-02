from django.core.exceptions import ValidationError
from django.test import TestCase

from quiz.models import Category, Question, Quiz


def sample_quiz(title, **params):
    defaults = {"description": "Some text", "category": Category.objects.create()}
    defaults.update(params)
    return Quiz.objects.create(title=title, **defaults)


def sample_question(quiz, order_number, **params):
    defaults = {"text": "Some text"}
    defaults.update(params)
    return Question.objects.create(quiz=quiz, order_number=order_number, **defaults)


class TestQuizModel(TestCase):
    def setUp(self) -> None:
        self.questions_count = 10
        self.test_quiz = sample_quiz(title="test_quiz")
        for i in range(self.questions_count):
            sample_question(quiz=self.test_quiz, order_number=i)

    def tearDown(self) -> None:
        self.test_quiz.delete()

    def test_questions_count_normal_case(self):
        self.assertEqual(self.questions_count, self.test_quiz.questions_count())

    def test_title_limit(self):
        with self.assertRaises(ValidationError):
            sample_quiz(title="i" * 70000)
