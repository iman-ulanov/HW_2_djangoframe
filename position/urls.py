from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('position', views.PositionViewSet)
router.register('employee', views.EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v-1.0/', include(router.urls)),
]
