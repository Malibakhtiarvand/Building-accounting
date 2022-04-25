from tkinter import*

widnow=Tk()
widnow.title('Revenues an expenses')
widnow.geometry('300x400')
widnow.configure(bg='red')


title_label=Label(widnow,text='موضوع',bg='red').pack()
title_input=Entry(widnow,bd=5)
title_input.pack(fill='x')

tozih_label=Label(widnow,text='توضیح',bg='red').pack()
tozih_input=Text(widnow,height=4)
tozih_input.pack()


# def checked(check:bool) -> bool:
#     return check

def writeCostAndIcomeInFile ():
    ischeckedCost = cost_intVar.get()
    ischeckedIcome = Income_intVar.get()
    if ischeckedCost == 1:
        with open('money.txt','r+') as f:
            readFile=int(f.readlines()[-1])
            print(readFile)
            f.write('\n')
            f.write(str((readFile)-int(countMoney.get())))




cost_intVar=IntVar()
Income_intVar=IntVar()
Cost=Checkbutton(widnow,text='هزینه',variable=cost_intVar,offvalue=0,onvalue=1)
Cost.pack()


Income=Checkbutton(widnow,text='درآمد',variable=Income_intVar,offvalue=0,onvalue=1)
Income.pack()

countMoneyLabel = Label(widnow,text='مقدار').pack()
countMoney = Entry(widnow)
countMoney.pack(fill='x')

finish=Button(widnow,text='انجام',command=writeCostAndIcomeInFile).pack(side='bottom')







widnow.mainloop()
