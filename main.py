import tkinter

def center_screen(window, height, width):
    wheight = window.winfo_screenheight()
    wwidth = window.winfo_screenwidth()
    y = int((wheight/2) - (height/2))
    x = int((wwidth/2) - (width/2))
    window.geometry(f"{width}x{height}+{x}+{y}")

def removewelcome():
    var_label.destroy()

    var1 = "NAAT PLAYER"
    var_label1 = tkinter.Label(window, text=var1, font=("Arial", 16))
    var_label1.pack(pady=50)


window = tkinter.Tk()
window.title("Naat Player")   #title name
window_height = 400
window_width = 600
center_screen(window, window_height, window_width)

var = "WELCOME TO THE NAAT PLAYER"
var_label = tkinter.Label(window, text=var, font=("Arial", 16))
var_label.pack(pady=50)

image = tkinter.PhotoImage(file = "bg_image.png")
image_label = tkinter.Label(window, image=image)


window.after(3000, removewelcome)