from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from add_db import load_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('load_data/', load_data),
    path('api/v1/', include('api.urls', namespace='api')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
