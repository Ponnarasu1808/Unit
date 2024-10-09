from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Vercel! This is a Django app deployed on Vercel.")
