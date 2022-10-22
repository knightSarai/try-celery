from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.contrib.staticfiles import views
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]

