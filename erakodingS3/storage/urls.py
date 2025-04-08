from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_upload_view, name='image_upload'),
    path('delete/<int:pk>/', views.image_delete_view, name='delete_image'),
    path('update/<int:pk>/', views.image_update_view, name='update_image'),
]