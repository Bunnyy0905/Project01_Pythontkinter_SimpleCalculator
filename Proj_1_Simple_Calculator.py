from tkinter import *
root=Tk()

root.geometry("570x570+100+50")   #root.geometry("570x570")--> geometry()--> used to fix your page size (i.e.Screen, where w=570 and h=570) 
# Note:- root.geometry("570x570+100+50")--> used to show window at different position. The window is appearing at (100 shifted on X-axis and 50 shifted on Y-axis).
root.resizable(False,False)       #resizable()--> used to allow root window to change it’s size according to the user's need (as well) we can prohibit resizing of the Tkinter window 
                                                         # i.e.user will not able to minimize or maximize the root window
root.title("Simple Calculator")     #title()--> used to give name to your Screen(i.e. parent window)
root.config(bg="#17161b")           #config()--> not just to change the text. Also, it is used to change the background color

equation=""     #Global variable declaration

# equation is a global variable
#Note:- We can access the global variable. But can't modify the value of global variable inside a function. 
#If you try to modify the global variable value inside a function, it will throw an UnboundLocalError, because while modifying Python treats it as a local variable, as it is not defined inside the function. 
# Therefore, to define it as a local variable, we have to define it, with help of keyword 'global' inside a function.
 # global keyword --> used to make changes in the global variable in a local context. The keyword ‘global’ is also used to create or declare a global variable inside a function. 
def show(value):
    global equation    #declaring a global variable inside a function 
    equation+=value    #changing value of global variable in a local context;  equation+=value--> equation=equation+value 
    label_result.config(text=equation)  #config() function--> used to simply change the text on a label.

#defining clear()
def clear():
    global equation     #declaring a global variable inside a function 
    equation=""         #changing value of global variable in a local context
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

def delete():
    global equation
    equation=equation.rstrip(equation[-1])
    label_result.config(text=equation)
#Note:- rstrip. The string method, rstrip removes the characters from the right side of the string that is given to it. So, we can use it to remove the last element of the string. 

#Creating Result Bar -->By using label widget
label_result=Label(root,width=24,height=2,text="",anchor="e",font=("arial", 30),bg="powder blue",borderwidth=10, relief=SUNKEN )    #Note:- anchor="e",inside label widget--> used to display the entered values from right in the result bar; relief is an attribute of label widget used to give border styling --> SUNKEN, RAISED, SOLID, GROOVE, RIDGE
label_result.pack(anchor="nw")  #anchor=nw--> used to place the Result Bar on the Top-Left  

#Creating Buttons
Button(root,text="C",width=5,height=1,font=("arial", 30, "bold"), borderwidth=1, relief=RAISED, fg="#fff", bg="#BF0A30",command=lambda:clear()).place(x=10,y=120)   #place() --> used to position a widget based on x,y coordinates in a frame
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

Button(root,text="DEL",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#5bb450",command=lambda:delete()).place(x=10,y=480)
Button(root,text="0",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show("0")).place(x=150,y=480)
Button(root,text=".",width=5,height=1,font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda:show(".")).place(x=290,y=480)   
Button(root,text="=",width=5,height=3,font=("arial", 30, "bold"), borderwidth=1, relief=RAISED, fg="#fff", bg="#fe9037",command=lambda:calculate()).place(x=430,y=390)

root.mainloop()

