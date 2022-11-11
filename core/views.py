from django.shortcuts import render,redirect
import requests
from django.utils import timezone
import json
from django.db.models import Q
from django.shortcuts import get_object_or_404
from core.models import ToDO
from core.forms import ToDOForm


def Index(request):
    res_usd = requests.get("https://api.blockchain.com/v3/exchange/tickers/BTC-USD")
    data= res_usd.json()  
    todos = ToDO.objects.all()
    form=ToDOForm()
    print(data)
    queryset= request.GET.get("search")

    if queryset:
        todos = ToDO.objects.filter(
            Q(name__icontains = queryset)
        ).distinct() 
        
    if request.method == 'POST':
        form = ToDOForm(request.POST)

        if form.is_valid() :
            f=form.save(commit=False)
            f.save()

        
    else:
        form = ToDOForm()

    
    context={
        'data':data,
        'todos':todos,
        'td_form':form,

    }
    return render(request,"core/single.html",context)

def Update(request,id,name):        
    obj = get_object_or_404(ToDO, id = id) 

    obj.id=id
    obj.name=name
    obj.updated_at=timezone.now()
    obj.save()

    return redirect('index')

def ChangeState(request,id):
    obj = get_object_or_404(ToDO, id = id) 
    if obj.state:
        state=False
    else:
        state=True
    obj.state=state
    obj.save()
    return redirect('index')

def Test(request):
    return render(request, "core/test.html")