import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def add_entry_text():

    global entry, button, label, label_num, button_rm, cb
    global i
    
    i += 1

    # 현재 entry의 텍스트 가져오기
    text = tk.Entry.get(entry)
    
    # 입력 내용 출력 
    label_num = tk.Label(root, text="{}.".format(i-1))
    label_num.grid(row=i-1,column=0,padx=0)
    label = tk.Label(root, text=text)
    label.grid(row=i-1,column=1,padx=10)
    button_rm = tk.Button(root, text="제거")# + , command=remove_lebel
    button_rm.grid(row=i-1,column=2,padx=10)
    # 완료 버튼 생성
    cb = tk.Checkbutton(root, text="완료", variable=var)
    cb.grid(row=i-1, column=3, padx=10)
    
    # 기존 entry, button 삭제
    tk.Entry.destroy(entry)
    tk.Button.destroy(button)



    # 새로운 entry,button,combobox 생성
    entry = tk.Entry(root, width=30) # entry
    entry.grid(row=i+1, column=0, padx=5)
    button = tk.Button(root, text="추가", command=add_entry_text) # button
    button.grid(row=i+1, column=1, padx=5)
    
    


root = tk.Tk()
root.title("Entry 추가 예시")
root.geometry("500x1000")
var = tk.IntVar()   # 체크 여부 저장 (0 or 1)


i = 1

# 타이틀
label_title = tk.Label(root, text="To do List")
label_title.grid(row=0, column=1, padx=10)

entry = tk.Entry(root, width=30)
entry.grid(row=i, column=0, padx=5)

button = tk.Button(root, text="추가", command=add_entry_text)
button.grid(row=i, column=1, padx=5)



root.mainloop()
