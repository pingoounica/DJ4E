from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. f98ed892 is the polls index.")