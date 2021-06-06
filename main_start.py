#import library
from tkinter import *

#create main page
def start_main_page():
    def start_game(args):  #start game
        main_window.destroy()
        if args == 1:
            from Options import Animals
            Animals.main()
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()


    #create option buttons
    def option():

        #Go Back Button
        lab_img1 = Button(
            main_window,
            image=img1,
            bg='white',
            border=0,
            justify='center',

        )
        sel_btn1 = Button(
            text="Animals",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="purple3",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="Body parts",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="purple3",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="Colour",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="purple3",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="Fruits",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="purple3",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="Shapes",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="purple3",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="Vegetable",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="purple3",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )
    
    #show options
    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Jumbled Words Quiz")
    main_window.configure(background="#e6fff5")
    
    #Define images
    img0 = PhotoImage(file="C:/Users/fali0/OneDrive/Desktop/JUMBLE WORDS GAME/logo/logo2.png")
    img1 = PhotoImage(file="C:/Users/fali0/OneDrive/Desktop/JUMBLE WORDS GAME/logo/back.png")
    
    #create a label
    lab_img = Label(
        main_window,
        image=img0,
        bg='#e6fff5',
    )
    lab_img.pack(pady=(50, 0))
   

    #create start button
    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="red2",
        font=("", 15),
        cursor="hand2",
        command=show_option,
    )

    #pack the start button
    start_btn.pack(pady=(50, 30))

    main_window.mainloop()


start_main_page()
