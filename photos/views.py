from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image
from django.http import HttpResponse
from .utils import generate_directory_tree
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

def rename_images_in_folder(folder_path):

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


def importAlbum(request):
    if request.method == "POST":
        folder_path = request.POST.get('folder_path')
        if folder_path:
            rename_images_in_folder(f'photos/templates/albums/'+folder_path)
            return HttpResponse("Images renamed successfully!")
        else:
            return HttpResponse("Folder path is required.", status=400)
    return render(request, 'add.html')

def directory_tree_view(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tree = generate_directory_tree(base_dir)
    return render(request, 'pages/directory_tree.html', {'tree': tree})


