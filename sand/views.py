from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from .models import *


def dust_list(request):
    '''dusts post list'''
    dust = Dust.objects.all()

    paginator = Paginator(dust, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sand/base.html',
     {'page_obj': page_obj})
