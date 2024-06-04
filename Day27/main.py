from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# label
my_label = Label(window, text="My Label", font=("Helvetica", 24, "bold"))
my_label.config(text = "New Text")
my_label.grid(column=0, row=0)


#button
def btn_clicked():

    #my_label.config(text=f"{text}")
    print("Button clicked")

button2  = Button(text="New Button", command=btn_clicked)
button2.grid(column=2, row=0)
button = Button(text="Click Me", command=btn_clicked)
button.grid(column=1, row=1)


#entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
window.mainloop()

