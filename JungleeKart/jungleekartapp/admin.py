from django.contrib import admin
from . import models

# Register your models here.

class AdminModel(admin.ModelAdmin):
    # list_display = ('pk', '__str__',)
    pass
admin.site.register(models.Product,AdminModel)
admin.site.register(models.Product_Category,AdminModel)
admin.site.register(models.Product_Inventory,AdminModel)
admin.site.register(models.Discount,AdminModel)
admin.site.register(models.Custom_User,AdminModel)
admin.site.register(models.Order_Details,AdminModel)
admin.site.register(models.Order_Items,AdminModel)
admin.site.register(models.Cart_Details,AdminModel)
admin.site.register(models.Cart_Items,AdminModel)
admin.site.register(models.Payment_Details,AdminModel)
admin.site.register(models.Brand,AdminModel)