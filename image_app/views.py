from django.shortcuts import render, redirect
from .forms import *
from .forms import Image_upload
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


def image_view(request):
    if request.method == 'POST':
        ima = request.FILES['ima']
        print(ima)
        img = Image.open(ima)
        width, height = img.size
        if 100 <= width <= 300 and 100 <= height <= 300:
            Image_upload(image=ima).save()
            messages.success(request, 'image saved')
            return redirect('image_upload')
        elif width > 300 and height > 300:
            Image_upload(image=ima).save()
            messages.success(request, 'image saved')
            return redirect('image_upload')
        else:
            messages.error(request, 'image less than 100px')
            return redirect('image_upload')
    return render(request, 'image_form.html')
