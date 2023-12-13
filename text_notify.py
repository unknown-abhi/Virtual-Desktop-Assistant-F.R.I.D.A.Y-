import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
import string
from collections import Counter
#from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen
from twilio.rest import Client

def send_sms(contact_number):
	account_sid = "ACf8413d38bb885b54de7488d975a6662e"
	# Your Auth Token from twilio.com/console
	auth_token  = "25cd1b932c24b4585c25e0f1acdc168d"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to=contact_number, 
	    from_="+14357097912",
	    body="Hello ! your close friend is going through a tough time and needs your support kindly contact " )
	print("Notified\n")
	print(message.sid)

if __name__ == '__main__':
	print('Entered in notify mode')
	filepath = 'close_contact.txt'

	with open(filepath) as fp:
	   line = fp.readline()
	
send_sms(line)
 