from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from accounts.models import Customer
from api.serializers import (CustomerSerializer, QuestionSerializer,
                             QuizSerializer)
from quiz.models import Question, Quiz


class UserViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class QuestionDetailsView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_object(self):
        return Question.objects.get(quiz__uuid=self.kwargs.get("uuid"), order_number=self.kwargs.get("order"))


class QuizListView(ListAPIView):
    """
    test docs
    """

    # permission_classes = [AllowAny]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
