import tkinter as tk
import time

from func import pwGenerate

m = tk.Tk()
#################################################
def getPW(size = 5):
    data = pwGenerate(size)

    new_pw = data[0]
    pw_strength = data[1]
    pw_color = data[2]

    PASSWORD.set(new_pw)

    lbl_strength.configure(foreground = "white", background = pw_color, text = pw_strength, font = ('sans serif', 10, 'bold'), bd = 10, height = 1, width = 10)

    m.clipboard_clear()
    m.clipboard_append(new_pw)
    m.update()

    time.sleep(.02)
    m.update()

"""VARIABLES"""
PASSWORD = tk.StringVar()
PW_SIZE = tk.IntVar()
e1 = tk.Entry(m, text = PW_SIZE)
PW_SIZE.set(5)

"""WINDOW"""
m.title("RANDOM PASSWORD GENERATOR")

width = 600
height = 262

screen_width = m.winfo_screenwidth()
screen_height = m.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

m.geometry("%dx%d+%d+%d" % (width, height, x, y))

"""FRAME"""
Top = tk.Frame(m, width = width)
Top.pack(side = tk.TOP)

Form = tk.Frame(m, width = width)
Form.pack(side = tk.TOP)

Bot = tk.Frame(m, width = width)
Bot.pack(side = tk.BOTTOM)

"""WIDGETS"""
# Labels
lbl_title = tk.Label(Top, width = width, font = ('sans serif', 12, 'bold'), text = "", bd = 1, relief = tk.SOLID)
lbl_title.pack(fill = tk.X)
lbl_password = tk.Label(Form, font = ('sans serif', 14), text = "Password :", bd = 10)
lbl_password.grid(row = 0, pady = 10)
lbl_strength = tk.Label(Form, font = ('sans serif', 10, 'bold'), foreground = "white", background = "#6d0001", text = "Very Weak", bd = 10, height = 1, width = 10)
lbl_strength.grid(row = 0, column = 3, pady = 10, padx = 10)
lbl_pw_size = tk.Label(Form, font = ('sans serif', 14), text = "Select Size :", bd = 10)
lbl_pw_size.grid(row = 1, pady = 9)
lbl_instructions = tk.Label(Bot, width = width, font = ('sans serif', 12, 'bold'), text = "RESULT COPIED TO CLIPBOARD", bd = 1, relief = tk.SOLID)
lbl_instructions.pack(fill = tk.X)

# Entries
password = tk.Entry(Form, textvariable = PASSWORD, font = (18), width = 22)
password.grid(row = 0, column = 1, columnspan = 2)
pw_size = tk.Scale(Form, from_= 5, to = 30, length = 230, width = 23, sliderlength = 14, orient = tk.HORIZONTAL, variable = PW_SIZE, font = (18))
pw_size.grid(row = 1, column = 1, columnspan = 2)

# Button
btn_generate = tk.Button(Form, text = "GENERATE !", width = 20, command = lambda: getPW(PW_SIZE))
btn_generate.grid(row = 2, column = 1, columnspan = 2)
#################################################
m.mainloop()