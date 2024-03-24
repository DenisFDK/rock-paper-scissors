from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Камень Ножницы Бумага')
root.geometry('310x300')

items = ['Камень', 'Ножницы', 'Бумага']

def startGame1():
	import random
	randChoice = random.choice(items)
	txt1.config(text='Твой выбор:')
	txt2.config(text='Выбор бота:')
	userChoice.config(text='Камень')
	botChoice.config(text=randChoice)
	if randChoice == 'Бумага':
		txt3.config(text='Ты проиграл')
	elif randChoice == 'Камень':
		txt3.config(text='Ничья')
	else:
		txt3.config(text='Ты выиграл')


def startGame2():
	import random
	randChoice = random.choice(items)
	txt1.config(text='Твой выбор:')
	txt2.config(text='Выбор бота:')
	userChoice.config(text='Бумага')
	botChoice.config(text=randChoice)
	if randChoice == 'Ножницы':
		txt3.config(text='Ты проиграл')
	elif randChoice == 'Бумага':
		txt3.config(text='Ничья')
	else:
		txt3.config(text='Ты выиграл')

def startGame3():
	import random
	randChoice = random.choice(items)
	txt1.config(text='Твой выбор:')
	txt2.config(text='Выбор бота:')
	userChoice.config(text='Ножницы')
	botChoice.config(text=randChoice)
	if randChoice == 'Камень':
		txt3.config(text='Ты проиграл')
	elif randChoice == 'Ножницы':
		txt3.config(text='Ничья')
	else:
		txt3.config(text='Ты выиграл')

txt1 = Label(root, text='')
txt1.place(x=10,y=50)
userChoice = Label(root, text='')
userChoice.place(x=100,y=50)

txt2 = Label(root, text='')
txt2.place(x=10,y=100)
botChoice = Label(root, text='')
botChoice.place(x=100,y=100)

rock = Button(root, text='Камень', command=startGame1)
rock.place(x=20,y=10)

paper = Button(root, text='Бумага', command=startGame2)
paper.place(x=110,y=10)

scissors = Button(root, text='Ножницы', command=startGame3)
scissors.place(x=200,y=10)

txt3 = Label(root, text='')
txt3.place(x=10, y=150)

root.mainloop()