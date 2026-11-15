from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RegisterView
# Create router
router = DefaultRouter()

# Register ProductViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),

]