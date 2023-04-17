import tkinter  
import random  

clrs = ['Blue', 'Pink', 'Orange', 'Green', 'Yellow', 'Black', 'Purple', 'Brown', 'White']  
scrn = 0  
time_left = 25  

def start_game(event):
    global time_left
    if time_left == 25:
        countdown()
    next_color()

def next_color():
    global scrn
    global time_left
    
    if time_left > 0:
        i.focus_set()
        if i.get().lower() == label['fg'].lower():
            scrn += 5
        i.delete(0, tkinter.END)
        random.shuffle(clrs)
        label.config(fg=str(clrs[1]), text=str(clrs[0]))
        scrn_label.config(text="Score: " + str(scrn))

def countdown():
    global time_left
    
    if time_left > 0:
        time_left -= 1
        time_label.config(text="Time left: " + str(time_left))
        time_label.after(1000, countdown)

root = tkinter.Tk()  
root.title("COLOR GAME")  
root.geometry("900x600")  

instruction = tkinter.Label(root, text="\nType the color of the words, and not the word text!\n", font=('TimesNewRoman', 20))  
instruction.pack()  

scrn_label = tkinter.Label(root, text="Press Enter to Play\n", font=('TimesNewRoman', 20))  
scrn_label.pack()  

time_label = tkinter.Label(root, text="Time left: " + str(time_left), font=('TimesNewRoman', 20))  
time_label.pack()  

label = tkinter.Label(root, font=('TimesNewRoman', 80))  
label.pack()  

i = tkinter.Entry(root)  
root.bind('<Return>', start_game)  
i.pack()  
i.focus_set()  

root.mainloop() 
