from unicodedata import category
from django.db import models

# Create your models here.

#########################################################
############### allocation choices #####################
#########################################################

allocation_choices = (
    ('incomplete', 'incomplete'),
    ('pending', 'pending'),
    ('complete', 'complete')
)

####################################################
############## ORDER ITEM MODEL ###################
####################################################

class OrderItem(models.Model):
    order_id=models.CharField(max_length=30,null=True,blank=True)
    category_id=models.IntegerField()
    category_name=models.CharField(max_length=100)
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=20,decimal_places=2)
    description=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    allocation=models.BooleanField(default=False)
    table_no=models.IntegerField()
    prepared_by=models.CharField(max_length=100,blank=True,null=True)
    status=models.CharField(max_length=20, choices=allocation_choices, default='incomplete')


    class Meta:
        verbose_name='OrderItem'
        verbose_name_plural='OrderItems'

    def __str__(self):
        return '{}' .format(self.category_name)


#############################################################
################# CATEGORY MODEL ############################
#############################################################

class Category(models.Model):
    category_id=models.IntegerField()
    category_name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    category_image=models.ImageField(default='media')

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categorys'
    
    def __str__(self):
        return '{}' .format(self.category_name)

#############################################################
############### CHEF MODEL ##################################
#############################################################


class Chef(models.Model):
    chef_id=models.IntegerField()
    chef_name=models.CharField(max_length=100,unique=True)
    chef_image=models.ImageField(default='media')
    category_name=models.ManyToManyField(Category)
    product_name=models.CharField(max_length=100)
    orders_completed=models.IntegerField(default=0)
    description=models.TextField(null=True,blank=True)

    mobile=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Chef'
        verbose_name_plural='Chefs'
    
    def __str__(self):
        return '{}' .format(self.chef_name)

##########################################################
################ CUSTOM USER MODEL #######################
##########################################################

class CustomUser(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=30)

    class Meta:
        verbose_name='CustomUser'
        verbose_name_plural='CustomUsers'
    
    def __str__(self):
        return '{}' .format(self.username)