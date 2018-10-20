
from django.shortcuts import  render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import Article 
from django.contrib.auth.decorators import login_required


def home(request):
    
    

     user_list = Article.objects.all()
     page = request.GET.get('page', 1)

     paginator = Paginator(user_list, 6)
     try:
        users = paginator.page(page)
     except PageNotAnInteger:
        users = paginator.page(1)
     except EmptyPage:
        users = paginator.page(paginator.num_pages)

     
     return render(request, 'Home.html', {'users':users})

@login_required(login_url="/nlogin")
def detail(request, slug1):
    articleD =  get_object_or_404(Article, slug1=slug1)
    return render(request, 'Detail.html',{'articleD':articleD})
