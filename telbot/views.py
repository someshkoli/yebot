# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
import requests
# Create your views here.
"""config={
'apikey': " AIzaSyCMTjIY5xAjzz4rngCMQWygVcNNVgQlvFg ",
'storageBucket':"gs://telbot-9c138.appspot.com/",
}
firebase=pyrebase.initialize_app(config) """
#
def index(request):
	return render(request,"index.html")

def get_man(request):
	"""return render(request,
                        "https://api.telegram.org/bot727019423:AAEnYQDHDKygojIJovPpAttzskvS6bAaB5g/sendMessage?chat_id=573080922&text=tesst"
                        )"""
	return requests.post('https://api.telegram.org/bot727019423:AAEnYQDHDKygojIJovPpAttzskvS6bAaB5g/sendMessage',json={'chat_id':573080922,'text':'test'})

