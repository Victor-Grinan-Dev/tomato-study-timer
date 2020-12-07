import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time as tm
from study_timer import tomato_timer_script as tts

window = tk.Tk()
window.title('Tomato Timer')

window.iconbitmap(r'tomato.ico')
# window.geometry('485x275')
window.resizable(width=False, height=False)
window.configure(bg="black")


def display_time():
    current_time = tm.strftime('%H:%M:%p')
    clock_label['text'] = current_time
    window.after(1000, display_time)  # corrects the lost of 1ms per second calling func every 1000 ms...


def popout():
    global study_counter
    global tomatos_eraned

    if study_counter:

        tk.messagebox.showwarning("Time up!", "You erned a tomato!!", icon="info")
        response = tk.messagebox.askquestion("Ready?", "continue to rest?", icon="question")
        if response == "yes":
            tts.countdown(rest_time)
            study_counter = False
            tomatos_eraned *= 1
    else:
        tk.messagebox.showwarning("Time up!", "You Lazy bastard!!", icon="info")
        response = tk.messagebox.askquestion("Ready?", "Earn 1 more tomato?", icon="question")

        if response == "yes":
            tts.countdown(rest_time)
            study_counter = True

def subject_panel():
    top = tk.Toplevel(bg='black')
    entry = tk.Entry(top)
    entry.pack()
    sudmit = tk.Button(top, text="add")
    sudmit.pack()


clock_label = tk.Label(window, font='ariel 80', bg='black', fg='red')
clock_label.grid(row=0, column=0, columnspan=3)

counter_label = tk.Label(window, text="00:00", font='ariel 80', bg='black', fg='red')
counter_label.grid(row=1, column=0, columnspan=3)

start = tk.Button(window, text="start", command=tts.countdown)
start.grid(sticky="w")

study_entry_label = tk.Label(window, text="Study Time", fg="white", bg="black")
study_entry_label.grid(row=2, column=1, sticky="e")

study_entry = tk.Entry(window, width=5)
study_entry.grid(row=2, column=2, sticky="w")

rest_entry_label = tk.Label(window, text="Rest Time", fg="white", bg="black")
rest_entry_label.grid(row=2, column=3, sticky="e")

rest_entry = tk.Entry(window, width=5)
rest_entry.grid(row=2, column=4, sticky="w")

load = Image.open("tomato.ico")
render = ImageTk.PhotoImage(load)
img = tk.Label(window, image=render, bg="black", width=100, height=100)
img.image = render
img.grid(row=3, column=0, sticky="w")

frame1 = tk.Frame(window, bg='black')
frame1.grid(row=0, column=3)
studies = ["general", "math"]
row = 0

for subject in studies:
    radio = tk.Radiobutton(frame1, bg="black")
    radio.grid(row=row, column=0, sticky="e")

    #  deselect the radio buttons

    label = tk.Label(frame1, text=subject, bg="black", fg="white")
    label.grid(row=row, column=1, sticky="w")
    row += 1

add_subject = tk.Button(window, text='edit_subjects', command=subject_panel)
add_subject.grid(row=0, column=3, sticky="n")

display_time()
window.mainloop()
