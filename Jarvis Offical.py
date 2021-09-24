import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import pyautogui
import subprocess
import time
from fuzzywuzzy import fuzz
import tkinter as tk
import AutomaticFileSortProgram.SortingFiles as SortingFiles 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)








''' Speak our input '''
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

""" Taking Inut """
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" Please tell me how may I help you")       


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abhijio2620@gmail.com', '________')
    server.sendmail('abhijio2620@gmail.com', to, content)
    server.close()

def ChecMarkData(query):
    try:
        with open(r'CommandDB.txt','r') as CD:
            for i in CD.readlines():
                # print(i)
                score = fuzz.token_set_ratio(query,i.split('\t')[0])
                if score >= 90:
                    # print(i)
                    li = i.split('\t')[1].split('|')
                    # print(li)
                    j = random.randint(0,len(li)-1)
                    return li[j]
    except Exception as e:
        pass


def KeyBoardGen(query):
    if 'scroll' in query:
        if 'up' in query:
            pyautogui.scroll(250)
        elif 'down' in query:
            pyautogui.scroll(-250)
        elif 'left' in query:
            pyautogui.hscroll(-200)
        elif 'right' in query:
            pyautogui.hscroll(200)
    elif 'close' in query and ('this' in query or 'all' in query):
        pyautogui.hotkey('alt','f4')
# Commands for Browser -> In Progress
"""
def BroweFun():
    while True:
        print('Brows Command')
        bquery = takeCommand().lower()

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://www.google.com")
        driver.minimize_window()
        driver.maximize_window()
        if 'search' in bquery and 'now' in bquery:
            SearchWeb = bquery.replace('search','').replace('now','')
            driver.get(SearchWeb)
        elif 'refresh' in query and 'page' in bquery:
            pyautogui.press('f5')
        
        elif 'maximize' in bquery or 'expand it' in bquery:
            print('maximize')
            WinBrows.maximize()
        elif 'manimize' in bquery and ('it' in bquery or 'this' in bquery):
            WinBrows.minimize()

        elif 'close' in bquery and ('this' in bquery or 'all' in bquery or 'it' in bquery):
            pyautogui.hotkey('alt','f4')
            break
        elif KeyBoardGen(bquery):
            pass
"""
import win32gui,win32con


FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
def closeWindow(winName):
    try:
        win = win32gui.FindWindow(None,winName)
        win32gui.SetForegroundWindow(win)
        win32gui.PostMessage(win,win32con.WM_CLOSE,0,0)
        print('\n\nClose WIndow Funcion -- Closed :',winName)
    except Exception as e:
        print('Close WIndow Funcion -- Not Closed :',winName)
        print(e)
def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)
    if path[0]=="\\" or path[0] == "/":
        subprocess.Popen("explorer ,'")
    elif os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    # elif os.path.isfile(path):
    #     subprocess.run([FILEBROWSER_PATH, '/select,', path])
def selectFile(path):
    path = os.path.normpath(path)
    if os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', path])
        
