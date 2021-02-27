import tkinter as tk
# import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
check_list = []
timer = None
# check_string = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    rep = 0
    check_list = []
    timer_label.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    work_sec = WORK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    rep += 1
    if rep % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        countdown_timer(5)
    elif rep % 2 == 0 and rep % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown_timer(3)
    else:
        timer_label.config(text="Break", fg=PINK)
        countdown_timer(2)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown_timer(count):
    global timer
    # global check_list, rep
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    # if count_sec < 10:
    #     # canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
    #     count_sec =
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # print(count)
    if count > 0:
        timer = window.after(1000, countdown_timer, count-1)
    else:
        start_timer()
        # work_sessions = rep // 2
        # mark = ""
        # for sessions in range(work_sessions):
        #     mark += "✔"

        if rep % 2 == 0:
            check_list.append("✔")
            check_string = "".join([item for item in check_list])
            # for item in check_list:
            #     check_string += item
            check_label.config(text=check_string)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas
canvas = tk.Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)
# count_down()

# label
timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
timer_label.grid(row=0, column=1)

check_label = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "normal"))
check_label.grid(row=3, column=1)

# Button
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
