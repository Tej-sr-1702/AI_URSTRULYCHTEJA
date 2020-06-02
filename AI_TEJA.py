#!/usr/bin/env python
# coding: utf-8

# In[7]:


#creating a virtual assistant
#this is by
#urstrulychteja
import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import calendar
import random
import wikipedia
import warnings
#here the module named warning we imported,this gives the warnings 
#here we do that,
#ignoring any messages
warnings.filterwarnings("ignore")
#creating a function for speech recognition
#it records the audio and returns in a string format
def MySpeech():
    # by using Recognizer function,
    # it recognizes sounds etc..
      speech = sr.Recognizer()
        # with Microphone function as source variable,
        # microphone function records the sounds or voice of the user
      with sr.Microphone() as source:
        #we are asking the user to speak anything
            print("Speak Something...")
            # we are saying it to listen the voice or sound of the user using listen function
            audio_data = speech.listen(source)
            # here we use exception handling functions
            # we use try and except method
            try:
                text_info = speech.recognize_google(audio_data)
                print('You said : '+text_info)
                return text_info
            except :
                print("Sorry i couldn't understand your voice")
# let's create a function for the AIresponses back
# by using the gTTS(GOOGLE TEXT TO SPEECH) module
def AIresponse(textResponse):
    # print the textresponse..
    print(textResponse)
    # using gttd select tha language to understand 
    # to give output of the assistant
    # here i am choosing the language english(en)
    # you can choose, whatever the language you want
    ai_response = gTTS(text = textResponse,lang="en",slow=False)
    # save the file
    # you can give your own name
    # i have given here "myassis.mp3"
    ai_response.save("myassis.mp3")
    # using the module os
    # and the attribute system
    # using those and with help of keyword start
    # play the audio named "myassis.mp3"
    os.system("start myassis.mp3")
#now we look in to the Some actiavting words
#like if we see:"ok google","hey alexa","hey siri"
#let's create a function for that
def WakeUpCall(textResponse1):
    #create a list of wake up words
    #you can create your own wake up words
    wake_calls = ["ok teja","hey teja"]
    #convert the list of characters in to lower cases
    text = textResponse1.lower()
    #check to see if the users command/text contains a wake word/phrase
    for calls in wake_calls:
        if calls in text:
            return True
    # in case wake up call doesn't found in the loop it returns false
    return False
# let's create a function for the datetime
def Dates():
    #we use here now function to get the current date & time
    #and also we are using today function to get current date & time
    #here now function we use it for only months & days not for time
    now_func = datetime.datetime.now()
    my_dates = datetime.datetime.today()
    #by using calendar module
    #using the function weekday we get the day of the current date
    week_day = calendar.day_name[my_dates.weekday()]
    #here we just stored months with index numbers 1 to a variable
    month_num = now_func.month
    #here we stored numbers from 1 to 31 in a variable
    day_num = now_func.day
    # let's create a list of months
    #here the index numbers of months_names starts with 0
    months_names = ["January","Febuary","March","April","May"
                   ,"June","July","August","September","October"
                    ,"November","December"]
    # let's create a list of dates
    #same here also index number starts with 0
    days_numbers = ["1st","2nd","3rd","4th","5th"
                   ,"6th","7th","8th","9th","10th"
                   ,"11th","12th","13th","14th","15th"
                   ,"16th","17th","18th","19th","20th"
                   ,"21st","22nd","23rd","24th","25th"
                   ,"26th","27th","28th","29th","30th"
                   ,"31st"]
    return 'Hello teja..today is '+week_day+' '+months_names[month_num - 1]+' '+days_numbers[day_num - 1]+' .'
#now we will see the random greeting messages
# for that we use grreting inputs and response
# let's create a function for the greeting messages by the user
def Greeting_Responses(textResponse2):
    # create a greeting inputs using a list type
    # you can create whatever the greeting you want to give for your assistant
    greeting_inputs = ['hey teja','wish me']
    # and also create the greeting responses
    # we cretae greeting responses again by using list type
    greeting_responses = ['yes..sir','have a nice day sir']
    #if the user input is a greeting the return a randomly messages
    for words in textResponse2.split():
        if words.lower() in greeting_inputs:
            return random.choice(greeting_responses)
    # if no greetings was detected, then return an empty a string
    return ''
# ok till now we have seen the taking audio
# and AI responses
# and also we created the dates
# now lets see the famous personalities
# if we ask our assistant about any famous personalities...
# for example[hey teja,who is steve jobs]
# let's create a function for this
def GetPersonsData(textResponse3):
    word_list = textResponse3.split()
    for i in range(0,len(word_list)):
        if i+3<=len(word_list)-1 and word_list[i].lower() =='who' and word_list[i+1].lower() == 'is':
            return word_list[i+2]+''+word_list[i+3]
while True:
    # record the audio
    text = MySpeech()
    response = ''
    # check for the wake up call word
    if WakeUpCall(text)==True:
        #check for greetings by the user
        response = response + Greeting_Responses(text)
        #check to see,if the user said anything having to  do with date
        if 'date' in text:
            get_dates = Dates()
            response = response+' '+get_dates
        #now here we create,to tell the time
        #our assistant will say the current time
        #if the user said anything having to do with the time
        if 'time' in text:
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                #p.m means post meridiem (PM) after the midday
                meridiem = 'p.m'
                hour = now.hour - 12
            else:
                #a.m means after meridiem(AM) br=efore the midday
                meridiem = 'a.m'
                hour = now.hour
                #convert minute in to a proper string
            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)
            response = response+' '+'It is '+str(hour)+':'+minute+' '+meridiem+'.'
            #check to see if the user said 'who is'
        if 'who is' in text:
            persons = GetPersonsData(text)
            wiki = wikipedia.summary(persons,sentences=2)
            response = response+' '+wiki
        #have the assistant is working
        #let's check
        AIresponse(response)


# In[ ]:





# In[ ]:




