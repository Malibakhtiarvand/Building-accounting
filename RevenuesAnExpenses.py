from tkinter import*
from tkinter import messagebox
from typing import ChainMap

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
    root = Tk()

    root.title('Full Window Scrolling X Y Scrollbar Example')

    root.geometry("1350x400")



    # Create A Main frame

    main_frame = Frame(root)

    main_frame.pack(fill=BOTH,expand=1)



    # Create Frame for X Scrollbar

    sec = Frame(main_frame)

    sec.pack(fill=X,side=BOTTOM)



    # Create A Canvas

    my_canvas = Canvas(main_frame)

    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)



    # Add A Scrollbars to Canvas

    x_scrollbar = Scrollbar(sec,orient=HORIZONTAL,command=my_canvas.xview)

    x_scrollbar.pack(side=BOTTOM,fill=X)

    y_scrollbar = Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    y_scrollbar.pack(side=RIGHT,fill=Y)



    # Configure the canvas

    my_canvas.configure(xscrollcommand=x_scrollbar.set)

    my_canvas.configure(yscrollcommand=y_scrollbar.set)

    my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 



    # Create Another Frame INSIDE the Canvas

    second_frame = Frame(my_canvas)



    # Add that New Frame a Window In The Canvas

    my_canvas.create_window((0,0),window= second_frame, anchor="nw")


    count=0
    for i in listLine:
        dictItem=[]
        dictItem.append([i,count])
        count+=1
        items=Button(second_frame,text=i[:i.index(':')-1])
        items['command']=lambda:showReports()


    if len(idList) < len(listLine):
        idList.append(idList[-1]+1)
        print(idList)

    # for thing in listLine:
    #     Button(second_frame ,text=thing[:thing.index(':')-1],command=lambda:showReports(listLine.index(thing))).pack()



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

