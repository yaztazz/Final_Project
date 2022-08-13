from tkinter import *


def create_window1():    #open new window
    def submit_total():  #add values after submit button is pressed
        result = float(entry1.get()) + float(entry2.get()) + float(entry3.get())
        print(result)



    new_window = Tk()
    new_window.geometry("600x600")
    new_window.title('Total Points Earned Calculator')
    label = Label(new_window,text="Please enter homework,test, and bonus points:")
    label.pack()
    entry1 = Entry(new_window)
    entry1.pack
    entry1.place(x=25,y=100)
    entry2 = Entry(new_window)
    entry2.pack
    entry2.place(x=25, y=250)
    entry3 = Entry(new_window)
    entry3.pack
    entry3.place(x=25, y=400)
    submit_button = Button(new_window,text="submit",command =submit_total)
    submit_button.place(x=25,y=450)


def create_window2():
    new_window = Tk()
    new_window.geometry("600x600")
    new_window.title('Average Points Earned Calculator')
    label = Label(new_window, text="Please enter homework,test, and bonus points:")
    label.pack()
    entry1 = Entry(new_window)
    entry1.pack
    entry1.place(x=25, y=100)
    entry2 = Entry(new_window)
    entry2.pack
    entry2.place(x=25, y=250)
    entry3 = Entry(new_window)
    entry3.pack
    entry3.place(x=25, y=400)
    submit_button = Button(new_window, text="submit")
    submit_button.place(x=25, y=450)

def create_window3():
    new_window = Tk()
    new_window.geometry("600x600")
    new_window.title('Letter Grade Calculator')
    label = Label(new_window, text="Please enter homework,test, and bonus points:")
    label.pack()
    entry1 = Entry(new_window)
    entry1.pack
    entry1.place(x=25, y=100)
    entry2 = Entry(new_window)
    entry2.pack
    entry2.place(x=25, y=250)
    entry3 = Entry(new_window)
    entry3.pack
    entry3.place(x=25, y=400)
    submit_button = Button(new_window, text="submit")
    submit_button.place(x=25, y=450)


window = Tk() #instantiate window
window.geometry("600x600") #size
window.title("Grade Calculator") #window name

calc_icon = PhotoImage(file='img.png') #convert image to usable data type
window.iconphoto(True,calc_icon) #set photo to corner
window.config(background="#8516CE") #background change to purple
label = Label(window,text="Please Choose a Calculator Option:",font=('Arial',20,'bold'))
label.pack()

button1 = Button(window, text ="1-Total Points Earned",command=create_window1)
button1.pack
button1.place(x=25,y=100)

button2 = Button(window, text= "2-Average Points Earned",command=create_window2)
button2.pack
button2.place(x=25,y=250)

button3 = Button(window, text= "3-Letter Grade",command=create_window3)
button3.pack
button3.place(x=25,y=400)




window.mainloop() #place window


