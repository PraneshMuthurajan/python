from tkinter import*
window = Tk()
window.title("Pranesh's calculator ® (All Rights Reserved)")
input1 = Entry(window,borderwidth = 20,bg = "black",fg = "white",font = ("Comic Sans MS",10))
input1.grid(row=0,column=0,columnspan = 3,padx=10,pady = 10)

def button_click(number):
    current = input1.get()
    input1.delete(0,END)
    input1.insert(0, str (current) + str(number))
    return
def button_clear():
    input1.delete(0,END)

def button_equal():
    secondnumber = input1.get()
    input1.delete(0,END)
    if math == "addition":
        input1.insert(0,f_num + int(secondnumber))
    if math == "subtraction":
        input1.insert(0,f_num - int(secondnumber))
    if math == "multiplication":
        input1.insert(0,f_num * int(secondnumber))
    if math == "division":
        input1.insert(0,f_num / int(secondnumber))

def button_add():
    firstnumber = input1.get()
    global f_num
    global math
    math = "addition"
    f_num = int(firstnumber)
    input1.delete(0,END)
    
def button_sub():
    firstnumber = input1.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(firstnumber)
    input1.delete(0,END)

def button_mul():
    firstnumber = input1.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(firstnumber)
    input1.delete(0,END)

def button_div():
    firstnumber = input1.get()
    global f_num
    global math
    math = "division"
    f_num = int(firstnumber)
    input1.delete(0,END)

button1= Button(window, text="1", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(1))
button2= Button(window, text="2", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(2))
button3= Button(window, text="3", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(3))
button4= Button(window, text="4", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(4))
button5= Button(window, text="5", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(5))
button6= Button(window, text="6", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(6))
button7= Button(window, text="7", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(7))
button8= Button(window, text="8", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(8))
button9= Button(window, text="9", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(9))
button0= Button(window, text="0", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command=lambda:button_click(0))
button_add = Button(window, text="+", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command = button_add)
button_sub=Button(window, text="-", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command = button_sub)
button_mul=Button(window, text="*", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command = button_mul)
button_div=Button(window, text="/", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command = button_div)
button_equal=Button(window, text="=", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command = button_equal)
button_clear=Button(window, text="AC", padx=20, bg="black", fg="white", font=("Comic Sans MS",20),command = button_clear)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
button_add.grid(row=3,column=3)
button_sub.grid(row=2,column=3)
button_mul.grid(row=1,column=3)
button_div.grid(row=4,column=3)
button_equal.grid(row=4,column=2)
button_clear.grid(row=4,column=1)
window.mainloop()


