"""# GUI: Graphical User Interface
from tkinter import *

window = Tk()
# Create a window with tkinter.
window.title("My First GUI Program")
# Change title of window
window.minsize(width=500, height=300)
# set up the size of window is a 500-pixel by 300-pixel

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.configure(text="New Text")
# New Text show up instead of the original text.

# Button"""


"""def button_clicked():
    print("I got clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()"""


"""# Show "Button Got Clicked" on my_label when the button get's clicled:

def button_clicked():
    print("I got clicked")
    my_label.configure(text="Button Got Clicked")


button = Button(text="Click Me", command=button_clicked)
button.pack()"""


"""# Entry


input = Entry(width=10)
input.pack()
print(input.get())

# Show something we input to entry:


def button_clicked():
    print("I got clicked")
    my_label.configure(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()
# Mainloop is the thing that will keep the window on screen.
"""


"""# tkinter-widget-demo

from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()"""


from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)


window.mainloop()