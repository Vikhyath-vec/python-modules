import tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()
mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x480-8-200')
# widthxheight+x_coord+y_coord
label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='left', fill=tkinter.Y) -----> for y
# canvas.pack(side='top', fill=tkinter.Y, expand=True) -----> for y
# canvas.pack(side='top', fill=tkinter.X) -----> for x
# canvas.pack(side='left', fill=tkinter.X, expand=True) -----> for x
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2)

button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

mainWindow.mainloop()



