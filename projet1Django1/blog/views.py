from django.shortcuts import render
from .models import Client
def index(request):
    return render(request,"Clients/index.html",{
        "Client": Client.objects.all()
    })
