import tkinter as tk
from tkinter import messagebox

    

def remove_lebel():
    global entry, button, label, label_num, button_rm
    global i
    global label_list

    tk.Label.destroy(label_num)
    tk.Label.destroy(label)
    tk.Button.destroy(button_rm)

    i -= 1

root = tk.Tk()
root.title("Entry 추가 예시")
root.geometry("1000x2000")


i = 1

# 타이틀
label_title = tk.Label(root, text="To do List")
label_title.grid(row=0, column=1, padx=10)

entry = tk.Entry(root, width=30)
entry.grid(row=i, column=0, padx=5)

button = tk.Button(root, text="추가") # add label command 추가
button.grid(row=i, column=1, padx=5)


root.mainloop()