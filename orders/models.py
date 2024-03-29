from django.db import models
from shop.models import Product
from django.conf import settings

class Order(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    address         = models.CharField(max_length=250)
    email           = models.EmailField()
    postal_code     = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    created         = models.DateTimeField(auto_now_add= True)
    updated         = models.DateTimeField(auto_now=True)  
    paid            = models.BooleanField(default=False)
    stripe_id       = models.CharField(max_length=250, blank=True)

    class Meta : 
        ordering = ['-created']
        indexes  = [
            models.Index(fields=['-created'])
        ]


    def __str__(self) -> str:
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())
    
    def get_stripe_url (self): 
        if not self.stripe_id: 
            return ''
        if '__test__' in settings.STRIPE_SECRET_KEY:
            path = '/test/'
        else:
            path = '/'
        return f'https://dashboard.stripe.com{path}payments/{self.stripe_id}'


    
class OrderItem(models.Model):
    order     = models.ForeignKey(Order, related_name='item', on_delete=models.CASCADE)
    product   = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price     = models.DecimalField(max_digits=12, decimal_places=2)
    quantity  = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
    