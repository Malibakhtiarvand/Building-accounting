from tkinter import*
from tkinter import messagebox

widnow = Tk()
widnow.title('Revenues an expenses')
widnow.geometry('300x400')
widnow.configure(bg='red')


title_label = Label(widnow, text='موضوع', bg='red').pack()
title_input = Entry(widnow, bd=5)
title_input.pack(fill='x')

tozih_label = Label(widnow, text='توضیح', bg='red').pack()
tozih_input = Text(widnow, height=4)
tozih_input.pack()


# def checked(check:bool) -> bool:
#     return check

openTitleDotTxt=open('title.txt','r+')
listLine=openTitleDotTxt.readlines()

def writeCostAndIcomeInFile():
    ischeckedCost = cost_intVar.get()
    ischeckedIcome = Income_intVar.get()
    if ischeckedCost == 1:
        with open('money.txt', 'r+') as f:
            readFile = int(f.readlines()[-1])
            f.write('\n')
            f.write(str((readFile)-int(countMoney.get())))
    file=open('title.txt', 'r+')
    title_write = title_input.get()
    tozih_write = tozih_input.get('1.0','end-1c')
    listLine.append(f'{title_write} : {tozih_write} va bodje {readFile-int(countMoney.get())} gardid.\n')
    file.write(''.join(listLine))
    file.close()

def showReports(lineShow:int):
    messagebox.showinfo(listLine[lineShow][:listLine[lineShow].index(':')-1],listLine[lineShow])

idList=[0]  
def report_def ():
    widnowReport=Toplevel(widnow)
    widnowReport.title('reports')
    widnowReport.geometry('300x400')
    widnowReport.configure(bg='red')

    for i in listLine:
        Button(widnowReport,text=i[:i.index(':')-1],command=lambda:showReports(idList[-1])).pack()
        if len(idList) < len(listLine):
            idList.append(idList[-1]+1)
            print(idList)
    scrollItems=Scrollbar(widnowReport)
    scrollItems.pack( side = 'right', fill = 'y' )
    scrollItems.config()
    widnowReport.mainloop()


cost_intVar = IntVar()
Income_intVar = IntVar()

Cost = Checkbutton(widnow, text='هزینه',
                   variable=cost_intVar, offvalue=0, onvalue=1)
Cost.pack()


Income = Checkbutton(widnow, text='درآمد',
                     variable=Income_intVar, offvalue=0, onvalue=1)
Income.pack()

countMoneyLabel = Label(widnow, text='مقدار').pack()
countMoney = Entry(widnow)
countMoney.pack(fill='x')

finish = Button(widnow, text='انجام',
                command=writeCostAndIcomeInFile).pack(side='bottom')

report=Button(widnow,text='گزارشات',command=report_def).pack()

openTitleDotTxt.close()

widnow.mainloop()

