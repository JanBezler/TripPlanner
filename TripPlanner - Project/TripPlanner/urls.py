from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('TripPlannerApp.urls')),
    path('api/', include('APIsApp.urls')),
]
