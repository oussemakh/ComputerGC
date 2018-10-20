from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import PROD

# Create your views here.
@login_required(login_url="/nlogin")
def product(request):
    prod = PROD.objects.all()
    page = request.GET.get('page',1)

    paginator = Paginator(prod,1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage :
        users = paginator.page(paginator.num_pages)
    return render(request, 'prod.html', {'users':users})
def productd(request, slug):
    prodd = get_object_or_404(PROD, slug=slug)

    return render(request, 'productDetail.html', {'prodd':prodd})