from django.urls import path,re_path
from apps.buku import views

urlpatterns = [
    path('',views.index)
]
