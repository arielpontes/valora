from django.contrib import admin
from django.urls import path

from apps.estimates.views import estimate_detail, estimate_wizard, home


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("estimate/", estimate_wizard, name="estimate-wizard"),
    path("estimate/<int:pk>/", estimate_detail, name="estimate-detail"),
]
