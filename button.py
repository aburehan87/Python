from tkinter import *

window=Tk()

window.config(background="black")

count=0
def click():
    global count
    count+=1
    print("You clicked a button")
    print(count)



#bd=adds border to the text
#padx,pady=adds some space between the border and the text
photo=PhotoImage(file='C:\\Users\\abure\\OneDrive\\PROGRAMMING\\Python GUI\\like.png')

button=Button(window,text="Click Me",
              command=click,
              font=("Comic Sans",5),
              activeforeground='black',
              activebackground='black',
              image=photo)
button.place(x=155,y=220)


window.mainloop()
