import pyautogui
import time
import pyperclip
import webbrowser
url='https://www.facebook.com/messages/t/100068655491527'
webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)
pyperclip.copy('美少女これくしょん~ステータスが存在する世界で、女の子を自由に育てるアプリ~')
time.sleep(10)
pyautogui.keyDown('ctrl')
pyautogui.press('v')
pyautogui.keyUp('ctrl')
pyautogui.press("enter")
