from django.urls import path

from mongo_blog.views import create_in_mongo, all_entries

app_name = "mongo_blog"

urlpatterns = [
    path("create_mongo/", create_in_mongo, name="create_mongo"),
    path("all_entries/", all_entries, name="all_entries"),
]
