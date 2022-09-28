from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from register.views import CustomerViewSet

router = SimpleRouter()
router.register(
    'manager', CustomerViewSet
)

urlpatterns = [
    path(
        'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path(
        'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'
    ),
    path('', include(router.urls)),
]
