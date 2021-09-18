from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import Domain
from .filters import DomainFilter


def Domain(request):
	DomainResult= Domain.objects.all()

	myFilter = DomainFilter(request.GET, queryset=DomainResult)
	RD= myFilter.qs 

	context = {'RD':RD,
	'myFilter':myFilter}
	return render(request, 'Domain.html',context)


