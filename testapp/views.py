from unicodedata import category
from .models import CustomUser,Chef,OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect, render,get_object_or_404
from .serializers import OrderItemsSerializer,CategorysSerializer
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import threading
import datetime

#refresh using time,automatically orders completed will zero using the time
def test():
    satisfied=1
    while True:
        current_time = datetime.datetime.now()
        if (current_time.hour==4 ) or (current_time.hour==14):
            if satisfied==1:
                chef=Chef.objects.all()
                for x in chef:
                    x.orders_completed=0
                    x.save()
                satisfied=0
        else:
            satisfied=1

threading.Thread(target=test).start()

# Create your views here.

# we can get orderitem from apis ,this is orderitem api views
@api_view(['POST'])
def orderitem_view(request):
    serializer = OrderItemsSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

# we can get category from apis ,this is category api views
@api_view(['POST'])
def category_view(request):
    serializer = CategorysSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)



#login view
@csrf_exempt
def login_view(request):
    form = CustomUserForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                user.save()
                return redirect("testapp:chef")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    return render(request, "testapp/login.html", {"form": form, "msg": msg})


#order item allocation and chefs list
def chef_view(request):
    #filter the all  orderitems and store in order_list
    orders_list=OrderItem.objects.filter(prepared_by=None) 
    # get all chefs from Chef model using status is active by using filter
    chef_list=Chef.objects.filter(status=True)    
    def chefallotment(st):
        b2=Chef.objects.filter(id=st)
        return b2[0].orders_completed
    try:
        #each orderitem in order list 
        for i in orders_list:
            #we can get orderitem orderid      
            oID=i.order_id
            # orderitem productname
            prn=i.product_name
            # all active chefs store in z 
            z=Chef.objects.filter(status=True)
            zk=[]
            for k in range(len(z)):
                all_user_categories = z[k].category_name.all() #filter chefs who can cook category name items
                filtered_user_categories = z[k].category_name.filter(category_name = i)
                if len(filtered_user_categories)>0:
                    zk.append(z[k])
            z=zk
            print('final z',z)
            print('Im printing z',z)
            #here we get chefs id  
            zc1=[zc.id for zc in z]      
            z=zc1      
            print('Im printing z id',z)
            cn=i.category_name        
            FL=[chefallotment(st) for st in z]  
            m=min(FL)
            i=FL.index(m) 
            asgn=Chef.objects.filter(id=z[i])   
            CN=asgn[0].chef_name
            #get orderid and category name and product_name from orderitem model
            cf=OrderItem.objects.get(order_id=int(oID),category_name=cn,product_name=prn)
            cf.prepared_by=CN
            cf.save()
            cf1=Chef.objects.get(id=z[i])
            #increment to 1 to the particular chef
            cf1.orders_completed=int(cf1.orders_completed)+1
            cf1.save()
        return render(request,'testapp/chef.html',{"chef_list":chef_list})
    except Exception as e:
        print(e)
        return render(request,'testapp/chef.html',{"chef_list":chef_list})

#chef details view and orders allocation to the chef 
def chefdetailsview(request,id):
    chef=Chef.objects.get(id=id)
    print(chef.chef_name)
    orderitem=OrderItem.objects.filter(Q(prepared_by = chef.chef_name) & ( Q(status = 'incomplete') | Q(status = 'pending')))
    if len(orderitem) == 1:
        alloc_1 = orderitem[0]
        return render(request, 'testapp/chef_detail.html', {
                                                        'chef' : chef, 
                                                        'orderitem':  orderitem, 
                                                        'alloc_1' : alloc_1,
                                                        })

    elif len(orderitem) > 1:
        alloc_1 = orderitem[0]
        alloc_2 = orderitem[1:]

        return render(request, 'testapp/chef_detail.html', {
                                                'chef' : chef, 
                                                'orderitem':  orderitem, 
                                                'alloc_1' : alloc_1,
                                                'alloc_2' : alloc_2, 
                                                })
    else:
        return render(request, 'testapp/chef_detail.html', {
                                                'chef' : chef, 
                                                'orderitem':  orderitem, 
 
 
                                                })




# PENDING ALLOCATION  STATUS VIEW
@login_required(login_url='login')
def PendingAllocStatus(request, id, chef_id):
    allocation = OrderItem.objects.get(id = id)
    allocation.status = 'pending'
    allocation.save()
    chef = Chef.objects.get(id = chef_id)    
    return redirect('testapp:details', chef.id)


# ALLOCATION COMPLETED VIEW
@login_required(login_url='login')
def CompleteAllocStatus(request, id, chef_id):
    allocation = OrderItem.objects.get(id = id)
    allocation.status = 'complete'
    allocation.save()
    chef = Chef.objects.get(id = chef_id)  
    return redirect('testapp:details', chef.id)


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("testapp:login")
