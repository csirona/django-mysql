from django.shortcuts import render
import requests
import json

def Index(request):
    res_usd = requests.get("https://api.blockchain.com/v3/exchange/tickers/BTC-USD")
    data= res_usd.json()    
    context={
        'data':data
    }
    return render(request,"/core/single.html",context)