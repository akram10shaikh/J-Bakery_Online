from django.contrib import admin
from myapp.models import User_work,UserProfile,Product,Type_product,Cart,Order,OrderStatus,Values,Cart_list

# Register your models here.

admin.site.register(Cart)
admin.site.register(Type_product)
admin.site.register(User_work)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Values)
admin.site.register(Cart_list)
