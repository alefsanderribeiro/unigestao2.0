from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        ) + [
    path('', admin.site.urls),
    # path('', include('employees.urls')),
]
