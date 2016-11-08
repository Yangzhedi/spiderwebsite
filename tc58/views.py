from django.shortcuts import render
from tc58.models import ArtiInfo
from django.core.paginator import Paginator


def index(request):
    limit = 15
    arti_info = ArtiInfo.objects[:20]
    paginatior = Paginator(arti_info, limit)
    page = request.GET.get('page',1)
    print request
    print request.GET
    loaded = paginatior.page(page)

    context = {
        # 'title': arti_info[0].title[9:20],           # 'Just a title',
        # 'des':  arti_info[0].area,  # 'Just a des',
        # 'score': arti_info[0].price,  # '1.0'
        'ArtiInfo': loaded
    }
    return render(request,'Components/index.html',context)


# def new_index(request):
#     return render(request,'new_index.html')
#

def index3(request):
    limit = 5
    arti_info = ArtiInfo.objects[:20]
    paginatior = Paginator(arti_info, limit)
    page = request.GET.get('page',1)
    print request
    print request.GET
    loaded = paginatior.page(page)

    context = {
        # 'title': arti_info[0].title[9:20],           # 'Just a title',
        # 'des':  arti_info[0].area,  # 'Just a des',
        # 'score': arti_info[0].price,  # '1.0'
        'ArtiInfo': loaded
    }
    return render(request,'index3.html',context)