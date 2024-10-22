import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Live Clock")

def update_time():
    current_time = strftime('%I:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  

time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
time_label.pack(anchor='center')

update_time()

root.mainloop()
