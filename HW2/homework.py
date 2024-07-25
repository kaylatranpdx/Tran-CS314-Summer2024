"""
Kayla Tran
CS314
Homework 2
July 24, 2024
"""

import tkinter

up_down_ctr = 0
left_right_ctr = 0

def move_up():
    global up_down_ctr
    up_down_ctr += 1
    if up_ctr == 50:
        up_ctr = 0
    lbl_up = tkinter.Label(window, text= "(" + str(up_down_ctr) + "," + str(left_right_ctr) + ")")
    lbl_up.pack()

def move_down():
    global up_down_ctr
    up_down_ctr -= 1
    if down_ctr < 0:
        down_ctr = 0
    lbl_down = tkinter.Label(window, text= "(" + str(up_down_ctr) + "," + str(left_right_ctr) + ")")
    lbl_down.pack()

def move_right():
    global left_right_ctr
    left_right_ctr += 1
    if right_ctr == 50:
        right_ctr = 0
    lbl_right = tkinter.Label(window, text= "(" + str(up_down_ctr) + "," + str(left_right_ctr) + ")")
    lbl_right.pack()

def move_left():
    global left_right_ctr
    left_right_ctr -= 1
    if left_ctr < 0:
        left_ctr = 0
    lbl_left = tkinter.Label(window, text= "(" + str(up_down_ctr) + "," + str(left_right_ctr) + ")")
    lbl_left.pack()

window = tkinter.Tk()
window.title("Homework 2")
window.geometry("500x600")
btn_up = tkinter.Button(window, text="UP", command=move_up)
btn_down =  tkinter.Button(window, text="DOWN", command=move_down)
btn_right = tkinter.Button(window, text="RIGHT", command=move_right)
btn_left =  tkinter.Button(window, text="LEFT", command=move_left)

btn_up.pack()
btn_down.pack() 
btn_right.pack()
btn_left.pack()

window.mainloop()