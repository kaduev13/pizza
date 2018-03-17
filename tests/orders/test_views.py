import json

import pytest
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_201_CREATED
from rest_framework.test import APIClient

from orders.models import Order, PizzaSize


@pytest.mark.django_db
class TestOrderViewSet:
    client = APIClient()

    @pytest.fixture
    def order_data(self):
        return {
            'customer_name': 'Ivan Kalita',
            'customer_address': 'Moscow, Zagorodnoe shosse 1',
            'pizza_id': 2,
            'pizza_size': PizzaSize.BIG.value
        }

    @pytest.yield_fixture(scope='function', autouse=True)
    def clean(self):
        Order.objects.all().delete()
        yield

    def test_retrieve_nonexistent(self):
        response = self.client.get('/api/v1/orders/1/')
        assert response.status_code == HTTP_404_NOT_FOUND

    def test_retrieve_existent(self, order_data):
        order = Order.objects.create(**order_data)

        response = self.client.get('/api/v1/orders/{}/'.format(order.id))
        data = json.loads(response.content)

        assert response.status_code == HTTP_200_OK
        for key, value in order_data.items():
            assert data[key] == value

    def test_create(self, order_data):
        response = self.client.post('/api/v1/orders/', order_data)
        data = json.loads(response.content)

        assert response.status_code == HTTP_201_CREATED
        for key, value in order_data.items():
            assert data[key] == value
