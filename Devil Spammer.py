import time
from tkinter import *
from tkinter import messagebox
from pynput.keyboard import Key, Controller
from random import choice

# Переменные

Keyboard = Controller()

after_10sec1 = ''

after_10sec2 = ''

after_10sec3 = ''

timer_10sec = ''

l9 = ''

l8 = ''

l7 = ''

l6 = ''

l5 = ''

l4 = ''

l3 = ''

l2 = ''

l1 = ''

L = 1  #L = 1(EN), L = 2(RU)

# Функции

def start_text9():
    global l9
    if L == 1:
        l.configure(text="Start in 9 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l9 = root.after(995, start_text8)
    if L == 2:
        l.configure(text="Старт через 9 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l9 = root.after(995, start_text8)

def start_text8():
    global l8
    if L == 1:
        l.configure(text="Start in 8 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l8 = root.after(995, start_text7)
    if L == 2:
        l.configure(text="Старт через 8 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l8 = root.after(995, start_text7)

def start_text7():
    global l7
    if L == 1:
        l.configure(text="Start in 7 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l7 = root.after(995, start_text6)
    if L == 2:
        l.configure(text="Старт через 7 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l7 = root.after(995, start_text6)

def start_text6():
    global l6
    if L == 1:
        l.configure(text="Start in 6 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l6 = root.after(995, start_text5)
    if L == 2:
        l.configure(text="Старт через 6 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l6 = root.after(995, start_text5)

def start_text5():
    global l5
    if L == 1:
        l.configure(text="Start in 5 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l5 = root.after(995, start_text4)
    if L == 2:
        l.configure(text="Старт через 5 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l5 = root.after(995, start_text4)

def start_text4():
    global l4
    if L == 1:
        l.configure(text="Start in 4 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l4 = root.after(995, start_text3)
    if L == 2:
        l.configure(text="Старт через 4 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l4 = root.after(995, start_text3)

def start_text3():
    global l3
    if L == 1:
        l.configure(text="Start in 3 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l3 = root.after(995, start_text2)
    if L == 2:
        l.configure(text="Старт через 3 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l3 = root.after(995, start_text2)

def start_text2():
    global l2
    if L == 1:
        l.configure(text="Start in 2 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l2 = root.after(995, start_text1)
    if L == 2:
        l.configure(text="Старт через 2 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l2 = root.after(995, start_text1)

def start_text1():
    global l1
    if L == 1:
        l.configure(text="Start in 1 second", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l1 = root.after(900, start_text)
    if L == 2:
        l.configure(text="Старт через 1 секунду", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
        l1 = root.after(900, start_text)

def start_text():
    if L == 1:
        l.configure(text="Start in 10 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
    if L == 2:
        l.configure(text="Старт через 10 секунд", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height=2, width=23)
    l.place_forget()

def RU():
    text_message.configure(text="Введите сообщение:", font='Comfortaa 14', fg='#3d3d42', bg='#ccc', height=2)
    text_message_quantity.configure(text="Введите кол-во сообщений:", font='Comfortaa 14', fg='#3d3d42', bg='#ccc', height=2)
    start_button.configure(text='Старт', bg='#ccc', command=start)
    l.configure(text = "Старт через 10 секунд",  font = 'Comfortaa 10',  fg = '#3d3d42',  bg = '#ccc',  height = 2, width = 23)
    help_button.configure(text='Помощь', bg='#ccc', command=help)
    help_button.place(y=5, x=285)
    global L
    L = 2

def EN():
    text_message.configure(text="Enter a message:", font='Comfortaa 14', fg='#3d3d42', bg='#ccc', height=2)
    text_message_quantity.configure(text="Enter the quantity of messages:", font='Comfortaa 14', fg='#3d3d42', bg='#ccc', height=2)
    start_button.configure(text=' Start ', bg='#ccc', command=start)
    l.configure(text="Start in 10 seconds", font='Comfortaa 10', fg='#3d3d42', bg='#ccc', height = 2, width = 23)
    help_button.configure(text=' Help ', bg='#ccc', command=help)
    help_button.place(y=5, x=303)
    global L
    L = 1

def help():
    global L
    if L == 1:
        messagebox.showinfo('Help', 'Instructions for use:\n1)Enter data in the fields\n2) Click on the "Start" button\n3) Click on the message input field in the messenger\n4)Wait 10 seconds\n \nTo cancel spam, simply close the program window.')
    if L == 2:
        messagebox.showinfo('Помощь', 'Инструкция по использованию:\n1)Введите данные в поля\n2)Нажмите на кнопку "Старт"\n3)Нажмите на поле ввода сообщения в мессенджере\n4)Подождите 10 секунд\n \nЧтобы отменить спам, просто закройте окно программы.')

def spammer():
    m = message.get()
    m_q = message_quantity.get()
    global L
    try:
        for num in range(int(m_q)):
            for letter in str(m):
                Keyboard.press(letter)
                Keyboard.release(letter)
            Keyboard.press(Key.enter)
            Keyboard.release(Key.enter)
            time.sleep(0.1)
    except ValueError:
        if L == 1:
            messagebox.showerror('Error', 'You entered a letter or character in the string for numbers!')
        if L == 2:
            messagebox.showerror('Ошибка', 'Вы ввели букву или символ в строке для чисел!')

def start():
    m = message.get()
    m_q = message_quantity.get()
    global L
    global after_10sec1
    global after_10sec2
    if L == 2:
        if m and m_q:
            l.place(y=180, x=85)
            after_10sec2 = root.after(1000, start_text9)
            after_10sec1 = root.after(10000, spammer)
        if not m:
            if not m_q:
                messagebox.showerror('Ошибка', 'Введите сообщение!\n\nВведите кол-во сообщений!')
        if not m:
            if m_q:
                messagebox.showerror('Ошибка', 'Введите сообщение!')
        if not m_q:
            if m:
                messagebox.showerror('Ошибка', 'Введите кол-во сообщений!')

    if L == 1:
        if m and m_q:
            after_10sec1 = root.after(10000, spammer)
            after_10sec2 = root.after(1000, start_text9)
            l.place(y=180, x=85)
        if not m:
            if not m_q:
                messagebox.showerror('Error', 'Enter a message!\n\nEnter the quantity of messages!')
        if not m:
            if m_q:
                messagebox.showerror('Error', 'Enter a message!')
        if not m_q:
            if m:
                messagebox.showerror('Error', 'Enter the quantity of messages!')
    
# Настройки Окна

root = Tk()

root.resizable(width = False, height = False)
root.geometry("350x250")
root.title("Devil's Spammer")
root.iconbitmap('icon.ico')
root['bg'] = '#ccc'

# Text

text_message = Label(text="Enter a message:", font='Comfortaa 14',    fg = '#3d3d42',   bg = '#ccc',  height = 2)

message = Entry(root, fg = '#524646',  font = 'Consolas 12',  bg = '#ccc',  justify = 'center',  width = 30)

text_message_quantity = Label(text="Enter the quantity of messages:",  font='Comfortaa 14',  fg = '#3d3d42',  bg = '#ccc',  height = 2)

message_quantity = Entry(root, fg = '#524646',  font = 'Consolas 12',  bg = '#ccc',  justify = 'center',  width = 30)

l = Label(text = "Start in 10 seconds",  font = 'Comfortaa 10',  fg = '#3d3d42',  bg = '#ccc',  height = 2, width = 22)

by = Label(text = 'made by danzyxd and TretcH',font = 'Comfortaa 7',  fg = 'black',  bg = '#ccc')

version = Label(text = 'v0.1',font = 'Comfortaa 7',  fg = 'black',  bg = '#ccc')

# Buttons

ru_button = Button(text='RU', bg='#ccc', command=RU)

en_button = Button(text='EN', bg='#ccc', command=EN)

start_button = Button(text=' Start ',  bg='#ccc',  command=start)

help_button = Button(text=' Help ',  bg='#ccc',  command=help)

# Packer

text_message.pack()
message.pack()

text_message_quantity.pack()
message_quantity.pack()

by.place(x=-7, y=238, relwidth=0.4, relheight=0.05)
version.place(x=270, y=238, relwidth=0.4, relheight=0.05)

ru_button.place(y = 5, x = 35)
en_button.place(y = 5, x = 5)
start_button.place(y = 155, x = 155)
help_button.place(y = 5, x = 303)

root.mainloop()