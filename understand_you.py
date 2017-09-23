# VIVEKIOT - Pydev  Artificial intelligence Code : developed on 17-4-2017 
# Program Ex -LInk : Doctor.py
import random
from time import sleep
import os
import webbrowser


username=raw_input("Who are you ?")
os.system('clear')
print "\n***********************Welcome to System chat*********************\n"

#style of conversion
class conversion:

    def __init__(self,uname):
        name=uname
    greetings=['hi','hii','hiii','Hi','Hii','Hiii','Hi!','Hii!']
    responses=['okay','seri','Hmm','ok']
    myself=['Fine, what about you','Good , You??','Always fine, How are you']
    general_questions=['what','who','how','why','when']
    leaving_greetings=['bye','Bye','Byee','Bye']
    angry=['Are you mad','will you Stop this','Are you playing ?']
    clear=['clear','Clear','delete','Delete']
    casual=['what are you doing']
    thankreply=['You are welcome ','Happy to help ']
    yes=['yea','yes','s']
    apologise=['its ok','take it easy','just leave it']

class counts:
    greet_message_count=1
    def __init__(self,value):
        greet_message_count=value
def play(s):
    w=webbrowser
    a=w.open(s)
    return a

memory =[]
CONV=True

#object definition
c=conversion(username)
count=counts(1)

while CONV:
    userInput=raw_input(">>> %s   : "%username)
    if userInput in c.greetings:
        mygreet=random.choice(c.greetings)
        print ">>> System  :",mygreet

        count.greet_message_count=count.greet_message_count+1
        if count.greet_message_count==3:
            talk= "\t\tHello %s , How many times will you send Hii !!" %username
            print talk

            talk1= "\t\tTalk something else"
            print talk1

            count.greet_message_count=count.greet_message_count+1
        if count.greet_message_count>=5:
            talk= "%s"%random.choice(c.angry)
            print talk

            count.greet_message_count=count.greet_message_count+1

    if userInput.find("bye")>=0:
        count.greet_message_count=1
        mygreet=random.choice(c.leaving_greetings)
        print ">>> System  :",mygreet

        CONV=False
    if userInput.find('how')>=0 and userInput.find('you')>0:
        randomreply=random.choice(c.myself)
        talk=">>> System  :"+randomreply+"\n>>> %s   :"%username

        userreply=raw_input(">>> System  :"+randomreply+"\n>>> %s   :"%username)
        if userreply!='':
            talk= ">>> System  :",random.choice(c.responses)

    if (userInput.find('delete')>=0 or userInput.find('clear')>=0) and userInput.find('chat')>0:
        talk= ">>> System   : Okay Ill clear in 2 seconds"
        print talk

        sleep(2)
        os.system('clear')
        print "\n***********************Welcome to System chat*********************\n"
    if userInput in c.yes:
        talk= ">>> System   : "+random.choice(c.responses)
        print talk

    if userInput.find("sorry")>=0:
        talk1=">>> System    : "+random.choice(c.apologise)
        talk2= ">>> System    : "+random.choice(c.casual)
        print talk1

        print talk2

        reply=raw_input(">>> %s   :"%username)
        talk= ">>> System   : "+random.choice(c.responses)
        print talk
    if (userInput.find("help")>=0 and userInput.find("me")>=0):
        talk= ">>> System    : Yea "
        print talk

        talk=">>> System    : Please tell me \n>>> %s  :"%username

        helper=raw_input(">>> System    : Please tell me \n>>> %s  :"%username)
        if helper.find("ping")>=0:
            talk=">>> System    : Yea. i can .  say ip address\n>>> %s:"%username
            ip=raw_input(">>> System    : Yea. i can .  say ip address\n>>> %s  :"%username)
            print "\n"
            z=os.system("ping %s -c 1"%ip)
            if z==0:
                talk= "\n\n\t\tAre you Happy now"
                print talk

            else:
                print "Sorry . You are not connected to internet properly"
    if userInput.find("play")>0 and userInput.find("song")>0:  #song recogniser
        play("content/whatsong.wav")
        print "What song u want ?"
        song=raw_input(">>> %s"%username)
        if ((song.find("bahubali")==0 or song.find("bahubali")>0)and (song.find("siva")>0 or song.find("siva")==0)):
            z=play("s.mp3")
            if z>0:
                print "playing song for u"
            else:
                print "I dont have it"
        if ((song.find("bahubali")==0 or song.find("bahubali")>0)and song.find("pachai")>0):
            z=play("p.mp3")
            if z>0:
                print "playing song for u"
                print "Enjoy"
            else:
                print "I dont have it"
        if ((song.find("what")==0 or song.find("what")>0)and ((song.find("song")==0  or song.find("song")>0) or (song.find("songs")==0 or song.find("songs")>0))):
            print "This all i have"

    if userInput.find("thank")>=0:
        print ">>> System   :",random.choice(c.thankreply),"%s"%username
