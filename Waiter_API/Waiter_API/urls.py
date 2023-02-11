
from django.urls import path, include
from django.contrib import admin

urlpatterns = [ # < System URLs
    path('admin/', admin.site.urls),
    path('', include("CORE.urls")) # < Will include the URLs from the urls.py [CORE]
]
