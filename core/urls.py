from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet,DevViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'developers',DevViewSet)

urlpatterns = [
    path('', include(router.urls)),
]