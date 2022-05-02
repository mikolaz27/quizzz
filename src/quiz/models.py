import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models


class Quiz(models.Model):
    QUESTION_MAX_LIMIT = 20
    QUESTION_MIN_LIMIT = 3

    class LEVEL_CHOICES(models.IntegerChoices):
        BASIC = 0, "Basic"
        MIDDLE = 1, "Middle"
        ADVANCED = 2, "Advanced"

    category = models.ForeignKey(to="quiz.Category", related_name="quizzes", on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024, null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC)
    image = models.ImageField(default="default.png", upload_to="media/covers")

    def questions_count(self):
        return self.questions.count()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Result(models.Model):
    user = models.ForeignKey(to=get_user_model(), related_name="results", on_delete=models.CASCADE)
    quiz = models.ForeignKey(to="quiz.Quiz", related_name="results", on_delete=models.CASCADE)


class Question(models.Model):
    quiz = models.ForeignKey(to="quiz.Quiz", related_name="questions", on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(Quiz.QUESTION_MAX_LIMIT)])
    text = models.CharField(max_length=512)


class Choice(models.Model):
    question = models.ForeignKey(to="quiz.Question", related_name="choices", on_delete=models.CASCADE)


class Category(models.Model):
    pass
