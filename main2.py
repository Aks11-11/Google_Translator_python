from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest

    trans = Translator()
    trans1 = trans.translate(text=text1, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_text.delete(1.0, END)
    dest_text.insert(END, textget)

root = Tk()
root.title("Ak's Translator")
root.geometry("500x900")
root.config(bg="Sky Blue")

lab_text = Label(root, text="Translator11", font=("Times New Roman", 40, "bold"))
lab_text.place(x=100, y=40, width=300, height=50)

frame = Frame(root)
frame.pack(side=BOTTOM)

lab_txt = Label(frame, text="Source text below", font=("Times new Roman", 20, "bold"))
lab_txt.place(x=100, y=110, width=300, height=20)

Sor_txt = Text(frame, font=("Times new Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=140, height=200, width=480)

list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame)
comb_sor.place(x=10, y=360, height=40, width=150)
comb_sor.set("English")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=360, height=40, width=120)

comb_dest = ttk.Combobox(frame)
comb_dest.place(x=300, y=360, height=40, width=180)
comb_dest.set("English")

dest_lab = Label(frame, text="Destination text below", font=("Times new Roman", 20, "bold"))
dest_lab.place(x=100, y=420, width=300, height=20)

dest_text = Text(frame, font=("Times new Roman", 20, "bold"), wrap=WORD)
dest_text.place(x=10, y=450, height=200, width=480)

root.mainloop()
