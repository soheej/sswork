from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

import pandas as pd
from django.views.generic import CreateView, UpdateView
from .models import Item
from .form import ItemForm


item_new = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)




def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('shop:item_list')


def item_list(request):
    items = Item.objects.all()
    # 키값이 'q'로 지정된 값이 없으면 None이 반환됨
    q = request.GET.get('q', '')  # 'q'로 지정된 값이 없으면 '' 반환
    if q:  # q가 널 아니면 qs에 filter 조건 추가
        items = items.filter(name__icontains=q)
    return render(request, 'shop/item_list.html', {
        'item_list': items,
        'q': q, })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html',
                  {'item': item})



def year_archive(request, year):
    if year is not None:
        return HttpResponse('{}년도 자료 입니다.'.format(year))
    else:
        return HttpResponse('해당년도 자료는 없습니다.')

