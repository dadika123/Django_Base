from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.main, name='main'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('new-admin/', include('adminapp.urls', namespace='new_admin')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
