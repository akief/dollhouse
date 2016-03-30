from django.shortcuts import render, get_object_or_404
from .models import Location
from .models import Article
from .models import Doll
from . import models

def index(request):
    dolls = models.Doll.objects.all()
    return render(request, 'houseitself/index.html', {'dolls': dolls})

def showdoll(request, doll_id):
    d = get_object_or_404(Doll, pk=doll_id)
    return render(request, 'houseitself/show_doll.html', {'doll': d})

def showdolly(request):
    doll_id = int(request.GET["ID"])
    d = get_object_or_404(Doll, pk=doll_id)
    return render(request,'houseitself/show_doll.html', {'doll': d})

def show_one_doll(request, doll_id):
    return render(request, 'houseitself/show_doll.html', {
                  'doll': doll_id,
                  })

def dragdrop(request):
    dolls = models.Doll.objects.all()
    return render(request,'houseitself/dragndrop.html', {'dolls':dolls})

#def showdoll(request):
#    doll_id = int(request.GET["ID"])
#    d = get_object_or_404(Doll, pk=doll_id)
#    return render(request, 'houseitself/show_doll.html', {
#                  'doll': d,
#                  })

def add_doll(request):
    d = Doll()
    d.name = request.POST["name"]
    d.image = request.POST["image"]
    d.location = Location(pk=int(request.POST["location"]))
    d.save()

# Create your views here.
