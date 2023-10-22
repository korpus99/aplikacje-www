from django.http import HttpResponse


def index(request):
    return HttpResponse("Tu kiedyś nic nie powstanie.")