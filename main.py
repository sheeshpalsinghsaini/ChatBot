from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import  *

bot = ChatBot("My Bot")

# from chatterbot.trainers import ListTrainer

conversation = [
    "hello",
    "hi there!",
    "what is your name?",
    "my name is Bot, i created by sheeshpal singh",
    "How are you ?",
    "i am doing great thsee days.",
    "that is good to hear",
    "thank you.",
    "you're welcome.",
    'in which city you live ?',
    'i live in Amroha',
    'in which language you talk ?',
    'i mostly talk in english'

]

trainer = ListTrainer(bot)

trainer.train(conversation)


# response = bot.get_response("my name")
# print(response)
# print("Talk with Bot")
# while True:
#     query=input()
#     if query=='exit':
#         break
#     answer=bot.get_response(query)
#     print("bot : ",answer)


main=Tk()
main.geometry("500x650")
main.title("My ChatBot")
img=PhotoImage(file="2.png" )
photoL=Label(main,image=img)
photoL.pack(pady=10)

def ask():
    query=textF.get()
    ans_from_bot=bot.get_response(query)
    msgs.insert(END,"You :",query)
    # print(type(ans_from_bot))
    msgs.insert(END,"Bot :",str(ans_from_bot))
    textF.delete(0,END)
    msgs.yview(END)


    # print("Cliked")



frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#Creating text field
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10,padx=10)
#creating Enter function

btn=Button(main,text="Ask",font=("Verdana",20),command=ask)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)


main.mainloop()
































