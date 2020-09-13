from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You're doing well")

def contact(request):
    return HttpResponse("Contact page here")