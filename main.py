import tkinter

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sys
from tkinter import *

def SetUpBot():
    global chatbot
    chatbot = ChatBot('John Snow')
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english.conversations")
    trainer.train("chatterbot.corpus.english.greetings")
    trainer.train("chatterbot.corpus.english")


def SetTk():
    global responcelabel, textBox
    window = Tk(className="Chat bot")
    window.geometry("1000x1000")
    responcelabel = Label(window, text="bruh?")
    responcelabel.pack()
    textBox = Text(window, height=5, width=52)
    textBox.pack()
    sendButton = Button(text="Send", command = SendMessage)
    sendButton.pack()
    window.mainloop()

def SendMessage():
    messageG = textBox.get("1.0", "end")
    if messageG != "":
        responce = chatbot.get_response(messageG)
        responcelabel.config(text = responce)
    else:
        responcelabel.config(text = "Uhh, I think you didn't put anything inside...")




if __name__ == '__main__':
    SetUpBot()
    SetTk()




