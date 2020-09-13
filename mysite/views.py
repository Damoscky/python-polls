from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi world, you're doing well")

def about(reqeust):
    return HttpResponse("About our page")

def contact(request):
    return HttpResponse("This is the contact page")

def service(request):
    return HttpResponse("Our Service are listed here")