import win32api
def explorerCmd():
    # A.RefreshWin(2)
    driveList = ['c','d','e','f']
    path = ''
    winName = 'This PC'
    flag=0
    flagFile = [0,'']
    while(True):
        # print("\n\nFul Beginnignn Path ->",path)
        # try:
        #     liDir = os.listdir(path)
        #     print(liDir,'\t\tLenght is ',len(liDir))
        #     if(len(liDir)==0):
        #         emptyFlag = 2
        #     else:
        #         emptyFlag = 1
        # except:
        #     pass
        print('\n\nStart_Path === ',path)
        print('Start_winName === ',winName)
        equery = takeCommand().lower()
        # print('End_Path = ',path)

        if len(equery)==0:
            pass
        elif 'close' in equery and 'explorer' in equery:
            closeWindow(winName)
            break
        elif 'copy' in equery and ('file' in equery or 'this' in equery):
            if(flagFile[0] == 1):
                closeWindow(winName)
                selectFile(path+flagFile[1])
                pyautogui.hotkey('ctr','c')
            else:
                speak('File is not Selected')
        elif 'cut' in equery and ('file' in equery or 'this' in equery):
            if(flagFile[0] == 1):
                closeWindow(winName)
                selectFile(path+flagFile[1])
                pyautogui.hotkey('ctr','x')
            else:
                speak('File is not Selected')
        elif 'paste' in equery and ('file' in equery or 'here' in equery):
            if(flagFile[0] == 1):
                closeWindow(winName)
                selectFile(path+flagFile[1])
                pyautogui.hotkey('ctr','v')
            else:
                speak('File is not Selected')

        elif ('open' in equery or 'go to' in equery) and 'drive' in equery:
            equery = equery.split(' ')
            for i in driveList:
                for j in equery:
                    if i==j:
                        path = i +':\\'
                        print(winName)
                        closeWindow(winName)
                        winName = win32api.GetVolumeInformation(path)[0]+f' ({i+":"})'
                        flag=1
                        break
            if(flag==0):
                speak('Drive Not Found, Give correct command !')
                continue
        elif ('open' in equery or 'go to' in equery or 'select' in equery) and flag==1:

            liDir = os.listdir(path)
            liScore = []
            equery = equery.replace('open','',1).replace('go to','',1)
            if('select' in equery):
                equery = equery.replace('select','',1)
                # flag=3
                liDir = [i for i in liDir if os.path.isfile(path+'\\'+i)]
                for i in range(len(liDir)):
                    liScore.append(fuzz.ratio(equery,liDir[i].lower()))
                    index = liScore.index(max(liScore))
                    closeWindow(winName)
                    selectFile(path+liDir[i])
                    flagFile = [1,liDir[i]]
                    continue
                continue

            for i in range(len(liDir)):
                liScore.append(fuzz.ratio(equery,liDir[i].lower()))

            index = liScore.index(max(liScore))
            path += liDir[index] + '\\'
            print(winName)
            closeWindow(winName)
            winName = liDir[index]
        # elif  'select' in equery and flag==1:

        elif 'automatic' in equery and 'run' in equery and ('file' in equery or 'sort' in equery):
            GenAdr = path
            DirAdrList = {'Audio':GenAdr+r'\AutomaticSortedFiles\Audio',
            'Video': GenAdr+r'\AutomaticSortedFiles\Video',
            'Documents':GenAdr+r'\AutomaticSortedFiles\Documents',
            'Images':GenAdr+r'\AutomaticSortedFiles\Images',
            'Code':GenAdr+r'\AutomaticSortedFiles\Code',
            'Folders':GenAdr+r'\AutomaticSortedFiles\Folders'}
            SortingFiles.RunProject(GenAdr,DirAdrList)


        elif 'go back' in equery and flag==1:
            path1 = path.split('\\')
            print('Start at Goto --> ',path1)
            if(path1[-1] == ''):
                path1.remove('')

            if(len(path1)==1):
                path1[0] += '\\'
                winName = win32api.GetVolumeInformation(path1[0])[0]+f' ({path1[0]})'
                closeWindow(winName)
                explore('\\')
                winName = 'This PC'
                flag = 0
                continue
            # print(f'\n\nIn Go back:   (EmptyFlag == {emptyFlag})')
            print('\n\nPath-1 = ',path1)
            path = "\\".join(path1[:-1])+"\\"
            print('Path = ',path)
            print(winName)
            closeWindow(winName)
            # if(':' in path1[-2]):
            #     winName = win32api.GetVolumeInformation(path1[0])[0]+f' ({path1[0]})'
            # else:
            winName = path1[-2]
        elif 'exit now' in equery:
            exit(1)
        else:
            speak('Cant undarstand repeat your Command !')
            continue
        print('End_Path = ',path)
        explore(path)




if __name__ == "__main__":
    wishMe()

    while True:

        print('General command')
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\Songs\\audio_ext'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'open' in query and 'explorer' in query:
            subprocess.Popen("explorer ,'")
            explorerCmd()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")   
        
        # """ Funtion-Open Browser -> In Progress """
        #
        # elif ('open'in query  and 'chrome' in query) or ('work' in query and 'browser' in query and ('in' in query or 'on' in query)):
        #     BroweFun()
        #

        elif 'exit now' in query:
            exit()
        elif ChecMarkData(query):
            speak(ChecMarkData(query))