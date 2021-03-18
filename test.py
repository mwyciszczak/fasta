#testowanie wyboru plików i listboxa
import tkinter as tk
from tkinter.filedialog import askopenfile

main = tk.Tk()
main.minsize(800, 500)

tab = []
listbox_tab = [1, 2, 3, 4]

def pick_file():
    file = askopenfile(mode="r", filetypes=[("TXT files", "*txt")])
    return file

def test():
    for line in pick_file():
        tab.append(line)
    print(tab)

tk.Button(main, command=test).place(relx=0.1, rely=0.1)
listbox = tk.Listbox(main)
listbox.place(relx=0.5, rely=0.5)
scrollbar = tk.Scrollbar(main)
scrollbar.place(relx=0.7, rely=0.5, relheight=0.2)
for values in listbox_tab:
    listbox.insert(tk.END, values)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
def klik():
    print(listbox.get(tk.ACTIVE))

tk.Button(main, command=klik).place(relx=0.4, rely=0.6)


main.mainloop()