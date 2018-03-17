from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('customer_name',)
    ordering_fields = ('created_at',)
