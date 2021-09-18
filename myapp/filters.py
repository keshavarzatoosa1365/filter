import django_filters
from django_filters import  CharFilter,NumberFilter

from .models import *

class DomainFilter(django_filters.FilterSet):
	min_price = NumberFilter(field_name="price", lookup_expr='gte')
	# max_price = NumberFilter(field_name="price", lookup_expr='lte')
	name = CharFilter(field_name='name', lookup_expr='icontains')
	class Meta:
		model = Domain
		fields = '__all__'
		