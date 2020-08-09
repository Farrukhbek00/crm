from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import *
from .forms import OrderForm

def home(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()

    customers = Customer.objects.all()

    context = {
        'orders':orders,
        'total_orders':total_orders,
        'orders_delivered':orders_delivered,
        'orders_pending':orders_pending,
        'customers':customers,
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    context = {
        'products':products,
    }

    return render(request, 'accounts/products.html', context)

def customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    orders = customer.order_set.all()
    print(orders)

    context = {
        'customer':customer,
        'orders':orders,
    }

    return render(request, 'accounts/customer.html', context)

def update_order(request, pk):
    order = get_object_or_404(Order, id=pk)

    form = OrderForm(instance = order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('accounts:home')
    context = {
        'form':form,
    }

    return render(request, 'accounts/update_order.html', context)

def delete_order(request, pk):
    order = get_object_or_404(Order, id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('accounts:home')

    return render(request, 'accounts/delete_order.html', {'order':order})

def create_order(request, pk):
    form = OrderForm()

    return render(request, 'accounts/create_order.html', {'form':form})
