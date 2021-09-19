from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoUploadForm
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
# Create your views here.

@require_safe
def main(request):
    videos = Video.objects.order_by('-pk')
    context = {
        'videos': videos,
    }
    return render(request, 'videos/main.html', context)

@login_required
@require_http_methods(["GET","POST"])
def upload(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos:main')
    else:
        form = VideoUploadForm()
    context = {
        'form': form,
    }
    return render(request, 'videos/upload.html', context)
