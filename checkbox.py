from tkinter import *

window=Tk()

x=IntVar()

def display():
    if x.get()==1:
        print("Rehan agree's :)")
    else:
        print("Rehan disagreed :(")


check_box=Checkbutton(window,
                      text="I agree to something",
                      font=("Arial",20),
                      fg='green',
                      bg='black',
                      variable=x,#we created a IntVar here
                      onvalue=1,
                      padx=25,
                      pady=25,#initial value will be 1
                      offvalue=0,
                      command=display,#this will display the contents from the display function
                      compound=LEFT)


check_box.pack()























window.mainloop()
