import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def add_entry_text():

    global entry, button, label, label_num, button_rm, cb, label_Dday
    global i
    global label_list
    
    i += 1

    # 현재 entry의 텍스트 가져오기
    text = tk.Entry.get(entry)
    year = ttk.Combobox.get()
    month = ttk.Combobox.get(month_cb)
    day = ttk.Combobox.get(day_cb)

    # 입력 내용 출력 
    label_num = tk.Label(root, text="{}.".format(i-1))
    label_num.grid(row=i-1,column=0,padx=0)
    label = tk.Label(root, text=text)
    label.grid(row=i-1,column=1,padx=10)
    button_rm = tk.Button(root, text="제거", command=remove_lebel)
    button_rm.grid(row=i-1,column=2,padx=10)
    # 완료 버튼 생성
    cb = tk.Checkbutton(root, text="완료", variable=var)
    cb.grid(row=i-1, column=3, padx=10)
    #입력 날짜 표시
    label_Dday = tk.Label(root, text="{}.{}.{}".format(ttk.Combobox.get(year),ttk.Combobox.get(month),ttk.Combobox.get(day)))
    label_Dday.grid(row=i-1,column=1,padx=10)

    # 기존 entry, button 삭제
    tk.Entry.destroy(entry)
    tk.Button.destroy(button)
    ttk.Combobox.destroy(cb)


    # 새로운 entry,button,combobox 생성
    entry = tk.Entry(root, width=30) # entry
    entry.grid(row=i+1, column=0, padx=5)
    button = tk.Button(root, text="추가", command=add_entry_text) # button
    button.grid(row=i+1, column=1, padx=5)
    # combobox
    year_cb = ttk.Combobox(root, values=years, width=6)
    month_cb = ttk.Combobox(root, values=months, width=4)
    day_cb = ttk.Combobox(root, values=days, width=4)

    year_cb.set("2025")
    month_cb.set("01")
    day_cb.set("01")

    year_cb.grid(row=i+1, column=2, padx=5)
    month_cb.grid(row=i+1, column=3, padx=5)
    day_cb.grid(row=i+1, column=4, padx=5) 


def remove_lebel():
    global i

    tk.Label.destroy(label_num)
    tk.Label.destroy(label)
    tk.Button.destroy(button_rm)

    i -= 1

label_list = [ None ]
label_list.append(["label", 1])

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

# 날짜 입력 칸
years = [str(y) for y in range(2025, 2050)]
months = [str(m).zfill(2) for m in range(1, 12+1)]
days = [str(d).zfill(2) for d in range(1, 31+1)]

year_cb = ttk.Combobox(root, values=years, width=6)
month_cb = ttk.Combobox(root, values=months, width=4)
day_cb = ttk.Combobox(root, values=days, width=4)

year_cb.set("2025")
month_cb.set("01")
day_cb.set("01")

year_cb.grid(row=i, column=2, padx=5)
month_cb.grid(row=i, column=3, padx=5)
day_cb.grid(row=i, column=4, padx=5)


root.mainloop()
