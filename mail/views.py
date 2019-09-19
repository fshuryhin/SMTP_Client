from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .Controllers.CMail import SendMail
from .Controllers.CSettings import CSettings
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse
from .Controllers.CCrypto import CCrypto

# Create your views here.

# Index function (Main page load)
def index(request):
    # create instance and get array model objects
    settings : CSettings = CSettings()
    settingsArr = settings.getSettings()

    # create dictionary from array of model objects
    dicSettings = {}
    for s in settingsArr:
        if s.name == 'password' :
            coder = CCrypto()
            s.val = coder.decode((s.val).encode('utf-8'))
        
        dicSettings[s.name] = s.val
    
    # create mail data dictionary
    dicMail = {
        'from' : dicSettings['username'],
        'subject' : 'Django mail sender',
        'text' : 'Hello!!!'
    }

    # send data to template
    context = {
        'dicmail' : dicMail,
        'dicsettings' : dicSettings,
    }

    return render(request, 'mail/index.html', context)

# Send Mail function
def sendMail(request):
    # send message
    listTo = request.POST['to'].replace(' ', '').split(',')
    sendMail: SendMail = SendMail(request.POST['subject'], request.POST['text'], request.POST['from'], listTo)
    result = sendMail.sendMessage()

    return JsonResponse(result)

def setSettings(request):
    settings : CSettings = CSettings()
    settings.setsettings(request.POST)

    return HttpResponse('Settings was set')
