# import tkinter
from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100,y=100)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# my_label["text"] = "New text1"
#Button

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=2, row=0)



#Entry
input = Entry(width=10)
# input.pack()
# print(input.get())
input.grid(column=3, row=2)



window.mainloop()

