from django.urls import include, path
from rest_framework.routers import SimpleRouter

from register.views import CustomerViewSet

router = SimpleRouter()
router.register(
    'manager', CustomerViewSet
)

urlpatterns = [
    path('', include(router.urls)),
]
