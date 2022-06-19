from django.contrib import admin
from django.urls import path
from main.views import ProjectList,ProjectDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', ProjectList.as_view()),
    path('project/<int:pk>/', ProjectDetail.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
