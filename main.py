#Blacky Assisstant v0.2.0
import tkinter as tk
import tkinter
def calculator():
    global button_calculator
    global button_notes
    global button_terminal
    global button_information
    global startba
    global answer
    button_information.destroy()
    button_terminal.destroy()
    button_calculator.destroy()
    button_notes.destroy()
    def firstnumber():
        global number1
        entry_no1 = tk.Entry(window,width=10,bg="black",fg="white")
        entry_no1.place(x=100,y=100)
        number1 = entry_no1.get()
    def secondnumber():
        global number2
        entry_no2 = tk.Entry(window,width=10,bg="black",fg="white")
        entry_no2.place(x=200,y=100)
        number2 = entry_no2.get()
    def multiplication():
        global answer
        answer = number1 * number2
    def division():
        global answer
        answer = number1 / number2
    def addition():
        global answer
        answer = number1 + number2
    def subtraction():
        global answer
        answer = number1 - number2
    button_multi = tkinter.Button(window,text="*",width=10,bg="black",fg="white",command=multiplication)
    button_multi.place(x=100,y=200)
    button_sub = tkinter.Button(window,text="-",width=10,bg="black",fg="white",command=subtraction)
    button_sub.place(x=150,y=200)
    button_add = tk.Button(window,text="+",width=10,bg="black",fg="white",command=addition)
    button_add.place(x=200,y=200)
    button_div = tk.Button(window,text="/",width=10,bg="black",fg="white",command=division)
    button_div.place(x=250,y=200)
    label_answer = tk.Label(window,text=f"Answer:{answer}")
    label_answer.place(x=300,y=100)
def startba():
    global button_start
    global button_calculator
    global button_notes
    global button_terminal
    global button_information
    global startba
    button_start.destroy()
    button_calculator = tk.Button(window,text="Calculator",width=10,bg="black",fg="white",command=calculator)
    button_calculator.place(x=100,y=100)
    button_notes = tk.Button(window,text="Notes",width=10,bg="black",fg="white")
    button_notes.place(x=200,y=100)
    button_information = tk.Button(window,text="Information",width=10,bg="black",fg="white")
    button_information.place(x=300,y=100)
    button_terminal = tk.Button(window,text="Terminal",width=10,bg="black",fg="white")
    button_terminal.place(x=400,y=100)

window = tk.Tk()
window.title("Blacky Assisstant")
window.geometry("600x600")
label_blackyassisstant = tk.Label(window, text="Blacky Assisstant")
label_blackyassisstant.place(x=200, y=10)
label_welcome = tk.Label(window, text="Welcome to Blacky Assisstant")
label_welcome.place(x=170, y=50)
button_start = tk.Button(window,text="Start BA v0.2.0",bg="black",fg="white",command=startba)
button_start.place(x=200, y=250)







window.mainloop()