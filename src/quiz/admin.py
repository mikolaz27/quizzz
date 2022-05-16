from django.contrib import admin

from quiz.models import Category, Choice, Question, Quiz, Result

for model in (Quiz, Choice, Result, Question, Category):
    admin.site.register(model)
