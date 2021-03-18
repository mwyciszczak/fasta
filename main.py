#działa, ale używa global, do poprawy
from Bio import SeqIO
import tkinter as tk
from tkinter.filedialog import askopenfile

main = tk.Tk()
main.minsize(800, 500)

pairs_dict = {}
global listbox
background_image = tk.PhotoImage(file="background_image.png")
background = tk.Label(main, image=background_image)
background.place(x=0, y=0, relheight=1, relwidth=1)


def pick_file_func():
    return askopenfile(mode="r", filetypes=[("FASTA files", "*fasta")])


def create_dict_func():
    fasta_sequences = SeqIO.parse(pick_file_func(), 'fasta')
    for fasta in fasta_sequences:
        sequence, description = str(fasta.seq), fasta.description
        description = description[description.find("("):]
        pairs_dict.update({description: sequence})


def on_click_func():
    create_dict_func()
    create_listbox_func()


def create_listbox_func():
    global listbox
    listbox = tk.Listbox(main)#możliwa przyczyna globala, praca na tej instancji listboxa
    scrollbar = tk.Scrollbar(main)
    listbox.place(relx=0.03, rely=0.2, relheight=0.7, relwidth=0.5)
    scrollbar.place(relx=0.53, rely=0.2, relheight=0.7)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    for x in pairs_dict:
        listbox.insert(tk.END, x)


def get_value_func():
    key = listbox.get(tk.ACTIVE)
    val = pairs_dict[key]
    return val


def nucleotides_func(value):
    nucleotides = {}
    output_string = ""
    a = value
    for x in sorted(a):
        nucleotides.update({x: a.count(x)})
    for y in nucleotides:
        output_string += "{},{}; ".format(y, nucleotides[y])
    text_output = tk.Text(main)
    text_output.place(relx=0.58, rely=0.2, relheight=0.7, relwidth=0.4)
    text_output.insert(tk.END, output_string)


def paired_nucleotides_func(value):
    a = value
    output_string = ""
    list_ = []
    for x in range(len(a) - 1):
        list_.append(a[x:x + 2])
    last = ''
    pairs = {}
    for x in sorted(list_):
        if last == x:
            continue
        else:
            counter = 0
            for y in sorted(list_):
                if x == y:
                    counter += 1
            pairs.update({x: counter})
            last = x
    for y in pairs:
        output_string += "{},{}; ".format(y, pairs[y])
    text_output = tk.Text(main)
    text_output.place(relx=0.58, rely=0.2, relheight=0.7, relwidth=0.4)
    text_output.insert(tk.END, output_string)


getfasta_button = tk.Button(main, text="Pobierz plik FASTA", command=on_click_func)
getfasta_button.place(relx=0.03, rely=0.03, relheight=0.1, relwidth=0.5)
nucleotides_button = tk.Button(main, text="Nukleotydy", command=lambda: nucleotides_func(get_value_func()))
nucleotides_button.place(relx=0.61, rely=0.03, relheight=0.1, relwidth=0.15)
nucleotides_button = tk.Button(main, text="Pary nukleotydów", command=lambda: paired_nucleotides_func(get_value_func()))
nucleotides_button.place(relx=0.8, rely=0.03, relheight=0.1, relwidth=0.15)

main.mainloop()
