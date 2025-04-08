from django.shortcuts import render, redirect, get_object_or_404
from .models import UploadedImage
from .s3_utils import upload_file, delete_file
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

# CREATE + READ
def image_upload_view(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        url = upload_file(file)
        UploadedImage.objects.create(name=file.name, url=url)
        return redirect('image_upload')
    
    images = UploadedImage.objects.all()
    return render(request, 'storage/image_form.html', {'images': images})

# DELETE
@csrf_exempt
@require_http_methods(['POST'])
def image_delete_view(request, pk):
    image = get_object_or_404(UploadedImage, pk=pk)
    delete_file(image.name)
    image.delete()
    return redirect('image_upload')

# UPDATE (rename image entry)
@csrf_exempt
@require_http_methods(['POST'])
def image_update_view(request, pk):
    image = get_object_or_404(UploadedImage, pk=pk)
    new_name = request.POST.get('name')
    
    if new_name:
        image.name = new_name
        image.save()

    return redirect('image_upload')