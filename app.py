from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as custom
import cv2
from PIL import Image, ImageTk, ImageSequence
from tkinter import filedialog


custom.set_appearance_mode("light")
app = custom.CTk()
app.resizable(False, False)
app.title("Zero")
app.iconbitmap("eagle.ico")
width = 750
height = 450
xpos = (app.winfo_screenwidth() - width) // 2
ypos = (app.winfo_screenheight() - height) // 2
app.geometry(f"{width}x{height}+{xpos}+{ypos}")

def ok(value=0):
    if value <= 100:
        progres["value"] = value
        app.after(10, ok, value + 1)
        if value == 100:
            play()

def play():
    global cap, vlab
    src = lab.get()
    cap = cv2.VideoCapture(src)
    vlab.place(x=100,y=60)
    update()
    if src == "":
        messagebox.showerror("Error", "Empty Path")
    else:
        lab.configure(state= DISABLED)
        but.configure(state= DISABLED)



def update():
    global cap
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (530, 330))
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(img)
        vlab.imgtk = imgtk
        vlab.configure(image=imgtk)
        app.after(10, update)
    else:
        cap.release()

def end():
    global cap
    cap.release()
    vlab.configure(image="")
    vlab.pack_forget()
    app.after_cancel(update)


    but.configure(state= NORMAL)
    lab.configure(state= NORMAL)
    



lab = custom.CTkEntry(app, width=210)
lab.place(x=7,y=10)

progres = ttk.Progressbar(app, length=300, orient="horizontal", mode="determinate")
progres.place(x=210,y=410)

but = custom.CTkButton(app, text="Play", command=ok, width=100,fg_color="#3cb371")
but.place(x=220,y=10)

but2 = custom.CTkButton(app, text="End", width=100, command=end, fg_color="#3cb371")
but2.place(x=330,y=10)

vlab = Label(app)
vlab.pack_forget()

app.mainloop()
