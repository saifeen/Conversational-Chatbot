from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

engine = pp.init()

voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)

def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()

bot = ChatBot("Sheen Bot",
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                  },
                  {
                      'import_path': 'chatterbot.logic.MathematicalEvaluation',
                  },
              ])

convo=["hi", "hello", "hi there", "hey", "heya",
       "who are you?", "I am Miss Bot and I love talking to you",
       "where do you stay?" "I live just in your device, hehe!",
       "who made you?", "Saifeen Naaz created me",
       "What can you do?", "I can uplift your mood.",
       "What can I call you", "You can call me Miss Bot!"
       "goodbye","tata","bye", "nice talking to you",
       "I'm fine thank you",
       "Do you know me?", "I know only Saifeen, you must be her friend",
       "Do you know Saifeen?", "She is my creator."
       ]

tr = ListTrainer(bot)
tr.train(convo)

main = Tk()
main.geometry("500x650")
main.title("Sheen")

img = PhotoImage(file='bot.png')
pl = Label(main, image=img)
pl.pack(pady=5)

def ask_the_bot():
    ques = tf.get()
    ans = bot.get_response(ques)
    msg.insert(END, "You : " + ques)
    msg.insert(END, "Bot : " + str(ans))
    speak(ans)
    tf.delete(0, END)
    msg.yview(END)

frame = Frame(main)

sc = Scrollbar(frame)
msg = Listbox(frame, width=80, height=18, yscrollcommand= sc.set)

sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
tf = Entry(main, font=('Verdana', 20))
tf.pack(fill=X, pady=10)
bttn = Button(main, text='ask me', font=('Verdana', 20), command=ask_the_bot)
bttn.pack(pady=2)

def enterfunc(event):
    bttn.invoke()
main.bind('<Return>', enterfunc)

main.mainloop()
