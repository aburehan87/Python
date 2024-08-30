from tkinter import *

window = Tk()
window.config(background="#34eb6e")


def submit():
    username = entry.get()  # this will take entry into the username
    print(f"Your password is : {username}")


def clear():
    entry.delete(
        0, END
    )  # this will delete chars from entry, starting from 0th index upto the end


def delete():
    entry.delete(
        len(entry.get()) - 1, END
    )  # this will delete each character starting from last element of entry


entry = Entry(window, font=("Arial", 20), fg="white", bg="black", show="*")
entry.pack(side=LEFT)

submit_button = Button(
    window, text="SUBMIT", font=("Arial", 30), fg="white", bg="black", command=submit
)
submit_button.pack(side=RIGHT)

clear_button = Button(window, text="CLEAR", fg="white", bg="black", command=clear)
clear_button.pack(side=RIGHT)

delete_button = Button(window, text="DELETE", fg="white", bg="black", command=delete)
delete_button.pack(side=RIGHT)


window.mainloop()
