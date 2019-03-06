from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
import pyrebase
import requests
import json
# Create your views here.
"""config = {
  "apiKey": "AIzaSyCMTjIY5xAjzz4rngCMQWygVcNNVgQlvFg",
  "authDomain": "telbot-9c138.firebaseapp.com ",
  "databaseURL": "https://telbot-9c138.firebaseio.com/",
  "storageBucket": "telbot-9c138.appspot.com/"
}
firebase=pyrebase.initialize_app(config) """
#
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 

def index(request):
	
	#if("""request['result']['message']['text']=='/get_man'"""True):
	
	get_man(request)
	
	return HttpResponse(escape(repr(request)))
def get_man(request):
	"""return render(request,
                        "https://api.telegram.org/bot727019423:AAEnYQDHDKygojIJovPpAttzskvS6bAaB5g/sendMessage?chat_id=573080922&text=tesst"
                        )"""
	return requests.post('https://api.telegram.org/bot727019423:AAEnYQDHDKygojIJovPpAttzskvS6bAaB5g/sendMessage',json={'chat_id':573080922,'text':str(json.load(request))})

"""def up(request):
	file=open
	chat_id=request['result']['from']['id']
	storage=firebase.storage()
	storage.child("am/").put("./image.png")
"""