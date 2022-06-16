import random

from django.http import HttpResponse

from mongo_blog.models import Blog, Entry


def create_in_mongo(request):
    some_random_text = "".join([random.choice("fdksgvjhkfdbvjhsfdbvhjsd") for _ in range(3)])

    saved = Entry(blog=[Blog(name=some_random_text, text=some_random_text)], headline="some random text").save()

    return HttpResponse(f"Done: {saved}")


def all_entries(request):
    blogs_timestamps = list(Entry.objects.all().values_list("timestamp"))

    print(blogs_timestamps)

    return HttpResponse("| ".join([timestamp.strftime("%m-%d-%Y %H:%M:%S") for timestamp in blogs_timestamps]))
