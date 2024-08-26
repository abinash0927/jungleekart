from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages as msg
from django.utils import timezone
import math

class Product_Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_desc = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to="images/")
    category_created_at = models.DateField(auto_now_add=True)
    category_modified_at = models.DateField(blank=True,null=True)
    category_deleted_at = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return self.category_name

class Product_Inventory(models.Model):
    quantity = models.IntegerField()
    inventory_created_at = models.DateField(auto_now_add=True)
    inventory_modified_at = models.DateField(blank=True,null=True)
    inventory_deleted_at = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return str(self.quantity)
    
class Discount(models.Model):
    discount_name = models.CharField(max_length=255)
    discount_desc = models.CharField(max_length=255)
    discount_percent = models.FloatField(max_length=3)
    discount_active = models.BooleanField()
    discount_created_at = models.DateField(auto_now_add=True)
    discount_modified_at = models.DateField(blank=True,null=True)
    discount_deleted_at = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return self.discount_name
class Brand(models.Model):
    brand_name = models.CharField(max_length=100,null=True,blank=True,default="")

    def __str__(self) -> str:
        return self.brand_name

class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    SKU = models.CharField(max_length=100)
    category_id = models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    inventory_id = models.OneToOneField(Product_Inventory,on_delete=models.CASCADE,null=True,blank=True)
    discount_id = models.ForeignKey(Discount,on_delete=models.CASCADE)
    price = models.FloatField(max_length=10)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True,blank=True,default="")
    rating = models.IntegerField(null=True,blank=True)
    main_image = models.ImageField(upload_to="images/")
    # sub_image1 = models.ImageField(upload_to="static/product_images")
    # sub_image2 = models.ImageField(upload_to="static/product_images")
    # sub_image3 = models.ImageField(upload_to="static/product_images")
    # sub_video = models.FileField(upload_to="static/product_videos")
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(blank=True,null=True)
    deleted_at = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
class Custom_User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone_number = models.IntegerField(blank=True,null=True)

    def __str__(self) -> str:
        return self.user.username

class Payment_Details(models.Model):
    status = models.BooleanField(default=False)

class Order_Details(models.Model):

    user_id = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    total = models.FloatField(null=True,blank=True)
    paymen_id = models.OneToOneField(Payment_Details,on_delete=models.CASCADE)
    order_details_created_at = models.DateField(auto_now_add=True)
    order_details_modified_at = models.DateField(blank=True,null=True)
    order_details_deleted_at = models.DateField(blank=True,null=True)

class Order_Items(models.Model):
    order_id = models.ForeignKey(Order_Details,on_delete=models.CASCADE)
    product_id = models.OneToOneField(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True,null=True)
    order_created_at = models.DateField(auto_now_add=True)
    order_modified_at = models.DateField(blank=True,null=True)
    order_deleted_at = models.DateField(blank=True,null=True)

class Cart_Details(models.Model):
    user_id = models.OneToOneField(Custom_User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user_id.user.username

    @property
    def total_price(self):
        x = self.cart_items_set.all()
        y = sum([xitem.total_value for xitem in x])
        return math.floor(y)
    @property
    def total_items(self):
        x = self.cart_items_set.all()
        y = sum([xitem.quantity for xitem in x])
        return math.floor(y)
    @property
    def discount_price(self):
        x = self.cart_items_set.all()
        y = sum([xitem.product_id.discount_id.discount_percent for xitem in x])
        return  math.floor((self.total_price * y) / 100)
    
    @property
    def total_amount(self):
        total = (self.total_price + 50) - self.discount_price
        return  math.floor(total)
    
class Cart_Items(models.Model):
    cart_id = models.ForeignKey(Cart_Details,on_delete=models.CASCADE)
    product_id = models.OneToOneField(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True,null=True,default=0)

    @property
    def total_value(self):
        item = self.product_id.price
        tota = 0
        tota += (self.quantity*item)
        return tota
    
    def __str__(self) -> str:
        return self.product_id.name