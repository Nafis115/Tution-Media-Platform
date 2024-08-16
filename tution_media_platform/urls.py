
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin_pannel/',include("admin_pannel.urls")),
    path('api/tutor/',include("tutor.urls")),
    path('api/tution/',include("tution.urls")),
    path('api/application/',include("apply_for_tution.urls")),
    path('api/service/',include("service.urls")),

    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)