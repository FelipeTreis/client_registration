from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from register.models import Customer
from register.serializers import CustomerSerializer


class CustomerPagination(PageNumberPagination):
    page_size = 10


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomerPagination
    permission_classes = [IsAuthenticated, ]
