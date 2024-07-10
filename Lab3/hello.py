"""
Kayla Tran
CS314
Lab3
"""

import tkinter

def display_goodmorning():
    #print("Good morning Kayla")
    lbl_morning = tkinter.Label(window, text="Good morning Kayla")
    lbl_morning.pack()

def display_goodafternoon():
    #print("Good afternoon Kayla")
    lbl_afternoon = tkinter.Label(window, text="Good afternoon Kayla")
    lbl_afternoon.pack()

window = tkinter.Tk()
window.title("Lab 3")
window.geometry("500x600")
btn_morning = tkinter.Button(window, text="Morning", command=display_goodmorning)
btn_afternoon =  tkinter.Button(window, text="Afternoon", command=display_goodafternoon)

btn_morning.pack()
btn_afternoon.pack()

window.mainloop()
