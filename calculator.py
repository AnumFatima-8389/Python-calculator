import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.geometry("500x650+750+10")
root.resizable(False, False)
root.configure(bg="#dfe3ee")
#:------------------------------------FUNCTIONS-------------------------------:
operationsList = ["+", "-", "/", "x", "="]
global actualOpList
actualOpList = []
divmultList = []
valuesList = []


def enter(value):
    text.insert(tk.END, value)


def compute():
    enter(" = ")
    value = "0"
    intvalue = 0
    operation = None
    global result
    result = 0
    global valuesList
    valuesList = []
    zeroDivision = False
    
    for c in text.get("1.0", tk.END):
        if c == " ":
            continue
        if c not in operationsList:
            read = True
        else:
            read = False
        if read:
            value = value + c
        else:
            intvalue = int(value)
            valuesList.append(intvalue)
            value = "0"
            if c != "=" and c in operationsList:
                global actualOpList
                actualOpList.append(c)
    for c in text.get("1.0", tk.END):
        if len(valuesList) >= 2:
            for c in actualOpList:
                if c == "x":
                    index = actualOpList.index(c)
                    valuesList[index : index + 2] = [
                        valuesList[index] * valuesList[index + 1]
                    ]
                    del actualOpList[index]
                   
                elif c == "/":
                    index = actualOpList.index(c)
                    if valuesList[index+1] != 0:
                        valuesList[index : index + 2] = [
                            valuesList[index] / valuesList[index + 1]
                        ]
                        del actualOpList[index]  
                    else:
                        zeroDivision=True
                        break
            result = valuesList[0]
            count = 1
            if actualOpList:
                for i in valuesList[1:]:
                    if actualOpList[count - 1] == "+":
                        result = result + i
                    elif actualOpList[count - 1] == "-":
                        result = result - i
                    count = count + 1
    if zeroDivision == False:
        text.insert(tk.END, str(result))
    else:
        text.insert(tk.END,"\nCan not divide by zero")


# clear button
def clear():
    global valuesList, result, actualOpList
    valuesList.clear()
    actualOpList.clear()
    result = 0
    text.delete("1.0", tk.END)


# -------------------------------------------------------------------------------------
# the block to enter values to be algebraically manipulated
f1 = tk.Frame(root, bg="#03396c")
f1.pack(side="top", fill="x", padx=5, pady=5)
text = tk.Text(f1, bg="#b3cde0", font=("Arial", 20), height=5)
text.pack(padx=10, pady=10, fill="x")


# lets make the buttons now
f2 = tk.Frame(root, bg="#03396c")
f2.pack(fill="both", padx=8)
for i in range(4):
    f2.columnconfigure(i, weight=1)
# --------------------------enter-------------------------
benter = tk.Button(
    f2,
    bg="#005b96",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    fg="white",
    text="=",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=compute,
)
# ----------------------------------------------------------

b1 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="1",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("1"),
)
b2 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="2",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("2"),
)
b3 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="3",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("3"),
)
bplus = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="+",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter(" + "),
)

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
bplus.grid(row=0, column=3)

b4 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="4",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("4"),
)
b5 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="5",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("5"),
)
b6 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="6",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("6"),
)
bminus = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="-",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter(" - "),
)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
bminus.grid(row=1, column=3)

bmult = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="x",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter(" x "),
)
b9 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="9",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("9"),
)
b7 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="7",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("7"),
)
b8 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="8",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("8"),
)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
bmult.grid(row=2, column=3)

bclear = tk.Button(
    f2,
    bg="#ffc0cb",
    activebackground="#f08080",
    cursor="hand2",
    activeforeground="white",
    text="C",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=clear,
)
b0 = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="0",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter("0"),
)

bdivide = tk.Button(
    f2,
    bg="#6497b1",
    activebackground="#011f4b",
    cursor="hand2",
    activeforeground="white",
    text="/",
    bd=5,
    relief="ridge",
    font=(("Arial", 20)),
    width=20,
    height=2,
    command=lambda: enter(" / "),
)

bclear.grid(row=3, column=0)
b0.grid(row=3, column=1)
benter.grid(row=3, column=2)
bdivide.grid(row=3, column=3)

root.mainloop()
