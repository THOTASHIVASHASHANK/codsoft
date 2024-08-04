from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self,root):
        self.root = root
        self.root.title('TO-DO-LIST')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='TO-DO-LIST APP',
                           font='Arial, 25 bold', width=10, bg= 'blue', fg='green')
        self.label.pack(side='top',fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font='Arial, 18 bold',width=10,bd=5,bg='grey',fg='orange')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                            font='Arial, 18 bold',width=10,bd=5,bg='orange',fg='grey')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root,height=9,bd=5,width=23,font="Arial, 12")
        self.main_text.place(x=280, y=100)

        self.text= Text(self.root,bd=5,height=2,width=30,font='Arial, 10 bold')
        self.text.place(x=20, y=120)
    
                        #---------for adding tasks_____#
        
        self.add_button = Button(self.root, text='Add Task',command=self.add_task,font='Arial, 12 bold',width=20)
        self.add_button.place(x=20, y=180)

        self.delete_button = Button(self.root,text='Delete Task',command=self.delete_task,font='Arial, 12 bold', width=20)
        self.delete_button.place(x=20, y=220)

        self.load_tasks()

    def add_task(self):
        content =self.text.get(1.0,END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'w') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)

    def delete_task(self):
        selected_task_index = self.main_text.curselection()
        if self:
            self.main_text.delete(selected_task_index)
            self.save_tasks()
        
    def save_tasks(self):
        tasks =self.main_text.get(0, END)
        with open('data.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')

        
        
    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.main_text.insert(END, task.strip())
        except FileNotFoundError:
            pass


def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()



