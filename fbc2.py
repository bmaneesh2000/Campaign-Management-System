from fbchat import Client
from fbchat.models import *
import pyautogui
import pyperclip
import time
import webbrowser

##def fb(s,i,c):
#    username = str("Sankaranetralayya Pione")
#   password= str("bonda2")
#    #i=100006835832468
#    i=int(i)
#   c=str(c)
#   s=str(s)
#   client = Client(username,password)
#   print("Own id: {}".format(client.uid))
#   client.send(Message(text=c), thread_id=i, thread_type=ThreadType.USER)

def fb(s,i,c):
    i=str(i)
    url='https://www.facebook.com/messages/t/'+i
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)
    c=str(c)
    pyperclip.copy(c)
    time.sleep(15)
    c=str(c)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    pyautogui.press("enter")
    c="to give feedback click here:- http://127.0.0.1:5000/feedback"
    pyperclip.copy(c)
    time.sleep(5)
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    pyautogui.press("enter")

