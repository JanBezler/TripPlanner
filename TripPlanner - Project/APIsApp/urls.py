from django.urls import path, include
from rest_framework.routers import DefaultRouter
from APIsApp import views


router = DefaultRouter()
router.register(r'routes', views.RouteViewSet, basename="routes")

app_name = 'APIsApp'

urlpatterns = [
    path('', include(router.urls)),
    path('button', views.buttonSiteView, name='buttonSiteView')
]
