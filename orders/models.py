from django.db import models
from django.db.models import Index

from lib.db.choice_enum import IntChoiceEnum


class PizzaSize(IntChoiceEnum):
    """ Available pizza sizes. """
    AVERAGE = 30
    BIG = 50


class Order(models.Model):
    """ Very simplified order model. """

    class Meta:
        indexes = [
            Index(fields=['customer_name'], name='idx__orders__customer_name')
        ]

    customer_name = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=400)
    pizza_id = models.IntegerField()
    pizza_size = models.PositiveSmallIntegerField(choices=PizzaSize.choices())
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
