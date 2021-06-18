import sqlite3
from django.shortcuts import render
import twstock
import matplotlib.pyplot as plt
import os

def ad(request):
    st = request.POST.get('Search')
    stock = {}
    for i in twstock.codes:
        if twstock.codes[i].code == st or twstock.codes[i].name == st:
            std = twstock.realtime.get(twstock.codes[i].code)
            stock.update({'sname': std.get('info').get('name')})
            stock.update({'scode': std.get('info').get('code')})
            stock.update({'stime': std.get('info').get('time')})
            stock.update({'sfullname': std.get('info').get('fullname')})

            stock.update({'bib_price': std.get(
                'realtime').get('best_bid_price')})
            stock.update(
                {'bib_vol': std.get('realtime').get('best_bid_volume')})
            stock.update({'ask_price': std.get(
                'realtime').get('best_ask_price')})
            stock.update(
                {'ask_vol': std.get('realtime').get('best_ask_volume')})

                
    pt = request.POST.get("value")
    rt = request.POST.get("month")
    ft = request.POST.get("year")
    A = ['1303', '2303', '2308', '2317', '2330', '2412', '2881', '2882', '6505']
    B = ['2010', '2011', '2012', '2013', '2014', '2015',
         '2016', '2017', '2018', '2019', '2020', '2021']
    C = ['01', '02', '03', '04', '05', '06',
         '07', '08', '09', '10', '11', '12']
    D = ['南亞', '聯華', '台達', '鴻海', '台積電', '中華電信', '聯發科', '富邦', '國泰', '台塑']
    conn = sqlite3.connect(
        os.path.join(os.path.dirname(os.path.dirname(__file__)),'db.sqlite3'))
    cursor = conn.cursor()
    e = -1
    for i in A:
        e += 1
        if pt == i:
            for j in B:
                if ft == j:
                    for k in C:
                        if rt == k:
                            cursor.execute(
                                "SELECT open, close,date FROM '{}'".format(i))
                            rows = cursor.fetchall()
                            o, c, d = [], [], []
                            for g in rows:
                                l = list(g)
                                t = l[2].split("-")
                                if t[0] == j and t[1] == k:
                                    l[0], l[1] = float(l[0]), float(l[1])
                                    l[2] = l[2].split(' ')[0]
                                    o.append(l[0])
                                    c.append(l[1])
                                    d.append(l[2])
                            plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
                            plt.rcParams['axes.unicode_minus'] = False
                            fig = plt.figure(figsize=(21, 13))
                            plt.plot(d, o, '-', label="收盤價")
                            plt.plot(d, c, '-', label="開盤價")
                            plt.title(
                                '{}{}-{} 開盤/收盤價曲線'.format(D[e], ft, rt), loc='center', fontsize=30)
                            print(ft)
                            plt.xlabel('日期', fontsize=25)
                            plt.ylabel('收盤價', fontsize=25)
                            plt.xticks(fontsize=18)
                            plt.yticks(fontsize=18)
                            plt.grid(True, axis='y')
                            plt.legend(fontsize=30)
                            plt.xticks(rotation=-30)
                            fig.savefig(os.path.join(os.path.dirname(os.path.dirname(__file__)),'mysite','static','pic','image.png'))
    return render(request, 'index.html', locals())


def our(request):
    return render(request, 'our.html')

