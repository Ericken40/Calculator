from tkinter import *
from tkinter import ttk
from functions import *

color1 = '#261919'
color2 = '#feffff'
color3 = '#38576b'
color4 = '#F0F0F2'
color5 = '#261919'

window = Tk()
window.title('Calculator')
window.geometry('235x309')
window.config(bg=color1)
window.resizable(width=0, height=0)


frame_screen = Frame(window, width=235, height=50, bg=color1)
frame_screen.grid(row=0, column=0)

frame_key = Frame(window, width=235, height=268)
frame_key.grid(row=1, column=0)

app_text = StringVar()
app_label = Label(
    frame_screen,
    textvariable=app_text,
    width=15,
    height=2,
    padx=1,
    pady=1,
    relief=FLAT,
    anchor=E,
    justify=RIGHT,
    font=('Ivy 18 bold'),
    bg=color1,
    fg=color2,
)
app_label.place(x=0, y=0)

b1 = Button(
    frame_key,
    command=lambda: app_text.set(clear()),
    text='C',
    width=11,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b1.place(x=0, y=0)

b2 = Button(
    frame_key,
    command=lambda: app_text.set(percent()),
    text='%',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b2.place(x=120, y=0)

b3 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key(div())),
    text='÷',
    width=5,
    height=2,
    bg=color5,
    fg=color2,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b3.place(x=177, y=0)

b4 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('7')),
    text='7',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b4.place(x=0, y=52)

b5 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('8')),
    text='8',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b5.place(x=60, y=52)

b6 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('9')),
    text='9',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b6.place(x=120, y=52)

b7 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key(times())),
    text='x',
    width=5,
    height=2,
    bg=color5,
    fg=color2,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b7.place(x=177, y=52)

b8 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('4')),
    text='4',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b8.place(x=0, y=104)

b9 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('5')),
    text='5',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b9.place(x=60, y=104)

b10 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('6')),
    text='6',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b10.place(x=120, y=104)

b11 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key(minus())),
    text='-',
    width=5,
    height=2,
    bg=color5,
    fg=color2,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b11.place(x=177, y=104)

b12 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('1')),
    text='1',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b12.place(x=0, y=156)

b13 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('2')),
    text='2',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b13.place(x=60, y=156)

b14 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('3')),
    text='3',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b14.place(x=120, y=156)

b15 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key(plus())),
    text='+',
    width=5,
    height=2,
    bg=color5,
    fg=color2,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b15.place(x=177, y=156)

b16 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('0')),
    text='0',
    width=11,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b16.place(x=0, y=208)

b17 = Button(
    frame_key,
    command=lambda: app_text.set(enter_key('.')),
    text='.',
    width=5,
    height=2,
    bg=color4,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b17.place(x=120, y=208)

b18 = Button(
    frame_key,
    command=lambda: app_text.set(result()),
    text='=',
    width=5,
    height=2,
    bg=color5,
    fg=color2,
    font=('Ivy 13 bold'),
    relief=RAISED,
    overrelief=RIDGE,
)
b18.place(x=177, y=208)

window.mainloop()
