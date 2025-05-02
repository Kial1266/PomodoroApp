import tkinter as tk
import time
import threading
from pomodoro1 import run_pomodoro

def start_focus():
    try:
        minutes = int (entry.get())
        thread = threading.Thread(target=run_pomodoro, args=(minutes * 60, update_label, "pomodor"))
        thread.start()
    except ValueError:
        update_label ("Masukan Inputan Yang Valid")    


def start_istirahat():
    try:
        minutes = int(entry.get())
        thread = threading.Thread(target=run_pomodoro, args=(minutes*60, update_label< "Istirahat"))
        thread.start()
    except ValueError:
            update_label("Masukan Inputan Yang Valid")
        
def update_label(text):
    label.config(text=text)
                                            
root = tk.Tk() 
root.title ("Pomodoro Interface")
root.geometry ("300x200")
label = tk .Label(root, text="Pomodoro")

entry = tk.Entry(root)
entry.pack(pady=10)


button_fokus = tk. Button(root, text="Mulai Pomodoro", command=start_focus)
button_istirahat = tk. Button(root, text="Segeralah Istirahat", command=start_istirahat) 
label = tk.Label(root, text="Pomodoro")

button_fokus.pack(pady=5)
button_istirahat.pack(pady=5)
label.pack(pady=20)

root.mainloop()   