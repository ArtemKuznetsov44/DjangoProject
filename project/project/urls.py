from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # This item will be used when user whants to go to the main page.
    # Our main page in our main app, that is why whe need to include it.
    # Main page path is empty path, just https://host/
    # In out main app we have to create the urls.py file which we have included here.
    path('', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Если мы находимся в режиме отладки, то: 
if settings.DEBUG:
    # К осноным определенным выше маршрутам добавляем еще один маршрут для статических графических файлов: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    