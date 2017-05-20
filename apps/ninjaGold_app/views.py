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
        place = 'farm!'
    if 'cave' in request.POST:
        randomNum = random.randrange(5,11)
        place = 'cave!'
    if 'house' in request.POST:
        randomNum = random.randrange(2,6)
        place = 'house!'
    if 'casino' in request.POST:
        randomNum = random.randrange(-50,51)
        place = 'casino!'

    # update gold counter
    request.session['gold'] += randomNum
    # if lost money, show log in red color
    if randomNum < 0:
        request.session['log'] = '<p class=red>Lost ' + str(abs(randomNum)) +' gold from casino! ' +str(now.strftime('%Y/%m/%d %H:%M')) + '</p>' + request.session['log']
    # else if gained money, show log in green color
    else:
        request.session['log'] = '<p class=green>Earned ' + str(randomNum) +' gold from ' + place + ' ' + str(now.strftime('%Y/%m/%d %H:%M')) + '</p>' + request.session['log']
    # if gold count is less than 0, keep at 0
    if request.session['gold'] < 0:
        request.session['gold'] = 0
    return redirect('/')
