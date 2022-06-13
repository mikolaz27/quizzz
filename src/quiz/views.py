from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from accounts.models import Customer
from quiz.models import Question, Quiz, Result
from quiz.tasks import mine_bitcoin, normalize_email_task


class IndexView(ListView):
    template_name = "index.html"
    queryset = Quiz.objects.all()
    context_object_name = "all_quiz"
    paginate_by = 1


class QuizDetailsView(DetailView):
    template_name = "quiz_details.html"
    model = Quiz

    def get_object(self, queryset=None):
        return Quiz.objects.get(uuid=self.kwargs.get("uuid"))


class ResultDetailsView(DetailView):
    model = Result
    template_name = "quiz_results.html"

    def get_object(self, queryset=None):
        return Result.objects.get(uuid=self.kwargs.get("uuid"))


class QuestionDetailsView(DetailView):
    model = Question
    template_name = "question_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quiz"] = Quiz.objects.get(uuid=self.kwargs.get("uuid"))
        return context

    def get_object(self, queryset=None):
        return Question.objects.filter(
            quiz__uuid=self.kwargs.get("uuid"),
            order_number=self.kwargs.get("order")
        ).first()

    def check_correct_answer(self, question_instance, result_instance):
        right_answer = question_instance.choices.filter(
            is_correct=True).first()
        answer = int(self.request.POST.get("checkbox"))

        if right_answer.id == answer:
            result_instance.number_of_correct_answers += 1
            result_instance.save()

    def post(self, request, uuid, order):
        question_instance = Question.objects.get(
            quiz__uuid=self.kwargs.get("uuid"),
            order_number=self.kwargs.get("order")
        )
        current_quiz = Quiz.objects.get(uuid=uuid)

        print(self.request.POST)
        if order == 1:
            result_instance = Result.objects.create(
                quiz=current_quiz,
                user=self.request.user,
            )
            self.request.session["result_instance"] = str(result_instance.uuid)
            self.check_correct_answer(question_instance, result_instance)

        elif order == current_quiz.questions.count():
            result_instance = Result.objects.get(
                uuid=self.request.session.get("result_instance"))
            self.check_correct_answer(question_instance, result_instance)

            return HttpResponseRedirect(reverse("quiz:result_details", kwargs={
                "uuid": result_instance.uuid}))

        else:
            result_instance = Result.objects.get(
                uuid=self.request.session.get("result_instance"))
            self.check_correct_answer(question_instance, result_instance)

        next_page = order + 1

        return HttpResponseRedirect(reverse("quiz:question_details",
                                            kwargs={"uuid": uuid,
                                                    "order": next_page}))


def bitcoin(request):
    mine_bitcoin.delay()

    return HttpResponse("Task is started")


def normalize_email(request):
    normalize_email_task.delay(filter=dict(email__endswith=".com"))
    return HttpResponse("Task is started")
