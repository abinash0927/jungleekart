# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45, blank=True, null=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    telephone = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
        unique_together = (('id', 'username'),)

class UserAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    address_1 = models.CharField(max_length = 255)
    city = models.CharField(max_length = 60)
    pin_code = models.IntegerField()
    country = models.CharField(max_length=50)
    telephone = models.IntegerField()