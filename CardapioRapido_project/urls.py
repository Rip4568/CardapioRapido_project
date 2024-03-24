from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('stores.api.urls_api')),
    path('api/', include('products.api.urls_api')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]

# Adicione as URLs estáticas apenas no modo de desenvolvimento
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)