import sqlite3
from django.shortcuts import render
import twstock

def ad(request):
    st=request.POST.get('Search')
    std = twstock.realtime.get(st)
    stock={}
    for i in twstock.codes:
        if twstock.codes[i].code==st or twstock.codes[i].name==st:
            stock.update({'sname': std.get('info').get('name')})
            stock.update({'scode': std.get('info').get('code')})
            stock.update({'stime': std.get('info').get('time')})
            stock.update({'sfullname': std.get('info').get('fullname')})

            stock.update({'bib_price': std.get('realtime').get('best_bid_price')})
            stock.update({'bib_vol': std.get('realtime').get('best_bid_volume')})
            stock.update({'ask_price': std.get('realtime').get('best_ask_price')})
            stock.update({'ask_vol': std.get('realtime').get('best_ask_volume')})      
    return render(request,'twstock.html',stock)

def test(request):
    return render(request, 'test.html')
def ball(request):
    return render(request, 'ball.html')
