from django.db import models
from django.db.models.signals import post_save
from accounts.models import User



class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'items'

    def __str__(self) -> str:
        return self.name


class Slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'slots'

    def __str__(self) -> str:
        return '%s - %s' % (self.start_time, self.end_time)


class Booking(models.Model):
    STATUS_CHOICES = (
        (0, 'received'),
        (1, 'preparing'),
        (2, 'complete'),
        (3, 'cancelled'),
        (4, 'collect your order')
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    slot = models.ForeignKey(Slot, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='bookings')
    additional_item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True, related_name='addtional_bookings')
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'

    def __str__(self) -> str:
        return str(self.id)