# In ChatApp/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Changed to 'chat/' to be more specific
    path("chat/", include("chat.urls")),
    # Changed to 'profiles/' to be more specific
    path('profiles/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
