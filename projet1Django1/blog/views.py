from django.shortcuts import render
from .models import Client
def index(request):
    return render(request,"Clients/index.html",{
        "Client": Client.objects.all()
    })


def client(request,client_id):
    client=Client.objects.get(pk=client_id)
    return render(request, "Clients/client.html",{
        "client":client
    })