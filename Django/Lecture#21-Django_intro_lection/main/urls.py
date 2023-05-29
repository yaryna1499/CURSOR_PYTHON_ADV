from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from main.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
