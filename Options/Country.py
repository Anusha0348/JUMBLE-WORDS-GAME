#import libraries
from tkinter import *
from random import *
from tkinter import messagebox
import time

#shuffle the list words of Countries
COLOUR_WORD = ['TKISAPNA', 'INAHC', 'AJAPN', 'NYEGRMA', 'CDAAAN', 'YKRTUE', 'DIANI', 'MGEILBU', 'FERCAN', 'IYATL', 'TAIWKU', 
                'YWRONA', 'MNYEE', 'HTLNIDAAI', ]

#create a list of Countries
COLOUR_ANSWER = ['PAKISTAN', 'CHINA', 'JAPAN', 'GERMANY', 'CANADA', 'TURKEY', 'INDIA', 'BELGIUM', 'FRANCE', 'ITALY', 'KUWAIT',
                 'NORWAY', 'YEMEN', 'THAILAND', ]


ran_num = randrange(0, (len(COLOUR_WORD)))
jumbled_rand_word = COLOUR_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        import main_start
        main_start.start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(COLOUR_WORD)))
        word.configure(text=COLOUR_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")
    
    #Define a Check fuction
    def check():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == COLOUR_ANSWER[ran_num]:
            points += 1
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(COLOUR_WORD)))
            word.configure(text=COLOUR_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    #define a show_answer
    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=COLOUR_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x500+500+100")
    my_window.resizable(0, 0)
    my_window.title("Jumbled Words Quiz-Countries")
    my_window.configure(background="turquoise2")
    img1 = PhotoImage(file="C:/Users/fali0/OneDrive/Desktop/JUMBLE WORDS GAME/logo/back.png")

    #create label
    lab_img1 = Button(
        my_window,
        image=img1,
        bg='turquoise2',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="turquoise2",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="turquoise2",
        fg="#000000",
        font="Titillium  30 bold"
    )
    word.pack()

    #create an Entry Box for answer
    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    #Pack the Entry Box
    get_input.pack()

    #create a submit button to submit answer
    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="MediumPurple3",
        command=check,
    )
    #Pack the Submit Button
    submit.pack(pady=(10, 20))

    #create a Change Word Button to change the word
    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="MediumPurple3",
        font=("", 13),
        command=change,
    )
    #Pack the Change Word Button
    change.pack()

    #create a "Show Answer" button to see the answer
    ans = Button(
        text="Show Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="MediumPurple3",
        font=("", 13),
        command=show_answer,
    )
     #Pack the answer Button
    ans.pack(pady=(20, 10))

    #create a label
    ans_lab = Label(
        text="",
        bg="turquoise2",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()