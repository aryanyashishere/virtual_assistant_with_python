import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from email.message import EmailMessage
from pytube import YouTube
import sqlite3
from os import path
# import sched
# from datetime import datetime
import time
from playsound import playsound
import psutil



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
x = engine.setProperty('voice', voices[len(voices) - 4].id)


client = wolframalpha.Client('W9TKGT-VQ9XQ4QK8L')
# ===================PLAY MUSIC AND YOUTUBE VIDEO DIRECTION SECTION ===========================================
music_dir = "D:\\my music\\vibes"
ytdown = "D:\\youtube videos"
# ===================PLAY MUSIC AND YOUTUBE VIDEO DIRECTION SECTION ENDSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS===========================================

def speak(audio):
    print('jarvis:- ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)

    tt = time.strftime("%I:%M %p")

    if currentH >= 0 and currentH < 12:
        speak(f"Good Morning!, it\'s  {tt}")

    if currentH >= 12 and currentH < 18:
        speak(f"Good Afternoon!, it\'s {tt}")

    if currentH >= 18 and currentH != 0:
        speak(f"Good Evening! , it\'s {tt}")


#_________________________________________-jarvis voice intro-_____________________________________________
now = datetime.datetime.now()
kk = int(now.strftime("%d%m%y"))
# print(kk)


conn = sqlite3.connect('tesla.db')
datedb= conn.execute('select * from jarvissounddate')
date1db = datedb.fetchone()


if kk == date1db[1]:
    conn.close()

else:
    playsound("Jarvis_sound.mp3")
    # conn = sqlite3.connect('tesla.db')
    conn.execute(f'update jarvissounddate set timesound = {kk} where did = 1')
    conn.commit()
    conn.close()



#____________________________________________

def usernamespeak0():


    conn = sqlite3.connect('teslauser.db')
    command = "select * from teslauser teslauser"
    result = conn.execute(command)
    r = result.fetchone()
    usernamespeak0.x = r[1]

# speak('Hello buddy, I am tesla, just tell me work or ask question  ')
# speak('')



# def usercall():


    # with open("usercall.txt", "w" ) as f:
    # (value, file = f)

#

def useridpassword():
    conn = sqlite3.connect('userpass.db')
    # command = "select * from useridpassword"
    resu = conn.execute("select * from useridpassword useridpassword")
    re = resu.fetchone()
    useridpassword.ab = re[1]

    useridpassword.ac = re[2]

def useridpasswordupdate():


    conn = sqlite3.connect('userpass.db')
    # command = "INSERT INTO teslauser (id,name) VALUES(?, ?) ", (seril, your)

    # = "UPDATE teslauser SET name = ? where id = 1 ", (diffname)
    conn.execute("UPDATE useridpassword SET userid =  (?) where id = 1 ", (userid,))
    conn.execute("UPDATE useridpassword SET password =  (?) where id = 1 ", (password,))

    conn.commit()
    speak("ok, changed ")
    conn.close()



# useridpassword()
# print(useridpassword.y)
# print(useridpassword.z)


def usernamespeak():


    conn = sqlite3.connect('teslauser.db')
    command = "select * from teslauser teslauser"
    result = conn.execute(command)
    r = result.fetchone()
    usernamespeak.x = r[1]


def usercallupdate():

    conn = sqlite3.connect('teslauser.db')
    # command = "INSERT INTO teslauser (id,name) VALUES(?, ?) ", (seril, your)

    # = "UPDATE teslauser SET name = ? where id = 1 ", (diffname)
    conn.execute("UPDATE teslauser SET name =  (?) where id = 1 ", (diffname,))
    conn.commit()
    speak("ok, i will call you " + diffname)
    conn.close()


def musicdirectorycall():
    conn = sqlite3.connect('directory.db')
    command = "select * from address"
    resu = conn.execute(command)
    re = resu.fetchone()

    musicdirectorycall.y = re[1]
    # print(x, y)



def musicdirectoryupdate():
    adds = input("ENTER THE MUSIC DIRECTORY HERE")

    conn = sqlite3.connect('directory.db')
    #     command = "INSERT INTO teslauser (id,name) VALUES(?, ?) ", (seril, your)
    #
    # = "UPDATE teslauser SET name = ? where id = 1 ", (diffname)
    conn.execute("UPDATE address SET addid =  (?) where id = 1 ", (adds,))
    # conn.execute("UPDATE useridpassword SET password =  (?) where id = 1 ", (password,))

    conn.commit()
    speak("ok, changed to " + adds)

    conn.close()


def youtubescrap():
    try:

        driver = webdriver.Chrome("chromedriver")
        driver.get('https://www.youtube.com')

        searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
        searchbox.send_keys(search)

        seabutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')

        seabutton.send_keys(Keys.ENTER)
    except:
        speak("sorry youtube is not accessible")


def youtubescrap1():


    driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")
    driver.get('https://www.youtube.com')

    searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
    searchbox.send_keys(search1)

    seabutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')

    seabutton.send_keys(Keys.ENTER)



def youtubescrap2():


        driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")
        driver.get('https://www.youtube.com')

        searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
        searchbox.send_keys(search2)

        seabutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')

        seabutton.send_keys(Keys.ENTER)



def googlescrap():
    try:

        driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")
        driver.get('https://www.google.com')

        searchbox = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys(gosearch)

        seabutton = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')

        seabutton.send_keys(Keys.ENTER)
    except:
        speak("sorry google is not accessible")
def googlescrap1():
    try:

        driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")
        driver.get('https://www.google.com')

        searchbox = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys(gosearch1)

        seabutton = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')

        seabutton.send_keys(Keys.ENTER)
    except:
        speak("sorry google is not accessible")


def googlescrap2():
    try:

        driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")
        driver.get('https://www.google.com')

        searchbox = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys(gosearch2)

        seabutton = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')

        seabutton.send_keys(Keys.ENTER)
    except:
        speak("sorry google is not accessible")


def emailsend():


    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = who_is_sending
    msg['To'] = recipient_address
    msg.set_content(Content)


    server = smtplib.SMTP_SSL('smtp.gmail.com' , 465)
    useridpassword()
    server.login(useridpassword.ab, useridpassword.ac)
    server.send_message(msg)
    server.quit()
    speak("email has been sent!!! to" + recipient_address)

def youdown():
    yt = YouTube(link)

    videos = yt.streams.all()

    i = 1
    for stream in videos:
        print(str(i) + " " + str(stream))
        i += 1

    stream_number = int(input("enter the number"))

    video = videos[stream_number - 1]
    video.download(ytdown)

    usernamespeak()
    speak("your youtube video , downloaded " + usernamespeak.x + " in this directory = " + ytdown)


class command:
    @staticmethod
    def myCommand():


        global query

        # try:


        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.energy_threshold = 1000
            r.pause_threshold = 1
            audio = r.listen(source)

        # except:
        #     print("THERE IS ERROR IN LISTENING")
        try:
            query = r.recognize_google(audio, language='en-in')
            usernamespeak()
            print(usernamespeak.x+ ":-  " + query + '\n')

        except sr.UnknownValueError:

            command.myCommand()
        except Exception as e:
            print(e)

                # speak('ok speak it!')


                # query = str(input('Command: '))

            # speak("you do not have internet connection")


        return query




                # query = str(input('Command: '))

            # speak("you do not have internet connection")


    @staticmethod
    def myCommand1():
        global query

        try:


            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.energy_threshold = 1000
                r.pause_threshold = 1
                audio = r.listen(source)



        except Exception as e:
            speak("THERE IS ERROR IN LISTENING")
            speak(str(e))
        try:
            query = r.recognize_google(audio, language='en-in')
            # query = query.lower()
            # if "i want to write it"== query or "want write it" == query or "want write" == query:
            #     query = input("Command: ")
            # else:
            #     pass
            usernamespeak()
            print(usernamespeak.x+ ":-  " + query + '\n')



        except sr.UnknownValueError:

            # usernamespeak()
            speak('didn\'t get, you can get writing mode on')
            command.myCommand1()
            # audio = r.listen(source)
            # query = audio = r.listen(source)

            # with sr.Microphone() as source:
            #     print("Listening...")
            #     r.pause_threshold = 1
            #     audio = r.listen(source)
            #     query = r.recognize_google(audio, language='en-in')
            #     usernamespeak()
            #     print(usernamespeak.x + ":-  " + query + '\n')
            #     if 'yes' == query or 'ok then' == query or 'ok' == query:
            #
            #         speak('write it!')
            #         query = str(input('Command: '))
            #     else:
            #
            #         speak('ok speak it!')
            #     command.myCommand1()




                # query = str(input('Command: '))

            # speak("you do not have internet connection")




        query =query.lower()
        return query




    @staticmethod
    def writecommand():
        query = input("Command: ")
        usernamespeak()
        print(usernamespeak.x + ":-  " + query + '\n')
        query.lower()
        return query



def taskExecution():
    while True:

        try:
            ii = command()
            conn = sqlite3.connect('tesla.db')
            value = conn.execute('select * from writing')
            valuee = value.fetchone()
            if valuee[1] == 0:

                query = command.myCommand1()
            else:
                query =command.writecommand()



        except Exception as e:
            speak(str(e))

        # ==================================SOCIAL MEDIA SECTION STARTS==========================================================
        if 'open youtube and search' in query:
            try:

                # x = "helllo how are you all"
                # y = x[]
                # while bool(y.isspace()):
                #     print("this is not valid string")

                # print(str(y))
                list = query.split()
                #
                y = list[4:]
                # print(y[0] + y[1])
                # z = str(y)
                # a = y
                # print(z)
                search = ''
                n = 0
                for element in y:
                    # y[]
                    search += (" " + y[n])
                    n += 1
                # print(result)
                if search == '':
                    speak("what do i have to search")
                    search = myCommand1()
                    speak("okay, SEARCHINIG.. " + search)

                    youtubescrap()




                else:
                    speak("okay, searching " + search + " on YOUTUBE")

                    youtubescrap()
            except:

                speak("what do i have to search")
                search = myCommand1()
                speak("okay, SEARCHINIG.. " + search)

                youtubescrap()


        elif 'open youtube search' in query:
            try:
                list1 = query.split()
                #
                y1 = list1[4:]
                # print(y[0] + y[1])
                # z = str(y)
                # a = y
                # print(z)
                search1 = ''
                n = 0
                for element in y1:
                    # y[]
                    search1 += (" " + y1[n])
                    n += 1
                # print(result)
                if search1 == '':
                    speak("what do i have to search")
                    search1 = myCommand1()
                    speak("okay, SEARCHINIG.. " + search1)

                    youtubescrap1()




                else:
                    speak("okay, searching " + search1 + " on YOUTUBE")

                    youtubescrap1()

                # if "" in x or "add 2 and 2" in x:

            except:

                speak("what do i have to search")
                search1 = myCommand1()
                speak("okay, SEARCHING.." + search1)

                youtubescrap1()

        elif 'open youtube' in query:
            speak("what do i have to search")

            search2 = myCommand1()
            speak("okay, SEARCHING.." + search2)

            youtubescrap2()












        elif 'open google and search' in query:
            try:


                listgoogle = query.split()


                ygoo = listgoogle[4:]
                        # print(y[0] + y[1])
                        # z = str(y)
                        # a = y
                        # print(z)
                gosearch = ''
                n = 0
                for element in ygoo:


                            # y[]
                    gosearch += (" " + ygoo[n])
                    n += 1
                        # print(result)
                    if gosearch == '':
                        speak("what do i have to search")
                        gosearch = myCommand1()
                        speak("okay, SEARCHINIG.. " + gosearch)

                        googlescrap()




                    else:
                        speak("okay, searching " + gosearch + " on GOOGLE")

                        googlescrap()
            except:








                speak("what do i have to search")
                gosearch = myCommand1()
                speak("okay, SEARCHING..." + gosearch)

                googlescrap()





        elif 'open google search' in query:
            try:
                listgoogle1 = query.split()
                #
                ygoo1 = listgoogle1[4:]
                # print(y[0] + y[1])
                # z = str(y)
                # a = y
                # print(z)
                gosearch1 = ''
                n = 0
                for element in ygoo1:
                    # y[]
                    gosearch1 += (" " + ygoo1[n])
                    n += 1
                if gosearch1 == '':
                    speak("what do i have to search")
                    gosearch1 = myCommand1()
                    speak("okay, SEARCHINIG.. " + gosearch1)

                    googlescrap1()




                else:
                    speak("okay, searching " + gosearch1 + " on GOOGLE")

                    googlescrap1()
                # print(result)
            except:

                speak("what do i have to search")
                gosearch1 = myCommand1()
                speak("okay")

                googlescrap1()

        elif 'open google' in query:
            speak('what do i have to search')
            gosearch2 = myCommand1()
            speak("okay SEARCHING" + gosearch2)

            googlescrap2()




        elif 'open gmail' in query:
            speak('okay')
            speak('opening GMAIL')
            driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")

            driver.get('https://www.mail.google.com')

        elif 'open facebook' in query or 'facebook open' in query:
            speak("opening facebook")
            driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")

            driver.get('https://www.facebook.com')

        elif 'open instagram' in query or 'instagram open ' in query:
            speak("opening INSTAGRAM")
            driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")

            driver.get('https://www.instagram.com')




        elif 'open twitter' in query or 'twitter open' in query:
            speak("opening TWITTER")
            driver = webdriver.Chrome("C:\\Users\\dell\\Desktop\\CODING TOOL\\chromdriver\\chromedriver")

            driver.get('https://www.twitter.com')


        # ======================================== SOCIAL MEIA SECTION ENDS==========================================================

        # ================= User FRIENDLY ENVIRONMENT SECTION STARTS========================================================================

        elif 'what is tesla' in query or 'tesla motors' in query or 'elon musk tesla' in query or 'elon tesla' in query:
            speak(
                'Searching Wikipedia... or if you want results on google, so  stop me and speak "open google and search" ' + query)
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'jarvis' in query:
            usernamespeak()
            jarvishelMsgs = ["yes, " + usernamespeak.x, "hello, what do you want " + usernamespeak.x + " ??", "yes, sir"]
            speak(random.choice(jarvishelMsgs))


        elif "what\'s up" in query or 'how are you' in query or 'how you doing' in query or 'what\'s going on' in query:
            usernamespeak()
            stMsgs = ['Just doing my thing' + usernamespeak.x + '!!', 'I am fine!' + usernamespeak.x + '!!',
                      'Nice!...' + usernamespeak.x + '!!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "call me" in query or "don't call" in query or "change my name" in query or 'my name' in query:
            speak("so, what do i call you")
            global diffname
            diffname = myCommand1()
            usercallupdate()
        # ================================FRIENDLY ENVIRONMENT SECTION ENDS==============================================================

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")


        # =======================WHO ARE YOU PROGRAM=====================================================================
        elif 'who are you' in query or 'don\'t know you' in query or 'who are you jarvis' in query or 'your full name' in query or 'your full form' in query:
            speak(
                "I am jarvis, your virtual assistant(TECHNOLOGY ENVELOPED in a SMART and LOVELY APPROACH), i help you with yoour tasks ")


        #     ==================who made you program========================================
        elif 'who made you' in query or 'you made' in query or 'programmed you' in query:
            speak(
                "As, I was thought in mind of my creators and then they just progrmmed ME by writing codes of PYTHON programming language..... Those 3... creators... were ....Aryan,.. Sakshi and ...Samarth (and no precendence in them... all three are my .....best.. FRIENDS.... AND I... LOVE.. THEM... A LOT) ")

        elif 'who is this aryan' in query or 'what aryan progrmmed' in query or 'what aryan coded' in query:
            speak(
                'HE ..MODIFIED ME AND ....GAVE.. SOME.. SPECIAL.. FEATURES TO.. ME ..... ALL THE FEATURES IN ME WERE MADE BY ARYAN YASH,..... MY FRIEND')


        elif 'who is this sakshi' in query or 'what sakshi programmed' in query or 'what sakshi coded' in query:
            speak(
                'SHE GAVE ME ABILITY TO REPLY RANDOM STATEMENTS FOR QUESTIONS AND TASKS,  SHE SAKSHI IS MY.. BEST... FRIEND ...AND THANKS .TO.. SAKSHI  ')

        elif 'who is this samarth' in query or 'what samarth programmed' in query or 'what samarth coded' in query:
            speak(
                'HE GAVE ME ABILITY TO SPEAK AND SHOW  YOU.. RESULTS FOR YOUR COMMANDS ..AND ....SAMARTH ..IS.. MY.. BEST.. FRIEND  TOO AFTER ARYAN AND SAKSHI .....THANKS TO SAMARTH ')

        # ===============WHO MADE YOU ENDSSSSSSSSSS=============================================================================================================

        # ===============================EMAIL SEND=====================================================================================================
        elif 'email' in query or 'email to someone' in query:
            try:
                speak("what is the subject??")
                subject = myCommand1()

                speak("ok.. who is sending???")
                who_is_sending = myCommand1()

                speak("ok.. to whom???? type the email address of recipient")
                recipient_address = input("enter the recipient email address ")

                speak("okk.. what do i have to say???")
                Content = myCommand1()
                useridpassword()
                # user = useridpassword.y
                # passw = useridpassword.z

                emailsend()
            except:
                speak(
                    "email can\'t be sent, your userID or password is wrong,  or GMAIL is serving privacy authentication")



        elif 'my email userID password' in query or 'username and password' in query or 'username password' in query or 'userID password' in query or 'userID and password' in query:
            speak("ok, write your userID and password of email to update")
            userid = input("ENTER THE USERID ")
            password = input("ENTER THE PASSWORD ")
            speak("okay, updating into database")
            useridpasswordupdate()

        # =============================================EMAIL SEND ENDSSSSS===============================================================================================

        # ============================WHO AM I SECTION===========================================================================================================
        elif 'who am i' in query:
            speak("You\'re ARE MY BUDDY " + usernamespeak.x)



        # =================================ABORT SECTION===========================================================================================================
        elif 'nothing jarvis' in query or 'abort' in query or 'stop working' in query or 'stop your work' in query:

            speak('okay')
            usernamespeak()
            speak('Bye,' + usernamespeak.x + ' have a good day.')
            break
        # ==============================ABORT SECTION ENDS==========================================================================================

        # ===================================================DOWNLOAD YT VIDEO SECTION=========================================================================
        elif 'download the youtube' in query or 'i want to download youtube video' in query or 'offline' in query:
            usernamespeak()
            speak("okay, Provide me the link..." + usernamespeak.x)
            link = input("ENTER THE YOUTUBE VIDEO LINK HERE")
            youdown()

        # =======================================DOWNLOAD YT VIDEO ENDSSSSSS================================================================================

        # ===========================WILL THE ROBOTS DESTROY US========================================================================================================

        elif 'robots destroy us' in query or 'robots destroy humanity' in query or 'robots destroy the humanity' in query or 'robot destroy the humanity' in query or 'robot destroy humanity' in query or 'robots destroy' in query or 'robots ruin' in query:
            speak(
                'I don\'t know much sir, well i am just ..a.. rather simple, friendly..assisstant and want..good ..of you ..always ')
            speak('and i\'m not much programmed ..to.. take decisions ..by ..myself')







        elif  'want write'in query or  'start writing mode' in query or 'i want to write it' in query or 'writing mode on' in query or 'listening mode off' in query or 'listening mode of' in query:
            conn.execute("update writing set writeid = 1 where id = 1")

            conn.commit()
            conn.close()
            speak("writing  mode  on.")

        elif 'want speak' in query or  'start listening mode' in query or 'i want to speak it' in query or 'writing mode off' in query or 'writing mode of' in query or 'listening mode on' in query:
            conn.execute("update writing set writeid = 0 where id = 1")
            conn.commit()
            conn.close()
            speak("listening  mode  on.")



        # ==================---------hello section-================================================================================================================-
        elif 'hello' in query:
            usernamespeak()
            hellomsgs = ['Hello' + usernamespeak.x, "hello, sir, I AM jarvis , HOW CAN I HELP YOU??"]
            speak(random.choice(hellomsgs))


        elif 'good jarvis' in query or 'nice working' in query or 'great' in query or 'great working ' in query or 'good' in query or 'nice' in query or 'awesome' in query or 'awesome' in query:
            thankMsgs = ['thank you!! ' + usernamespeak.x, 'i am always in your assistance! ' + usernamespeak.x,
                         'thanks buddy!!', 'I am nice and full of energy only cause of you ' + usernamespeak.x]
            speak(random.choice(thankMsgs))
        elif 'bye' in query or 'you go' in query or 'you can go' in query or 'bye jarvis' in query:
            usernamespeak()
            speak('Bye, ' + usernamespeak.x + ' have a good day.')
            break
        # HELLO SECTION ENDS=======================================================HELLO SECTION ENDS================================================================

        # ========================PLAY MUSIC SECTION=====================================PLAY MUSIC SECTION=====================================================

        elif 'music directory' in query:
            speak("so, what is the new music directory please write here")
            musicdirectoryupdate()


        elif 'play some music' in query or 'music play' in query or 'let us be refresh' in query or 'my music' in query or 'play music' in query:
            musicdirectorycall()
            try:

                songs = os.listdir(musicdirectorycall.y)

                # print(songs)


                # speak("choose your choice and enter the number with respect to choice")
                # print(" ")

                # no = int(input(
                #     " 1. Want to start first song from list\n 2. WANT TO SEE LIST AND MAKE YOUR CHOICE\n 3. RANDOMLY PLAY SONG\n\n ENTER THE NUMBER TO CHOOSE"))
                # if no == 1:
                #     speak("enjoy")
                #     os.startfile(os.path.join(musicdirectorycall.y, songs[0]))
                #     time.sleep(20)
                # elif no == 2:
                #     # print(songs)
                #     print(" ")
                #     i = 1
                #     for j in songs:
                #         # print(" ")
                #         # print(" ")
                #         print(str(i) + " " + str(j))
                #         i += 1
                #     print(" ")
                #     choice = int(input("ENTER THE NUMBER OF THE SONG TO PLAY"))
                #     os.startfile(os.path.join(musicdirectorycall.y, songs[choice - 1]))
                #     speak("enjoy")
                #
                #     time.sleep(10)

                # if no == 3:

                random_music = random.choice(songs)
                    # os.system(random_music)
                os.startfile(os.path.join(musicdirectorycall.y, random_music))
                speak("enjoy")
                time.sleep(10)
            except Exception as e:
                speak(e)

                speak("music directory is not accessible")




        # PLAY MUSIC SECTION ENDS==========================================PLAY MUSIC SECTION ENDS==============================================================





        elif "stop the music" in query or "i don\n't like it" in query or 'stop music' in query or 'close the music player' in query or 'close the player' in query:
            def stopmusic():
                for process in psutil.process_iter():

                    if process.name() == "vlc.exe":
                        print(process.pid)

                        os.system('taskkill /im ' + str(process.pid))

            stopmusic()
















        else:
            speak("this is not in my function sir!")




        '''else:
            gosearch = query
            speak('Searching...')
            try:
                try:
                    res = client.query(gosearch)
                    results = next(res.results).text

                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(gosearch, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                googlescrap()'''





        '''usernamespeak()
        lastMsgs = ['WHAT DO YOU WANT NEXT ' + usernamespeak.x + '!!', 'Ok, next command ' + usernamespeak.x + '!!',
                    'ANYTHING ELSE?? so speak the command!!' + usernamespeak.x + '!!',
                    'ASK ABOUT ANYTHING SUCH AS today\'s weather forecast...']
        speak(random.choice(lastMsgs))'''
        # speak(+ usernamespeak.x + '!!!')


taskExecution()

# if __name__ == '__main__':
#     while True:
#         uu = command()
#         permission = command.myCommand()
#
#         if "hey" in permission or "hay" in permission or "hey jarvis" in permission or "hay jarvis" in permission or 'hi jarvis' in permission:
#             greetMe()
#             usernamespeak0()
#             introMsgs = ['Hello, jarvis is here...' + usernamespeak0.x, 'hello, ' + usernamespeak0.x + ' hi sir',
#                          'Welocome ' + usernamespeak0.x, 'Hello sir, anything sir?']
#             speak(random.choice(introMsgs))
#
#             taskExecution()
#
#         elif "bye" in permission or "shutdown" in permission or "shutdown jarvis" in permission or "go now" in permission or "abort jarvis" in permission or "can go" in permission:
#             speak("ok sir, call me back sir!")
#             sys.exit()
#
#
