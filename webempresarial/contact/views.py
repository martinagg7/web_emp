from django.shortcuts import render,request

# Create your views here.
def contact(request):
    return render(request, "core/contact.html")