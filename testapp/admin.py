from django.contrib import admin
from django.db import models
from .models import Category, OrderItem,Chef,CustomUser
from django.forms import CheckboxSelectMultiple
# Register your models here.

##########################################
######## ORDER ITEM ADMIN CLASS ##########
##########################################
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order_id','category_name','product_name','table_no','prepared_by','status']

admin.site.register(OrderItem,OrderItemAdmin)

##########################################
######## CHEF  ADMIN CLASS ##########
##########################################

class ChefAdmin(admin.ModelAdmin):
    list_display=['chef_id','chef_name','product_name','orders_completed','status']
    #for checkbox select multiple for many to many field
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    readonly_fields=['orders_completed']
admin.site.register(Chef,ChefAdmin)

##########################################
######## CATEGORY ADMIN CLASS ############
##########################################

class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_id','category_name']
    readonly_fields=['category_id','category_name','description','category_image']
admin.site.register(Category,CategoryAdmin)

##########################################
######## CUSTOM USER ADMIN CLASS ##########
##########################################

admin.site.register(CustomUser)
