from django.urls import path

from quiz.views import QuestionDetailsView, QuizDetailsView, ResultDetailsView

urlpatterns = [
    path("<uuid:uuid>/", QuizDetailsView.as_view(), name="quiz_details"),
    path("<uuid:uuid>/question/<int:order>", QuestionDetailsView.as_view(), name="question_details"),
    path("result/<uuid:uuid>/", ResultDetailsView.as_view(), name="result"),
]
