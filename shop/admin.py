from django.contrib import admin
from shop.models import Flavour,Category,Occasion,Cake,CakeVarient,Basket,BasketItem
# Register your models here.

admin.site.register(Flavour)
admin.site.register(Category)
admin.site.register(Occasion)
admin.site.register(Cake)
admin.site.register(CakeVarient)
# admin.site.register(BasketItem)
# admin.site.register(Basket)