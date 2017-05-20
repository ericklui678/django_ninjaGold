from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    if request.session.get('gold') == None:
        request.session['gold'] = 0
    if request.session.get('log') == None:
        request.session['log'] = ''
    return render(request, 'ninjaGold_app/index.html')

def process_money(request):
    now = datetime.datetime.now()
    if 'farm' in request.POST:
        randomNum = random.randrange(10,21)
        request.session['gold'] += randomNum
        request.session['log'] = '<p class=green>Earned ' + str(randomNum) +' gold from farm!  ' +str(now.strftime('%Y/%m/%d %H:%M')) + '</p>' + request.session['log']
    if 'cave' in request.POST:
        randomNum = random.randrange(5,11)
        request.session['gold'] += randomNum
        request.session['log'] = '<p class=green>Earned ' + str(randomNum) +' gold from cave!  ' +str(now.strftime('%Y/%m/%d %H:%M')) + '</p>' + request.session['log']
    if 'house' in request.POST:
        randomNum = random.randrange(2,6)
        request.session['gold'] += randomNum
        request.session['log'] = '<p class=green>Earned ' + str(randomNum) +' gold from house!  ' +str(now.strftime('%Y/%m/%d %H:%M')) + '</p>' + request.session['log']
    if 'casino' in request.POST:
        randomNum = random.randrange(-50,51)
        request.session['gold'] += randomNum
        if randomNum > 0:
            request.session['log'] = '<p class=green>Earned ' + str(randomNum) +' gold from casino!  ' +str(now.strftime('%Y/%m/%d %H:%M')) + '</p>' + request.session['log']
        else:
            request.session['log'] = '<p class=red>Lost ' + str(abs(randomNum)) +' gold from casino!  ' +str(now.strftime('%Y/%m/%d %H:%M')) + '</p>' + request.session['log']
        if request.session['gold'] < 0:
            request.session['gold'] = 0
    return redirect('/')
