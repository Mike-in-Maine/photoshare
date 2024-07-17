from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image
from django.http import HttpResponse
import os

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

def importAlbum(request):
    folder_path = 'path/to/your/venezia_mare_folder'
    # Extract the folder name
    folder_name = os.path.basename(os.path.normpath(folder_path))

    # Get a list of files in the folder
    files = os.listdir(folder_path)

    # Filter the list to include only image files (you can add more extensions if needed)
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')
    image_files = [f for f in files if f.lower().endswith(image_extensions)]

    # Sort the image files to ensure consistent renaming
    image_files.sort()

    # Rename the image files sequentially
    for index, filename in enumerate(image_files):
        # Create the new file name
        new_filename = f"{folder_name}_{index + 1}{os.path.splitext(filename)[1]}"

        # Full paths
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed '{old_file}' to '{new_file}'")



