from django.shortcuts import render

from dashboard.models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def peta(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'peta_app/peta.html', {'post': post})

def peta_index(request):
    return HttpResponse("Silakan pilih lokasi dari dashboard.")
