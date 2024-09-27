
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin_panel/',include("admin_panel.urls")),
    path('api/tutor/',include("tutor.urls")),
    path('api/student/',include("student.urls")),
    path('api/tuition/',include("tuition.urls")),
    path('api/application/',include("apply_for_tuition.urls")),
    path('api/contact/',include("contact.urls")),

    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)