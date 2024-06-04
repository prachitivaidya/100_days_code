from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tim = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(tim)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
reps = 0
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break ", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec ==0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = "0"+str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # prints 5:0 so use dynamic typing
    if count > 0:
        global tim
        tim = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# label
timer = Label(window, text="Timer", font=(FONT_NAME, 44, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(column=1, row=0)

check = Label(window, text="", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
check.grid(column=1, row=3)

# buttons
start = Button(text="Start", bg=YELLOW, command= start_timer, highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=YELLOW,command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)

# canvas
canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), anchor=CENTER)
canvas.grid(column=1, row=1)



window.mainloop()