from django.urls import path
from . import views
from django.conf.urls import url
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton,InlineKeyboardMarkup
from firebase import firebase
import os
urlpatterns=[
#	url('',views.get_man,name='index'),
	url(r'\w*',views.index,name='index'),
#	url('up',views.up,name='up'),
]
bot=telepot.Bot('727019423:AAEnYQDHDKygojIJovPpAttzskvS6bAaB5g')
def handle(msg):
	if msg['text']=='/get_man':
		get_manual(msg)
	if msg['text']=='/get_assign':
		get_assignments(msg)
def get_manual(msg):
	content_type,chat_type,chat_id=telepot.glance(msg)
	firebase1=firebase.FirebaseApplication('https://assignments-c2657.firebaseio.com/')
	result=firebase1.get('studymaterialofsem4',None)
	posts=[]
	buton=[]
	for i in result:
		posts.append(result[i])
	
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
			   [InlineKeyboardButton(text='OS', url="https://firebasestorage.googleapis.com/v0/b/assignments-c2657.appspot.com/o/d2140051-ab29-472a-9a8a-4277a762f9f2?alt=media&token=a48b449a-9c1b-4619-a264-554dfc714a17")],
			   [InlineKeyboardButton(text='OSTL', url="https://firebasestorage.googleapis.com/v0/b/assignments-c2657.appspot.com/o/6cbb05b2-d4ac-4df7-b148-360dedc91684?alt=media&token=4c3c40a3-3285-46f0-82aa-f4b327c8f1f8")],
			   [InlineKeyboardButton(text='CG', url="https://firebasestorage.googleapis.com/v0/b/assignments-c2657.appspot.com/o/62473d02-bdff-4fd6-b01a-c2a1500e1c95?alt=media&token=7a5759e6-1a3a-416f-aea6-1b8bfebe5508")],
			   [InlineKeyboardButton(text='AOA', url="https://firebasestorage.googleapis.com/v0/b/assignments-c2657.appspot.com/o/fef7e230-6a36-4edc-939a-1e02f96d857d?alt=media&token=19aca5bd-260c-43c9-843a-65aad3329b17")],
			   [InlineKeyboardButton(text='COA', url="https://firebasestorage.googleapis.com/v0/b/assignments-c2657.appspot.com/o/5c77c9f4-275f-405f-8734-50a48c50f150?alt=media&token=32361964-a148-4a01-ade4-e3738c4ff3c6")],
           ])
	bot.sendMessage(chat_id,"SELECT SUBJECT",reply_markup=keyboard)
def get_assignments(msg):
	content_type,chat_type,chat_id=telepot.glance(msg)
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
               [InlineKeyboardButton(text='AM', callback_data='5')],
			   [InlineKeyboardButton(text='OS', callback_data='2')],
			   [InlineKeyboardButton(text='OSTL', callback_data='6')],
			   [InlineKeyboardButton(text='CG', callback_data='3')],
			   [InlineKeyboardButton(text='AOA', callback_data='1')],
			   [InlineKeyboardButton(text='COA', callback_data='4')],

           ])
	bot.sendMessage(chat_id,"SELECT SUBJECT",reply_markup=keyboard)
def on_callback_query(msg):
	print(msg)
	query_id,from_id,query_data=telepot.glance(msg,flavor='callback_query')
	firebase1=firebase.FirebaseApplication('https://assignments-c2657.firebaseio.com/')
	result=firebase1.get('assignmentsofsem4',None)
	posts=[]
	buton=[]
	for i in result:
		posts.append(result[i])
	for j in posts:
		if j['subjectcode']==int(query_data):
			buton.append([InlineKeyboardButton(text=j['description'],url=j['link'])])
	print(str(buton))
	query_id,from_id,query_data=telepot.glance(msg,flavor='callback_query')
	keyboard = InlineKeyboardMarkup(inline_keyboard=buton)
	bot.sendMessage(msg['from']['id'],"SELECT ASSIGNMENT",reply_markup=keyboard)
	bot.answerCallbackQuery(query_id, text='Got it')
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()