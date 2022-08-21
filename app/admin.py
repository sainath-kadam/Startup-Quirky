from atexit import register
from django.contrib import admin
from .models import Customer,OrderPlaced, OrderUpdate,Product,Cart,Productpg
from .models import Contact

from .models import Orders

# Register your models here.
admin.site.register(Customer)
admin.site.register(OrderPlaced)
admin.site.register(Product)
admin.site.register(Productpg)
admin.site.register(Cart)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

