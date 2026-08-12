#I have no clue how I wrote that code
total_hours_wasted = 10
#Blacky Assisstant v0.3.2
import tkinter as tk
import tkinter
import os
import platform
import psutil
import socket
import sys
import shutil
import subprocess
def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()
def home():
    clear_screen()
    startba()

def calculator():
    window_calculator = tk.Toplevel()
    window_calculator.title("Calculator")
    window_calculator.geometry("500x500")
    global button_calculator
    button_calculator.destroy()
    global button_notes
    button_notes.destroy()
    global button_informations
    button_informations.destroy()
    global button_terminal
    button_terminal.destroy()
    def get_num1():
        num1 = int(text_num1.get())
        return num1
    def get_num2():
        num2 = int(text_num2.get())
        return num2
    def set_answer(result):
        text_answer.delete(0, "end")
        text_answer.insert(0, result)
    def add():
        num1 = get_num1()
        num2 = get_num2()
        result = num1 + num2
        set_answer(result)
    def sub():
        num1 = get_num1()
        num2 = get_num2()
        result = num1 - num2
        set_answer(result)
    def mul():
        num1 = get_num1()
        num2 = get_num2()
        result = num1 * num2
        set_answer(result)
    def div():
        num1 = get_num1()
        num2 = get_num2()
        result = num1 / num2
        set_answer(result)
    button_add = tkinter.Button(window_calculator, text="+", command=add, width=10, height=2, bg="gold")
    button_sub = tkinter.Button(window_calculator, text="-", command=sub, width=10, height=2, bg="gold")
    button_mul = tkinter.Button(window_calculator, text="*", command=mul, width=10, height=2, bg="gold")
    button_div = tkinter.Button(window_calculator, text="/", command=div, width=10, height=2, bg="gold")
    text_num1 = tkinter.Entry(window_calculator, width=24, bg="black", fg="gold")
    text_num2 = tkinter.Entry(window_calculator, width=24, bg="black", fg="gold")
    text_answer = tkinter.Entry(window_calculator, width=24, bg="black", fg="gold")
    label_num1 = tkinter.Label(window_calculator, text="Enter the first number",width=20, background="silver")
    label_num2 = tkinter.Label(window_calculator, text="Enter the second number",width=20, background="silver")
    label_answer = tkinter.Label(window_calculator, text="Operation result:",width=20, background="silver")
    label_num1.place(x=200, y=80)
    label_num2.place(x=200, y=120)
    label_answer.place(x=200, y=280)
    text_num1.place(x=200, y=100)
    text_num2.place(x=200, y=140)
    button_add.place(x=200, y=180)
    button_sub.place(x=270, y=180)
    button_mul.place(x=200, y=220)
    button_div.place(x=270, y=220)
    text_answer.place(x=200, y=300)
    button_homee = tkinter.Button(window_calculator, text="HOME", width=10, bg="white", fg="black",command=window_calculator.destroy)
    button_homee.place(x=0, y=0)
def notes():
    print("Notes button working")
def terminal():
    print("Terminal button working")
    terminal_window = tk.Toplevel(window)
    terminal_window.title("Blacky Terminal")
    terminal_window.geometry("600x600")
    output = tk.Text(terminal_window, bg="black",fg="green",insertbackground="white")
    output.pack(fill="both",expand=True)
    command_entry=tk.Entry(terminal_window,bg="black",fg="white",insertbackground="white")
    command_entry.pack(fill="x")
    def run_command():
        command = command_entry.get()
        if not command:
            return
        try:
            result = subprocess.run(command,shell=True,capture_output=True,text=True)
            output.insert("end",f">{command}\n")
            output.insert("end", result.stdout)
            output.insert("end", result.stderr)
        except Exception as e:
            output.insert("end",f"Error: {e}\n")
    button_run = tk.Button(terminal_window,text="Run",bg="black",fg="white",command=run_command)
    button_run.pack()
    button_homee = tkinter.Button(terminal_window, text="HOME", width=10, bg="white", fg="black",command=terminal_window.destroy)
    button_homee.pack()
