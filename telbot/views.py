from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
import pyrebase
import requests
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt 

def index(request):
	query=json.load(request)
	data=query
	print(data['message']['text'])
	if data['message']['text']=="/get_man":
		get_man(request)
	elif data['message']['text'] is "/get_assig":
		get_assig(request)
	else:
		false_request()
	return HttpResponse("true")
def get_man(request):
	
	return requests.post('https://api.telegram.org/bot727019423:AAEnYQDHDKygojIJovPpAttzskvS6bAaB5g/sendMessage',json={'chat_id':573080922,'text':"select subject for manual",'reply_markup':{'inline_keyboard':[[{'text':'cg','url':'www.google.com'}],[{'text':'ostl','url':'www.google.com'}],[{'text':'am','url':'www.google.com'}],[{'text':'coa','url':'www.google.com'}],[{'text':'aoa','url':'www.google.com'}]]}})
def get_assig(request):
	return requests.post('https://api.telegram.org/bot727019423:AAEnYQDHDKygojIJovPpAttzskvS6bAaB5g/sendMessage',json={'chat_id':573080922,'text':"select subject for assignment",'reply_markup':{'inline_keyboard':[[{'text':'cg','url':'www.google.com'}],[{'text':'ostl','url':'www.google.com'}],[{'text':'am','url':'www.google.com'}],[{'text':'coa','url':'www.google.com'}],[{'text':'aoa','url':'www.google.com'}]]}})
def false_request():
	return requests.post(url='https://api.telegram.org/bot727019423:AAEnYQDHDKygojIJovPpAttzskvS6bAaB5g/sendMessage',json={'chat_id':573080922,'text':"false request please enter a valid request"})
	
"""def up(request):
	file=open
	chat_id=request['result']['from']['id']
	storage=firebase.storage()
	storage.child("am/").put("./image.png")
"""