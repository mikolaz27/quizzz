from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from quiz.models import Question, Quiz


class IndexView(ListView):
    template_name = "index.html"
    queryset = Quiz.objects.filter()
    context_object_name = "all_quiz"
    paginate_by = 1
    context_data = ["something", "something_else", ]

    def _get_something(self):
        return "something"

    def _get_something_else(self):
        return "something_else"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        for i in self.context_data:
            context[i] = getattr(self, f"_get_{i}")()
        print(context)
        return context


class QuizDetailsView(DetailView):
    pass


class ResultDetailsView(DetailView):
    pass


class QuestionDetailsView(DetailView):
    model = Question
