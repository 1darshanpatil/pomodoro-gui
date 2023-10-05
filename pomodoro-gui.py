#!/usr/bin/env python3

import tkinter as tk
import datetime as _dt
import os

def play_work_sound():
    os.system('play -nq -t alsa synth {} sine {}'.format(.5, 2500))

def play_break_sound():
    os.system('play -nq -t alsa synth {} sine {}'.format(.5, 3500))

def play_pomodoro_end_sound():
    os.system('play -nq -t alsa synth {} sine {}'.format(.5, 4000))




class PomodoroTimer:
    def __init__(self, work_time=15, break_time=3, final_break_time=5):
        self.timer_running = False
        self.wrkt = work_time
        self.brkt = break_time
        self.frkt = final_break_time

        self.wrks = self.wrkt * 60
        self.brks = self.brkt * 60
        self.frks = self.frkt * 60

        self.set_of_counts = []
        self.u = range(0, self.wrks)
        self.v = range(self.wrks + self.brks, 2 * self.wrks + self.brks)
        self.w = range(2 * self.wrks + 2 * self.brks, 3 * self.wrks + 2 * self.brks)
        self.x = range(3 * self.wrks + 3 * self.brks, 4 * self.wrks + 3 * self.brks)
        for h in (self.u, self.v, self.w, self.x):
            self.set_of_counts.extend(h)


        self.end_of_pomodoro = 3 * (self.wrks + self.brks) + self.wrks + self.frks
        self.CLOCK_FONT_TYPE = "Cambria Math"
        self.LABEL_FONT = "Segoe Print"
        self.W = None
        self.tiik = "✔"
        self.raund = 1
        self.dlt = None

        self.window = tk.Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=10, pady=10, bg='white')

        self.lbl = tk.Label(text='Timer', fg="#1E212D", bg="white", font=(self.LABEL_FONT, 35))
        self.lbl.grid(row=0, column=1)

        #self.img = tk.PhotoImage(file="pomodoro-gui.png")
        self.img = tk.PhotoImage(file="/usr/share/icons/hicolor/512x512/apps/background.png")
        self.kyanvas = tk.Canvas(width=290, height=290, bg='white', highlightthickness=0)
        self.kyanvas.create_image(144.5, 144.5, image=self.img)
        self.text_kyanvas = self.kyanvas.create_text(148, 148, text="00:00", fill='#4d91c9',
                                                     font=(self.CLOCK_FONT_TYPE, 45, 'bold'))
        self.kyanvas.grid(row=1, column=1)

        self.str_btn = tk.Button(text="start", highlightthickness=0, command=self.start_f, bg='#2d5289', fg='white')
        self.str_btn.grid(row=2, column=0)

        self.rst_btn = tk.Button(text="reset", highlightthickness=0, command=self.rst_f, bg='#2d5289', fg='white')
        self.rst_btn.grid(row=2, column=2)

        self.tick_mark = tk.Label(text='', fg="green", bg="white", font=(35))
        self.tick_mark.grid(row=3, column=1)

    def count_down(self, count):
        if count in [self.u[0], self.v[0], self.w[0], self.x[0]]:
            self.dlt = self.wrks
            play_work_sound()

        elif count in [self.u[-1] + 1, self.v[-1] + 1, self.w[-1] + 1, self.x[-1] + 1]:
            self.dlt = self.brks
            play_break_sound()

        if count == self.end_of_pomodoro:
            play_pomodoro_end_sound()
        
        if count == self.end_of_pomodoro:
            print('Pomodoro Ended!')

        if count in self.set_of_counts:
            self.lbl.config(text="Work", fg='green')
            if count in [self.u[0], self.v[0], self.w[0], self.x[0]]:
                self.dlt = self.wrks
        elif count in [self.u[-1] + 1, self.v[-1] + 1, self.w[-1] + 1, self.x[-1] + 1]:
            self.lbl.config(text="Break", fg='red')
            self.dlt = self.brks
            if count == self.x[-1] + 1:
                self.dlt = self.frks
                self.lbl.config(text='Enjoy!', fg='pink')
            self.tick_mark.config(text=self.tiik)
            self.timer_running = False
            self.tiik += "✔"

        if count < self.end_of_pomodoro + 1:
            tm_txt = f'{_dt.timedelta(seconds=self.dlt)}'
            self.kyanvas.itemconfig(self.text_kyanvas, text=tm_txt[2:])
            self.W = self.window.after(1000, self.count_down, count + 1)
            self.dlt += -1

    
    def start_f(self):
        if not self.timer_running:  # Only start the timer if it's not already running
            # self.tiik = ""
            self.timer_running = True
            self.count_down(0)


    def rst_f(self):
        self.timer_running = False
        try:
            self.window.after_cancel(self.W)
            self.lbl.config(text='Timer', fg='black')
            self.kyanvas.itemconfig(self.text_kyanvas, text=f"00:00")
            self.tick_mark.config(text="")
            self.tiik = "✔"
        except ValueError:
            return print("You should not press reset before starting the timer.")


    def run_timer(self):
        self.window.mainloop()


# Make changes only to the below three variables.
work_time = 15
break_time = 3
final_break_time = 5

timer = PomodoroTimer(work_time, break_time, final_break_time)
timer.run_timer()

