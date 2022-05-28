
from tkinter import *
import random
from tkinter import messagebox

# initialize tkinter
root = Tk()
# set window title
root.title("What is the number")
# set windows size
root.geometry("300x300")



def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        exit()
        
def start_game():
    global round_count
    round_count = Label(root, text='')
    round_count.pack(pady=5)

    global label
    label = Label(root, text='Guess the number between 1-10')
    label.pack(pady=20)

    global box
    box = Entry(root)
    box.pack(pady=10)

    global button
    global var
    var = IntVar()
    button = Button(root,text='Summit Answer',command=lambda: var.set(1))
    button.pack(pady=10)

    global alert
    alert = Label(root, text='')
    alert.pack(pady=5)

    global alert_repeat
    alert_repeat = Label(root, text='')
    alert_repeat.pack(pady=5)

    global exit_button
    exit_button = Button(root, text="Quit", command=on_closing)
    exit_button.pack(pady=5)

def replay_game(score):
    label.destroy()
    round_count.destroy()
    box.destroy()
    button.destroy()
    alert.destroy()
    alert_repeat.destroy()
    exit_button.destroy()

    global text_score
    text_score = Label(root, text=f'\n Your score is {score}/{game_round}')
    text_score.pack(pady=5)

    global button_replay
    button_replay = Button(root,text='Play Again',command=lambda: game(check_start+1))
    button_replay.pack(pady=10)
    
    global exit_button_two
    exit_button_two = Button(root, text="Quit", command=on_closing)
    exit_button_two.pack(pady=5)
    
check_start = 0
game_round = 10

def game(check_start):
    
    if check_start > 0 :
         button_replay.destroy()
         exit_button_two.destroy()
         text_score.destroy()
    
    start_game()
    score = 0
    for i in range(1,game_round):
        round_count.config(text= f'\n Round {i}')
        correct_number = random.randint(1,10)
        
        for repeat in range(1,4):
            
            number_input = ''
            while type(number_input) == str:
                try:
                    button.wait_variable(var)
                    number_input = int(box.get())

                except:
                    alert_repeat.config(text='Please input only Number between 1-10')
                    box.delete(0,END)

            if correct_number != number_input:
                alert.config(text='Wrong!!')
                if repeat != 3:
                    alert_repeat.config(text= f'You can try again in {3-repeat} times')
            else:
                alert.config(text='Correct!!')
                score += 1
                box.delete(0,END)
                break
            box.delete(0,END)
            
        alert_repeat.config(text='')
    
    replay_game(score)
    print(f'\n Your score is {score}')
    



# loop
game(check_start)
root.mainloop()