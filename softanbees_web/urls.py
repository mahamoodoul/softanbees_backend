from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path,include

urlpatterns = [
    path('',include('apply.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
