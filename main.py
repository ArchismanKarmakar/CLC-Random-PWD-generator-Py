import math
from tkinter import *
import tkinter
import random
import pyperclip

window = tkinter.Tk()
window.title("Password Generator")
window.geometry('450x480')

# constraints
cond1 = IntVar()
cond2 = IntVar()
cond3 = IntVar()
cond4 = IntVar()
length = IntVar()

# charecter lists
list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']  # LWC
list_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']  # UPC
list_3 = ['!', '@', '#', '$', '%', '^', '&', '*',
          '(', ')', '+', '-', '_', '=', '`', '{', '}', '[', ']', ',', '.', '/', '<', '>', '?', ';', ':', '"', '|']  # SPECIAL
list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def entropy(password):
    char_set = password
    char_set_size = length.get()
    password_size = length.get()
    entropy = math.log2(char_set_size ** password_size)
    print(entropy)
    return entropy

# generator


def password():
    final_list = []
    ln = length.get()
    if (cond3.get()):
        final_list.append(list_1)
    if (cond4.get()):
        final_list.append(list_2)
    if (cond2.get()):
        final_list.append(list_3)
    if (cond1.get()):
        final_list.append(list_4)
    bound = cond1.get() + cond2.get() + cond3.get() + cond4.get()
    if not (bound):
        return ("Nothing selected")
    password = []
    for i in range(ln):
        if (i == 0):
            a = 1
        else:
            a = random.randint(1, bound)
        k = final_list[a - 1]
        b = random.randint(0, len(k) - 1)
        password.append(str(k[b]))
    return (''.join(password))


# gloabal password variable
pswrd = StringVar()
pswrd.set(password())
txt_1 = tkinter.Label(window, textvariable=pswrd, font=("Tahoma", 16))
entrpy = entropy(pswrd)
txt_2 = tkinter.Label(window, textvariable=entrpy, font=("Tahoma", 16))

# function to display generated password


def display_password():
    global txt_1
    txt_1.pack_forget()
    pswrd.set(password())

    global txt_2
    txt_2.pack_forget()
    entrpy = entropy(pswrd)
    txt_1 = tkinter.Label(window, textvariable=pswrd, font=("Tahoma", 18))
    txt_1.pack()
    txt_2 = tkinter.Label(window, textvariable=entrpy,
                          font=("Tahoma", 16))
    txt_2.pack()


# top labels
label_1 = tkinter.Label(
    window, text="\nPassword Generator", font=("Tahoma", 30))
label_2 = tkinter.Label(
    window, text="Select atleast two options\n", font=("Tahoma", 18))
label_1.pack()
label_2.pack()


# creating gui components
chkbutton_1 = tkinter.Checkbutton(
    window, text='Numbers', variable=cond1, onvalue=1, offvalue=0, font=("Tahoma", 14))
chkbutton_2 = tkinter.Checkbutton(
    window, text='Special Charecters', variable=cond2, onvalue=1, offvalue=0, font=("Tahoma", 14))
chkbutton_3 = tkinter.Checkbutton(
    window, text='Small Letters', variable=cond3, onvalue=1, offvalue=0, font=("Tahoma", 14))
chkbutton_4 = tkinter.Checkbutton(
    window, text='Capital Letters', variable=cond4, onvalue=1, offvalue=0, font=("Tahoma", 14))
slider_1 = tkinter.Scale(window, variable=length, orient=HORIZONTAL, label="Set length of password", length=180,
                         from_=8, to=30, font=("Tahoma", 12))
button_1 = tkinter.Button(
    window, text="Generate password", command=display_password, font=("Tahoma", 18))

# run created components
chkbutton_1.pack()
chkbutton_2.pack()
chkbutton_3.pack()
chkbutton_4.pack()
slider_1.pack()
button_1.pack()

window.mainloop()
