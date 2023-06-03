import tkinter
import pygame
naat = ["Naat.mp3","Naat1.mp3","Naat2.mp3"]
i = 0
pause = 0
loop = False

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

def playclicked():

    if (play_button.cget('text')=="Play"):
        pygame.mixer.init()
        pygame.mixer.music.load(naat[i])
        pygame.mixer.music.play()
        play_button.config(text="Pause")
    else:
        pygame.mixer.music.pause()
        play_button.config(text = "Play")
    pass

def prevclicked():
    global i
    if i == 0:
        i = 2
        pygame.mixer.music.load(naat[i])
    else:
        i = i-1
        pygame.mixer.music.load(naat[i])
    pygame.mixer.music.play()

def nextclicked():
    global i
    if i == 2:
        i=0
        pygame.mixer.music.load(naat[i])
    else:
        i = i+1
        pygame.mixer.music.load(naat[i])
    pygame.mixer.music.play()

def loopbutton():
    if (loop_on.cget('text')=="loop"):
        loop_on.config(text="no loop")
        pygame.mixer.music.play(loops=-1)
    elif (loop_on.cget('text')=="no loop"):
        pygame.mixer.music.play()
        loop_on.config(text="loop")
    pass

def buttons():
    play_button.pack(side=tkinter.LEFT, anchor=tkinter.SW)
    previous_button.pack(side = tkinter.LEFT, anchor = tkinter.SW)
    loop_on.pack(side=tkinter.LEFT, anchor=tkinter.SW)
    next_button.pack(side=tkinter.LEFT, anchor=tkinter.SW)
    image_label.place(relx=0.5, rely=0.5, anchor="center")



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
window.after(3000,buttons)
play_button = tkinter.Button(window, text="Play", command=playclicked, width=10, height=2)
previous_button = tkinter.Button(window, text = "Prev", command=prevclicked, width=10, height=2)
loop_on=tkinter.Button(window, text="loop", command=loopbutton, width=10,height=2)
next_button = tkinter.Button(window, text = "Next", command=nextclicked, width=10,height=2)

window.mainloop()