from django.contrib import admin
from django.urls import path, include
from .views import index, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product_module.urls')),
]