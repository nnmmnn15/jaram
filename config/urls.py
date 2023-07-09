from django.contrib import admin
from django.urls import path, include

from main.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jaram/', include('main.urls')),
    path('', index, name='index'),
]
