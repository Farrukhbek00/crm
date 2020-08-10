from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import *
from .forms import OrderForm, UserForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .filters import OrderFilter

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
    filter = OrderFilter(request.GET, queryset=orders)

    context = {
        'customer':customer,
        'orders':orders,
        'filter':filter,
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
    customer = get_object_or_404(Customer, id=pk)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('accounts:home')

    return render(request, 'accounts/create_order.html', {'formset':formset})


def registerPage(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    return render(request, 'accounts/register.html', {'form':form})


def loginPage(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('accounts:home')
        else:
            messages.error(request, 'Username or password is wrong')

    return render(request, 'accounts/login.html', {'form':form})


def logoutPage(request):
    logout(request)
    return redirect('accounts:login')
