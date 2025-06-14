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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="TIMER")



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    #count_down(5*60)
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        count_down(short_break_sec)
        text_label.config(text=f"BREAK", fg=RED)
        reps += 1
    elif reps % 8 == 0:
        count_down(long_break_sec)
        text_label.config(text=f"BREAK", fg=PINK)
        reps += 1
    else:
        count_down(work_sec)
        text_label.config(text=f"BREAK", fg=GREEN)
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = "0" + str(count_seconds)
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodaro")
window.config(padx=100, pady=100, bg=YELLOW)
text_label = Label(text="TIMER", fg="GREEN", bg="YELLOW", font=(FONT_NAME, 50))
text_label.grid(column=1, row=0)

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0 , command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
