from keyboard import press
from time import sleep
import pyautogui, os
from tkinter import *


with open("Texto ;).txt") as f:
    info = f.read()


def end(): #Exit function with a message
    print('\nGracias por usar mi botsito hasta otraa')
    exit(0)


def main(): 
    os.system('cls')
    print('''
░█████╗░███╗░░██╗░█████╗░░░░░░░██╗░░░░░██╗███████╗░█████╗░██████╗░░█████╗░██████╗░
██╔══██╗████╗░██║██╔══██╗░░░░░░██║░░░░░██║╚════██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██╔██╗██║███████║█████╗██║░░░░░██║░░███╔═╝███████║██║░░██║██║░░██║██████╔╝
██╔══██║██║╚████║██╔══██║╚════╝██║░░░░░██║██╔══╝░░██╔══██║██║░░██║██║░░██║██╔══██╗
██║░░██║██║░╚███║██║░░██║░░░░░░███████╗██║███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░░░░╚══════╝╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝   \n By Jeff Sniper
Instruciones: Escribe el numero de veces que quieres spamear el texto en el cuadro, luego dale al boton de Ana-Lizador y pulsa el boton de new en omegle.

Server de discrod por si tienes dudas: https://discord.gg/cN76aw28Ur VERIFICATE 

''') 

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping the script')
        end()

def main():
    global amount
    sleep(4)
    pyautogui.press("esc")
    for _ in range(int(amount.get())):
        sleep(0.3)
        # type info
        pyautogui.typewrite(info)
        sleep(0.3)
        # enter
        pyautogui.press("enter")
        sleep(0.3)
        # esc x 3
        x = pyautogui.screenshot().getpixel(pyautogui.position())
        if x[2] > 200 and x[0] < 200:
            x = pyautogui.position()
            pyautogui.click(x)
        else:
            for _ in range(3):
                pyautogui.press("esc")
    for _ in range(2):
        pyautogui.press("esc")

def Help():
    window = Tk()
    window.config(background="#2c3e50")
    #window.iconbitmap('icono')
    window.minsize(800, 130)
    window.maxsize(800, 130)
    window.title("Ayuda")
    Label(window, text="Ana-Lizador:\n AYUDA PARA RETRASADOS", bg="#2c3e50", fg="white").pack()
    Label(window, text="Si no consigues que te vaya el bot escribeme al discord y te ayudare encantado alomejor hasta te pongo un rol fachero XD", bg="#2c3e50", fg="white").pack()        


JeffSniper = Tk()
JeffSniper.title("Ana-Lizador")
JeffSniper.iconbitmap('logo-bot.ico')
JeffSniper.config(background="#2c3e50")
JeffSniper.minsize(310, 60)
JeffSniper.maxsize(420, 180)


#Top Menu bar
menu = Menu(JeffSniper)
JeffSniper.config(menu=menu)


def stop():
    exit(0)

#Submenu
submenu = Menu(JeffSniper)
menu.add_cascade(label="Salida de emergencia", menu=submenu)
submenu.add_command(label="EXIT", command=stop)
menu.add_command(label="Ayuda", command=Help)



#menu
amount = StringVar()
Entry(JeffSniper, text=amount, bd=1, width=7, fg="black").pack()

button = Button
button(JeffSniper, text="Ana-lizador", command=main, bg="#34495e", fg="white").pack()

JeffSniper.mainloop()







