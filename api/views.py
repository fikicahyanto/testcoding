from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Post

def api_view(request):
    posts = Post.objects.all().order_by('-created_at')[:20]
    data = [
        {
            'user': p.user.username,
            'message': p.message,
            'location': p.location,
            'latitude': p.latitude,
            'longitude': p.longitude,
            'datetime': p.created_at.isoformat()
        } for p in posts
    ]
    return JsonResponse({'posts': data})
