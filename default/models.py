from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

def user_directory_path_tablets(instance, filename):
	return 'product/tablets/'+ instance.name + '.jpg'


def user_directory_path_injections(instance, filename):
	return 'product/injections/'+ instance.name + '.jpg'

def user_directory_path_medicines(instance, filename):
    return 'product/medicines/'+ instance.name + '.jpg'


class Member(models.Model):
    name = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    email = models.EmailField(blank=False)  
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)  

class Address(models.Model):
    member = models.ForeignKey(Member, blank=False, related_name="address", on_delete=models.CASCADE)
    value = models.TextField()


class Tablet(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    image =  models.ImageField(upload_to=user_directory_path_tablets)
    brand = models.CharField(max_length=200)
    description = models.TextField(null=True)
    composition = models.TextField(null=True)
    manufacturer = models.CharField(max_length=200,blank=True)
    pharmaceutical_name = models.TextField(null=True)
    unit_name = models.CharField(max_length=200,null=True)
    price_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_25 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_50 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_100 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    purchase_quantity = models.IntegerField(null=True)
    in_cart = models.ForeignKey(Member, related_name="tablet_bought", blank=True, null=True)


    def __str__(self):
    	return self.name;


class Injection(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    image =  models.ImageField(upload_to=user_directory_path_injections)
    description = models.TextField(null=True)
    brand = models.CharField(max_length=200)
    description = models.TextField(null=True)
    composition = models.TextField(null=True)
    manufacturer = models.CharField(max_length=200,blank= True)
    pharmaceutical_name = models.TextField(null=True)
    unit_name = models.CharField(max_length=200,null=True)
    price_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_25 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_50 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_100 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    purchase_quantity = models.IntegerField(null=True)
    in_cart = models.ForeignKey(Member, related_name="injection_bought", blank=True, null=True)
    def __str__(self):
    	return self.name;

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    image =  models.ImageField(upload_to=user_directory_path_medicines)
    description = models.TextField(null=True)
    brand = models.CharField(max_length=200)
    description = models.TextField(null=True)
    composition = models.TextField(null=True)
    manufacturer = models.CharField(max_length=200,blank= True)
    pharmaceutical_name = models.TextField(null=True)
    unit_name = models.CharField(max_length=200,null=True)
    price_1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_25 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_50 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price_100 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    purchase_quantity = models.IntegerField(null=True)
    in_cart = models.ForeignKey(Member, related_name="medicine_bought", blank=True, null=True)



    def __str__(self):
        return self.name;