import django_filters
from .models import Order

class OrderFilter(django_filters.FilterSet):
    note = django_filters.CharFilter(lookup_expr='icontains')
    end_date = django_filters.DateFilter(field_name='date_created', lookup_expr='date__lt')
    start_date= django_filters.DateFilter(field_name='date_created', lookup_expr='date__gt')
    class Meta:
        model = Order
        fields = ['product', 'status', 'note',]
