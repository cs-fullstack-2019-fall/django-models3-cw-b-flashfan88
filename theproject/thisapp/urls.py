from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('.urls')),   # you need to include inside "theproject" not "thisapp" and you need to include "thisapp.urls" to successfully access the urls and views inside you application
    path('admin/', admin.site.urls),
]