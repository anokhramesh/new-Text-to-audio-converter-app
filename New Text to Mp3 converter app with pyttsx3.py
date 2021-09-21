# visit this website-https://pypi.org/project/pyttsx3/
#copy the command for installing the module
#open the command prompt and type or paste the command(pip install pyttsx3) then hit enter key
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo
import pyttsx3

root=Tk()
root.title("Text to Voice Converter App")#title of the Application
root.iconbitmap('python_icon1.ico')#icon of the Application
root.geometry('380x370')# Application window size
root.configure(bg='#f08c0a')#Application backgroud color
info_label=Label(root,bg='#07fa48',fg='black',text="Enter your Text below",font=("Georgia 16 bold"))
info_label.grid(row=0,columnspan=3,pady=5)
# Create a function for text to speech
def speak():
    engine=pyttsx3.init()
    audio_string=my_text.get('0.0',END)
    if audio_string:
        engine.setProperty('rate',125)# Speech speed
        voices=engine.getProperty('voices')#getting details of current voice
        engine.setProperty('voice',voices[1].id)# changing index, changes voices. 1 for female
        #engine.setProperty('voice', voices[0].id)#changing index, changes voices. 0 for male
        engine.say(audio_string)
        engine.runAndWait()
        engine.stop()

# Create a function for convert text to Mp3 and save as sound.mp3
def save():
    engine=pyttsx3.init()
    audio_string=my_text.get('0.0',END)
    if audio_string:
        engine.setProperty('rate', 125)  # Speech speed
        voices = engine.getProperty('voices')#getting details of current voice
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        # engine.setProperty('voice', voices[0].id)# changing index, changes voices. 0 for male
        engine.save_to_file(audio_string,'sound.mp3')# Converted audio file name
        engine.runAndWait()
        engine.stop()
        #Create a label to show the result
        result_label=Label(root,fg='red',bg='blue',font=("arial 12 bold"),text="file Saved as sound.mp3")
        result_label.grid(row=3,columnspan=3,pady=4)

#create a scrolledtext widget for user to input some text
my_text=ScrolledText(root,fg='#f00aba',bg='white',font=("Verdana 12 bold"),width=30,height=10,wrap=WORD,padx=10,pady=10,bd=5,relief=RIDGE)
my_text.grid(row=1,columnspan=3,pady=5)

#create a button for speak the text you entered on the scrolltext area
speak_button=Button(root,fg='blue',bg='#0af0ba',text=" Speech",font=("arial 12 bold"),command=speak)
speak_button.grid(row=2,column=0,padx=5,pady=10)

#Create a button for Clear the text you entered on the scrolltext area
clear_button=Button(root,fg='blue',bg='#0af0ba',text="Clear text",font=("arial 12 bold"),command=lambda :my_text.delete('0.0',END))
clear_button.grid(row=2,column=1,padx=5,pady=10)

#Create a button for Convert the text to mp3 and Save
save_button=Button(root,fg='blue',bg='#0af0ba',text="Convert and save",font=("arial 12 bold"),command=save)
save_button.grid(row=2,column=2,padx=5,pady=10)

root.mainloop()