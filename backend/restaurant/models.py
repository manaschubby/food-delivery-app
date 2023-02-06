from django.db import models
from customer.models import Outlet, Item
# Create your models here.


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='item')
    created = models.DateTimeField(auto_now_add=True)
    customerID = models.TextField()
    ready = models.BooleanField(default=False)
    quantities = models.TextField()

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.created.__str__()
     
    def get_absolute_url(self):
        return f'/{self.slug}/'