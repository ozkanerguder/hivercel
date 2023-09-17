from django.http import HttpResponse

from django.shortcuts import render
from django.contrib.auth import authenticate
#from django.http import JsonResponse
#import json
from ast import literal_eval


user = authenticate(username="super", password="persu")
if user is not None:
    x = 3
else:
    x = 3


def myfunction( HTTPRequest ):
    word1 = "ozkan" #xrequest.POST.get("id")
    word2 = HTTPRequest.POST.get("id", "shit" )
    contact = HTTPRequest.body
    data = literal_eval(HTTPRequest.body.decode('utf8'))
    print( data["id"] )
    aysegeriverdi = 'gonderi'
 #   all = '{ "var1": word1, "var2": word2, "var3": aysegeriverdi }'
    all = { "var1": "abc", "var2": "xyz", "var3": "qrt" }
    return render( HTTPRequest, "index.html", all )

glo = 'BIG'

def blankfunction( HTTPRequest ):
    global glo
    glo = glo + 'X'
    print (glo)
    return render( HTTPRequest, "index.html", {'var1': glo },content_type ="text/html" )



# def ayse(paket) :
#    return paket + 'yi actim!...'