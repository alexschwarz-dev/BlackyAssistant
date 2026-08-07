#Blacky Assisstant v0.2.0
import tkinter as tk
import tkinter
def startba():
    button_calculator = tk.Button(window,text="Calculator",width=10,bg="black",fg="white")
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