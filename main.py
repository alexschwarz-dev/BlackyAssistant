#Blacky Assisstant v0.2.0
import tkinter as tk
import tkinter
def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()
def home():
    clear_screen()
    startba()
def calculator():
    global button_calculator
    button_calculator.destroy()
    global button_notes
    button_notes.destroy()
    global button_information
    button_information.destroy()
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
    button_add = tkinter.Button(window, text="+", command=add, width=10, height=2, bg="gold")
    button_sub = tkinter.Button(window, text="-", command=sub, width=10, height=2, bg="gold")
    button_mul = tkinter.Button(window, text="*", command=mul, width=10, height=2, bg="gold")
    button_div = tkinter.Button(window, text="/", command=div, width=10, height=2, bg="gold")
    text_num1 = tkinter.Entry(window, width=24, bg="black", fg="gold")
    text_num2 = tkinter.Entry(window, width=24, bg="black", fg="gold")
    text_answer = tkinter.Entry(window, width=24, bg="black", fg="gold")
    label_num1 = tkinter.Label(window, text="Enter the first number",width=20, background="silver")
    label_num2 = tkinter.Label(window, text="Enter the second number",width=20, background="silver")
    label_answer = tkinter.Label(window, text="Operation result:",width=20, background="silver")
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


def startba():
    global button_notes
    global button_information
    global button_terminal
    global button_calculator
    button_start.destroy()
    button_calculator = tk.Button(window,text="Calculator",width=10,bg="black",fg="white",command=calculator)
    button_calculator.place(x=100,y=100)
    button_notes = tk.Button(window,text="Notes",width=10,bg="black",fg="white")
    button_notes.place(x=200,y=100)
    button_information = tk.Button(window,text="Information",width=10,bg="black",fg="white")
    button_information.place(x=300,y=100)
    button_terminal = tk.Button(window,text="Terminal",width=10,bg="black",fg="white")
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