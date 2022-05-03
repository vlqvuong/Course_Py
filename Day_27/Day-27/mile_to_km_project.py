from tkinter import *

def convert():
    mile_to_km = round(float(input.get()) * 1.609343)
    my_label3.configure(text=f"{mile_to_km}")

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=150)
window.configure(padx=50, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

my_label1 = Label(text="Miles")
my_label1.grid(column=2, row=0)

my_label2 = Label(text="is equal to")
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0")
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km")
my_label4.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()