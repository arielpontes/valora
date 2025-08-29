from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from apps.estimates.views import estimate_wizard


def index(request):
    return HttpResponse("Hello, world!")


urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("estimate/", estimate_wizard),
]
