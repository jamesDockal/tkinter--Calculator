from tkinter import *

root = Tk()
root.geometry("500x500")
root.option_add("*font", "Raleway")

Grid.rowconfigure(root, 0, weight = 1)
Grid.rowconfigure(root, 1, weight = 1)
Grid.rowconfigure(root, 2, weight = 1)
Grid.rowconfigure(root, 3, weight = 1)
Grid.rowconfigure(root, 4, weight = 1)
Grid.rowconfigure(root, 5, weight = 1)

Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)

def pressedButton(number):
  current = myinput.get()
  myinput.delete(0, END)
  myinput.insert(0, str(current) + str(number))

def clear():
  myinput.delete(0, END)

def equal():
  equation = myinput.get()
  print(eval(equation))
  myinput.delete(0, END)
  myinput.insert(0, eval(equation))

def addsignal(signal):
  current = myinput.get()
  position = len(str(current))
  myinput.insert(position, f' {signal} ')


  
myinput = Entry(root)
myinput.grid(column = 0, row = 0, columnspan = 3, sticky ='nswe')

clearbutton = Button(root, command = clear, text = 'clear').grid(column = 1, row = 4, sticky = 'nswe')
equalbutton = Button(root, command = equal, text = '=').grid(row = 4, column = 2, rowspan = 2,sticky = 'nswe')
plusbutton = Button(root, command = lambda: addsignal('+'), text = '+').grid(column = 0, row = 5, sticky = 'nswe')
minusbutton = Button(root, command = lambda: addsignal('-'), text = '-').grid(column = 1, row = 5, sticky = 'nswe')

button1 = Button(root,text = 1,command=lambda: pressedButton(1)).grid(column = 0, row = 1,  sticky = 'nswe')
button2 = Button(root,text = 2,command=lambda: pressedButton(2)).grid(column = 1, row = 1,  sticky = 'nswe')
button3 = Button(root,text = 3,command=lambda: pressedButton(3)).grid(column = 2, row = 1,  sticky = 'nswe')
button4 = Button(root,text = 4,command=lambda: pressedButton(4)).grid(column = 0, row = 2,  sticky = 'nswe')
button5 = Button(root,text = 5,command=lambda: pressedButton(5)).grid(column = 1, row = 2,  sticky = 'nswe')
button6 = Button(root,text = 6,command=lambda: pressedButton(6)).grid(column = 2, row = 2,  sticky = 'nswe')
button7 = Button(root,text = 7,command=lambda: pressedButton(7)).grid(column = 0, row = 3,  sticky = 'nswe')
button8 = Button(root,text = 8,command=lambda: pressedButton(8)).grid(column = 1, row = 3,  sticky = 'nswe')
button9 = Button(root,text = 9,command=lambda: pressedButton(9)).grid(column = 2, row = 3,  sticky = 'nswe')
button0 = Button(root,text = 0,command=lambda: pressedButton(0)).grid(column = 0, row = 4,  sticky = 'nswe')


root.mainloop()



