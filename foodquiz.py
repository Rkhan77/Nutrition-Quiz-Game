import json
import random
import tkinter
from tkinter import messagebox


class ProgramGUI:

    def __init__(self):

        # Open the file data.txt in read mode
        try:
            file= open('data.txt', 'r')
            self.data = json.load(file)
            file.close()

        except FileNotFoundError:
            print('Missing/Invalid File!')

        self.components = ('calories', 'fat', 'cholestrol', 'sodium', 'carbohydrates', 'protein')

        # Creating GUI interfaces (main window)

        self.main = tkinter.Tk()

        self.main.configure(background='white')
        self.main.title('Food Quiz')
        self.main.resizable(310, 180)

        self.food1 = tkinter.StringVar()
        self.food2 = tkinter.StringVar()
        self.key = tkinter.StringVar()

        # welcome message
        self.welcomeMessage = tkinter.Label(self.main, text='Welcome to Nutrition Quiz Game', font=('Times', '10', 'bold'))
        self.welcomeMessage.configure(fg='black', bg='white')
        self.welcomeMessage.pack()

        # Creating frames
        self.frameFood = tkinter.Frame(self.main, bg='white')
        self.frameKey = tkinter.Frame(self.main, bg='white')
        self.frameQue = tkinter.Frame(self.main, bg='white')
        self.frameBtn = tkinter.Frame(self.main, bg='white')

        self.frameFood.pack()
        self.frameQue.pack()
        self.frameKey.pack()
        self.frameBtn.pack()

        # creating Label
        self.label_food1 = tkinter.Label(self.frameFood, textvariable=(self.food1), fg='blue', bg='white',
                                         font=('Times', '15', 'bold'))
        self.label_vs = tkinter.Label(self.frameFood, text=('Vs.'), fg='blue', bg='white',
                                      font=('Helvetica', '10', 'bold'))
        self.label_food2 = tkinter.Label(self.frameFood, textvariable=(self.food2), fg='blue', bg='white',
                                         font=('Times', '15', 'bold'))
        self.label_que = tkinter.Label(self.frameQue, text=('Which one has more...\n'), fg='black', bg='white',
                                       font=('Times', '16', 'bold'))
        self.label_key = tkinter.Label(self.frameKey, textvariable=(self.key), fg='black', bg='white',
                                       font=('Times', '15', 'bold'))

        self.label_food1.pack(side='left', padx=25)
        self.label_vs.pack(side='left')
        self.label_food2.pack(side='left', padx=25)
        self.label_que.pack()
        self.label_key.pack()

        # creating buttons
        self.button_food1 = tkinter.Button(self.frameBtn, width=12, textvariable=self.food1,
                                           command=lambda: self.checkAnswer('left'))
        self.button_roughlyEqual = tkinter.Button(self.frameBtn, width=12, text='Roughly Equal',
                                                  command=lambda: self.checkAnswer('middle'))
        self.button_food2 = tkinter.Button(self.frameBtn, width=12, textvariable=self.food2,
                                           command=lambda: self.checkAnswer('right'))

        self.button_food1.pack(padx=10, pady=10, side='left')
        self.button_roughlyEqual.pack(padx=10, pady=10, side='left')
        self.button_food2.pack(padx=10, pady=10, side='left')

        self.showQuestion()
        tkinter.mainloop()

    # This method is responsible for for randomly selecting two food
    # items and a nutritional component and showing them in the GUI.
    def showQuestion(self):

        if self.data != 0:
            foodListLength = len(self.data)
            randomNum1 = random.choice(range(foodListLength))
            randomNum2 = random.choice(range(foodListLength))
            self.foodList1 = self.data[randomNum1]
            self.foodList2 = self.data[randomNum2]

            key = random.choice(self.components)
            self.value1 = (self.data[randomNum1][str(key)])
            self.value2 = (self.data[randomNum2][str(key)])

            self.food1.set(self.data[randomNum1]['name'])
            self.food2.set(self.data[randomNum2]['name'])
            self.key.set(key.upper())

    # This method is responsible for determining whether the user
    # clicked the correct button and showing a Correct/Incorrect messagebox.

    def checkAnswer(self, clickedButton):
        nutrition1 = int(self.value1)
        nutrition2 = int(self.value2)
        if (clickedButton == 'left'):
            if (nutrition1 > nutrition2):
                messagebox.showinfo('Correct!', 'You got it right!')

            else:
                messagebox.showerror('Incorrect!', 'You got it wrong!')

        elif (clickedButton == 'middle'):
            difference = abs(nutrition1 - nutrition2)
            div = (nutrition1 / 10)

            if (difference < div):
                messagebox.showinfo('Correct!', 'You got it right!')

            else:
                messagebox.showerror('Incorrect!', 'You got it wrong!')


        elif clickedButton == 'right':
            if (nutrition1 < nutrition2):
                messagebox.showinfo('Correct!', 'You got it right!')

            else:
                messagebox.showerror('Incorrect!', 'You got it wrong!')

        self.showQuestion()

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
