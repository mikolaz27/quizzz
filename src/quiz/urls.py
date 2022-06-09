from django.urls import path

from quiz.views import QuestionDetailsView, QuizDetailsView, ResultDetailsView, \
    bitcoin, normalize_email

app_name = "quiz"

urlpatterns = [
    path("<uuid:uuid>/", QuizDetailsView.as_view(), name="quiz_details"),
    path("<uuid:uuid>/question/<int:order>", QuestionDetailsView.as_view(),
         name="question_details"),
    path("result/<uuid:uuid>/", ResultDetailsView.as_view(),
         name="result_details"),
    path("bitcoin/", bitcoin, name='bitcoin'),
    path("emails/", normalize_email, name='emails')
]
