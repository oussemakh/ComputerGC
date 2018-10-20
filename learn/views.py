from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import learn

# Create your views here.

@login_required(login_url="/nlogin")
def see_learn(request):
    see = learn.objects.all()
    page =request.GET.get('page',1)

    paginator = Paginator(see,6)
    try:
        seel = paginator.page(page)
    except PageNotAnInteger:
        seel = paginator.page(1)
    except EmptyPage:
        seel = paginator.page(paginator.num_pages)

    return render(request, 'learn.html', {'seel':seel})

def learn_detail(request, slug2):
    ldetail = get_object_or_404(learn, slug2=slug2)
    return render(request, 'learnd.html', {'ldetails':ldetail})