from tkinter import*

widnow=Tk()
widnow.geometry('300x400')
widnow.configure(bg='red')


title_label=Label(widnow,text='موضوع',bg='red').pack()
title_input=Entry(widnow,bd=5)
title_input.pack(fill='x')

tozih_label=Label(widnow,text='توضیح',bg='red').pack()
tozih_input=Text(widnow,height=4)
tozih_input.pack()


cost_intVar=IntVar()
Income_intVar=IntVar()
Cost=Checkbutton(widnow,text='هزینه',variable=cost_intVar,offvalue=0,onvalue=1)
Cost.pack()


Income=Checkbutton(widnow,text='درآمد',variable=Income_intVar,offvalue=0,onvalue=1)
Income.pack()

finish=Button(widnow,text='انجام').pack(side='bottom')







widnow.mainloop()
