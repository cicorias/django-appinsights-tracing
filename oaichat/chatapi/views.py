from django.http import HttpResponse
def index(request):
    return HttpResponse(content="index page for chatapi")
