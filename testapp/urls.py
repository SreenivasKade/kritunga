from . import views
from django.urls import path
# ADD APP NAME IN URLS
app_name='testapp'

urlpatterns = [
    path('category',views.category_view),# CATEGORY API VIEW URL
    path('orderitem',views.orderitem_view),# ORDERITEM API VIEW URL
    path('login',views.login_view,name='login'),# CUSTOM USER LOGIN  PAGE VIEW URL
    path("logout", views.logout_view, name="logout"),
    path('chef',views.chef_view,name='chef'),# CHEF LIST VIEW PAGE URL
    path('details/<int:id>/', views.chefdetailsview,name='details'),# CHEF DETAILS PAGE URL
    path('pending-alloc-status/<str:id>/<str:chef_id>/',  views.PendingAllocStatus, name = 'pending-alloc-status'),# ALLOCATIONS PENDING STATUS URL
    path('complete-alloc-status/<str:id>/<str:chef_id>/',  views.CompleteAllocStatus, name = 'complete-alloc-status'), # ALLOCATION COMPLETE STATUS URL
    
   
]