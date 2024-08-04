from tkinter import*
#function to update the display when a button is pressed
def button_click(number):
    global operator
    operator += str(number)
    input_value.set(operator)

#function to clear the display
def button_clear():
    global operator
    operator=""
    input_value.set("")

#function to calculate the result
def button_equal():
    global operator
    try:
        result = str(eval(operator))
        input_value.set(result)
        operator=result
    except:
        input_value.set("error")
        operator=""

#initilizes main window
main=Tk()
main.title("Calculator")

#initilize global variables 
operator=" "
input_value= StringVar()

#Display text
display_text=Entry(main,font=("Arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,bg="grey",justify=RIGHT)
display_text.grid(columnspan=4)
#create buttons with specified properties 
def create_button(text,row,column,command):
    button = Button(main,padx=16,bd=8,fg="black",font=("Arial",20,"bold"),text=text,command=command)
    button.grid(row=row,column=column)

buttons=[('7',1,0,lambda:button_click(7)),('8',1,1,lambda:button_click(8)),('9',1,2,lambda:button_click(9)),('/',1,3,lambda:button_click('/')),
         ('4',2,0,lambda:button_click(4)),('5',2,1,lambda:button_click(5)),('6',2,2,lambda:button_click(6)),('*',2,3,lambda:button_click('*')),
         ('1',3,0,lambda:button_click(1)),('2',3,1,lambda:button_click(2)),('3',3,2,lambda:button_click(3)),('-',3,3,lambda:button_click('-')),
         ('0',4,0,lambda:button_click(0)),('c',4,1,button_clear),('=',4,2,button_equal),('+',4,3,lambda:button_click('+'))]
#create and place buttons on the grid 
for(text,row,column,command)in buttons:
    create_button(text,row,column,command)
#start the Tkinter event loop
main.mainloop()
