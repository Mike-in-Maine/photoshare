from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def viewPhoto(request, pk):
    return render(request, 'pages/photo.html')

def addPhoto(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "pages/add.html", {"obj": obj})
    else:
        form = ImageForm()
    img = Image.objects.all()
    return render(request, "pages/add.html", {"img": img, "form": form})