def get_gpu_info():
    try:
        if platform.system() == "Windows":
            return subprocess.check_output(
                [
                    "powershell",
                    "-Command",
                    "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"
                ],
                text=True
            ).strip()

        elif platform.system() == "Linux":
            return subprocess.check_output(
                ["bash", "-c", "lspci | grep -Ei 'VGA|3D|Display'"],
                text=True
            ).strip()

        else:
            return "Unknown"

    except Exception as e:
        return f"GPU information unavailable: {e}"
def information():

    gpu_info = get_gpu_info()
    global button_notes
    global button_informations
    global button_terminal
    global button_calculator
    button_calculator.destroy()
    button_notes.destroy()
    button_terminal.destroy()
    button_informations.destroy()
    info_window = tk.Toplevel()
    info_window.title("Blacky Assisstant - Information")
    info_window.geometry("900x720")
    button_homeee = tkinter.Button(info_window, text="HOME", width=10, bg="white", fg="black",command=info_window.destroy)
    button_homeee.place(x=0, y=0)

    system_info = f"""
BLACKY ASSISSTANT
===============================

BLACKY ASSISSTANT INFORMATION
VERSION: 0.4.0
STATUS: Running
GUI: Tkinter
Python: {platform.python_version()}

SYSTEM INFO
===============================

Operating System: {platform.system()}
OS Version: {platform.version()}
Kernel: {platform.release()}
Architecture: {platform.machine()}
Hostname: {socket.gethostname()}

HARDWARE INFO
===============================

Processor: {platform.processor()}
CPU Usage: {psutil.cpu_percent()}%
RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB
RAM Usage {psutil.virtual_memory().percent}%
GPU: {gpu_info}

STORAGE
===============================

Disk Total: {round(psutil.disk_usage('/').total / (1024**3), 2)} GB
Disk Usage {psutil.disk_usage('/').percent}%
Disk Used: {round(psutil.disk_usage('/').used / (1024**3), 2)} GB
Disk Free: {round(psutil.disk_usage('/').free / (1024**3), 2)} GB

"""
    label_systeminfo = tk.Label(
        info_window,
        text=system_info,
        justify="left",
        font=("Consolas", 11),
        bg="black",
        fg="green"
    )

    label_systeminfo.pack(
        padx=0,
        pady=(20,0),
        anchor="w"
    )

def startba():
    button_knock = tk.Button(window,text="KNOCKOUT",bg="red",fg="black",command=window.destroy)
    button_knock.place(x=200,y=450)
    global button_notes
    global button_informations
    global button_terminal
    global button_calculator
    button_start.destroy()
    button_calculator = tk.Button(window,text="Calculator",width=10,bg="black",fg="white",command=calculator)
    button_calculator.place(x=100,y=100)
    button_notes = tk.Button(window,text="Notes",width=10,bg="black",fg="white",command=notes)
    button_notes.place(x=200,y=100)
    button_informations = tk.Button(window,text="Information",width=10,bg="black",fg="white",command=information)
    button_informations.place(x=300,y=100)
    button_terminal = tk.Button(window,text="Terminal",width=10,bg="black",fg="white",command=terminal)
    button_terminal.place(x=400,y=100)
    button_exit = tk.Button(window, text="Home", width=10, bg="black", fg="white", command=home)
    button_exit.place(x=200, y=500)


window = tk.Tk()
window.title("Blacky Assisstant")
window.geometry("600x600")
label_blackyassisstant = tk.Label(window, text="Blacky Assisstant")
label_blackyassisstant.place(x=200, y=10)
label_welcome = tk.Label(window, text="Welcome to Blacky Assisstant")
label_welcome.place(x=170, y=50)
button_start = tk.Button(window,text="Start Blacky Assisstant v0.2.0",bg="black",fg="white",command=startba)
button_start.place(x=200, y=250)



window.mainloop()