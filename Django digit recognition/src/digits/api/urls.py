from .views import DigitViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'digits', DigitViewSet)
urlpatterns = routers.urls