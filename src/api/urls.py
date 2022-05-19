from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import QuestionDetailsView, QuizListView, UserViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("customers", UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Quizzz API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    # path("auth/", include('djoser.urls
    path("auth/", include("djoser.urls.jwt")),
    path("<uuid:uuid>/question/<int:order>/", QuestionDetailsView.as_view(), name="question_details"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
]
