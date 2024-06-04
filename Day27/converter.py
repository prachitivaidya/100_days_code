from tkinter import *

# window
window = Tk()
window.title('Miles to Km Converter')
window.minsize(300, 150)
window.config(padx=20, pady=20)


# labels
is_equal = Label(window, text="is equal to", font=("Helvetica", 24, "bold"))
is_equal.grid(column=0, row=1)

ans = Label(window, text="0", font=("Helvetica", 24, "bold"))
ans.grid(column=1, row=1)

miles = Label(window, text="Miles", font=("Helvetica", 24, "bold"))
miles.grid(column=2, row=0)

km = Label(window, text="Km", font=("Helvetica", 24, "bold"))
km.grid(column=2, row=1)


# button
def btn_clicked():
    a = int(input.get()) * 1.609
    ans.config(text=f"{a}")

    print("Button clicked")

button  = Button(text="Calculate", command=btn_clicked)
button.grid(column=1, row=2)


# entry
input = Entry(width=10)
# print(input.get())
input.grid(column=1, row=0)
window.mainloop()