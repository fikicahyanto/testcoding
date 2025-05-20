from django.urls import path
from . import views

app_name = 'peta'
urlpatterns = [
    path('', views.peta_index, name='peta_index'),
    path('<int:post_id>/', views.peta, name='peta'),
]