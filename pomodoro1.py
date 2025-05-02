import time
import tkinter as tk

def run_pomodoro(duration_seconds, update_callback=None, label="Timer"):
    while duration_seconds > 0:
        minutes = duration_seconds // 60
        sec = duration_seconds % 60
        if update_callback:
            update_callback(f"{label} - {minutes}:{sec:02}") 
            time.sleep(1)
        duration_seconds -= 1
    if update_callback:    
        update_callback(f"{label}selesai")
    

                   
            
