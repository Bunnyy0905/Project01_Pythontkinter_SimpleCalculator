from tkinter import *
root=Tk()
root.geometry("570x570+100+200")
root.resizable(False,False) #resizable()--> used to allow Tkinter root window to change it’s size according to the user's need (as well) we can prohibit resizing of the Tkinter window i.e.user will not able to minimize or maximize the root window
root.title("Simple Calculator")
root.config(bg="#17161b")

equation="" #defining equation

#defining show()
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

#defining clear()
def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""

    if (equation!=""):
        try:
            result=eval(equation)
        except:
            result="errror"
    label_result.config(text=result)

#Creating Result Bar
label_result=Label(root,width=25,height=2,text="",font=("arial", 30),bg="powder blue",borderwidth=10, relief=SUNKEN )
label_result.pack()
# justify="right"

#Creating Buttons
Button(root,text="C",width=5,height=1,font=("arial", 30, "bold"), borderwidth=1, relief=RAISED, fg="#fff", bg="#BF0A30",command=lambda:clear()).place(x=10,y=120)   #place() --> used to position buttons based on x,y coordinates in a frame
Button(root,text="/",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda:show("/")).place(x=150,y=120)
Button(root,text="%",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda:show("%")).place(x=290,y=120)
Button(root,text="*",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda:show("*")).place(x=430,y=120)

Button(root,text="7",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("7")).place(x=10,y=210)   
Button(root,text="8",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("8")).place(x=150,y=210)
Button(root,text="9",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("9")).place(x=290,y=210)
Button(root,text="-",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda:show("-")).place(x=430,y=210)

Button(root,text="4",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("4")).place(x=10,y=300)   
Button(root,text="5",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda:show("+")).place(x=430,y=300)

Button(root,text="1",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("1")).place(x=10,y=390)   
Button(root,text="2",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("2")).place(x=150,y=390)
Button(root,text="3",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("3")).place(x=290,y=390)

Button(root,text="0",width=11,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("0")).place(x=10,y=480)
Button(root,text=".",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show(".")).place(x=290,y=480)   
Button(root,text="=",width=5,height=3,font=("arial", 30, "bold"), borderwidth=1, relief=RAISED, fg="#fff", bg="#fe9037",command=lambda:calculate()).place(x=430,y=390)

root.mainloop()

##5bb450