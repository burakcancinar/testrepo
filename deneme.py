import random
import time
from math import *

def menu():
    print("""
    
    2. Turn Off Pc
    3. Volume Settings
    4. Student Register
    5. Calculator
    6. Number Guessing Game 
    7. Hangman Game
    8. RPG Game
    Çıkmak İçin 'q' basınız.
    """)
def menu2():
    print("\n**** The Computer is 'OFF' Please Turn 'ON' The Computer ****")
def hangman():
    print("""
     ________
    |/   |     
    |   (_)             
    |   /|\           
    |    |        
    |   / \        
    |               
    |___    
                         _                     
                        | |                    
                        | | ___  ___  ___ _ __ 
                        | |/ _ \/ __|/ _ \ '__|
                        | | (_) \__ \  __/ |   
                        |_|\___/|___/\___|_|   

          """)
word = ["burak","cam","sivas"]
class computer():
    def __init__(self,pc_status ="OFF",pc_volume = "0"):
        self.pc_status = pc_status
        self.pc_volume = pc_volume
    def pc_on(self):
        if(self.pc_status == "ON"):
            print("Computer already ON")
        else:
            print("Computer starting...")
            time.sleep(1)
            self.pc_status = "ON"
    def pc_off(self):
        if(self.pc_status == "OFF"):
            print("Computer already OFF")
        else:
            print("Computer Shut Downing...")
            time.sleep(2)
            self.pc_status = "OFF"
    def sound_settings(self):
        if (self.pc_status == "OFF"):
            print("***PC Off You Have To Turn On***")
        else:
            self.pc_volume = 0
            while True:
                user_input = input("---------------\nDecrease Volume: '<'\nIncrease Volume: '>'\nMute Volume: '!'\nExit: exit\n---------------\n:")
                if(user_input == "<"):
                    if(self.pc_volume != 0):
                        self.pc_volume -= 10
                        print("Volume: ",self.pc_volume)
                elif(user_input == ">"):
                    if(self.pc_volume != 31):
                        self.pc_volume += 10
                        print("Volume: ",self.pc_volume)
                elif(user_input == "!"):
                    self.pc_volume = 0
                    print("Volume: ",self.pc_volume)
                else:
                    print("Volume Updated: ",self.pc_volume)
                    break
comp = computer()
class worker:
    def __init__(self, name, surname,student_id,sequence_number,phone_number,e_mail):
        self.name = name
        self.surname = surname
        self.student_id = student_id
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.sequence_number =sequence_number
    @classmethod
    def from_input(cls):
        return cls(
            sequence_number = int(input("Sequence Number: ")),
            name = input('Name: '),
            surname = input("Surname: "),
            student_id = int(input(('Student ID: '))),
            phone_number = int(input("Phone Number: ")),
            e_mail = input("E-Mail: ")
        )
    def __str__(self):  #printing function
        return "-------------\nName: {}\nSurname: {}\nStudent ID: {}\nPhone Number: {}\nE-Mail: {}\n-------------".format(self.name, self.surname, self.student_id,self.phone_number,self.e_mail)
class number_game():
    def __init__(self):
        self.user_play = 0
        self.secret_num = random.randint(0, 10)
        self.user_input = 0
        self.user_mistake = 0
        self.game_mechanics()  # This is new
    def game_mechanics(self):
        while True:
            self.user_input = int(input("Pick a Number Between 1-10\n>>>"))
            if (self.user_input > 10):
                print("I Picked a Number Between 1 to 10, You Entered {} Are You Idiot? ".format(self.user_input))
            elif (self.user_input < 0):
                print("I Picked a Number Between 1 to 10, You Entered {} Are You Idiot? ".format(self.user_input))
            elif (self.user_input > self.secret_num):
                print("Your Value Too High, Keep Try!")
                self.user_mistake += 1
            elif(self.user_input < self.secret_num):
                print("Your Value Too Low, Keep Try!")
                self.user_mistake += 1
            elif(self.user_input == self.secret_num):
                print(("You Won Finally... The Number Was {} After {} mistakes. If You Want Play Again Press 1".format(self.secret_num,self.user_mistake)))
                user_play = int(input(">>>"))
                if(user_play == "1"):
                    self.secret_num = random.randint(0,10)
                    new_game()
                else:
                    menu()
                    break
def new_game():
    number_game()
class hangman_game():
    def __init__(self):
        self.user_word = ""
        self.secret_word = random.choice(word)
        self.turns = len(self.secret_word)
        self.guesses = ""
        self.game_mech()
    def game_mech(self):
        while self.turns > 0:
            self.user_mistake = 0
            for char in self.secret_word:
                if char in self.guesses:
                    print(char, end='')
                else:
                    print(' _ ', end='')
                    self.user_mistake = self.user_mistake + 1
            if self.user_mistake == 0:
                print("\nYou Won.")
                user_restart = input("Play Again? YES Or NO: ")
                if user_restart == "YES":
                    new_gameh()
                else:
                    menu()
                break
            self.user_word = input("\nGuess a char: ")
            self.guesses =  self.guesses+self.user_word
            if self.user_word not in self.secret_word:
                self.turns = self.turns - 1
                print("Wrong")
            print("You have", + self.turns, "more guesses")
            if self.turns == 0:
                print("Secret word was {}".format(self.secret_word))
                hangman()
                user_restart = input("Play Again? YES Or NO: ")
                if user_restart == "YES":
                    new_gameh()
                else:
                    menu()
                    break
def new_gameh():
    hangman_game()
def login():
    attemp = 3
    while attemp > 0:
        print("Username: Admin Password: ")
        login = input(">>>")
        print("Checking...")
        time.sleep(1)
        if login == "123":
            print("Access Granted...")
            menu()
            break
        else:
            print("Error, Password not match..")
            attemp = attemp - 1
users = {}
menu2()
while True:
    process = input(">>>> ")
    if (process == "q"):
        print("Shutdowning...")
        break
    elif (process == "ON"):
        comp.pc_on()
        login()
    elif (process == "2"):
        comp.pc_off()
        break
    elif (process == "3"):
        comp.sound_settings()
        menu()
    elif (process == "4"):
        if (comp.pc_status == "OFF"):
            print("Please Turn ON Computer.")
            menu()
        else:
            n = int(input("How many student?: "))
            for _ in range(n):  # create n users
                print("{}. student".format(_ + 1))
                user = worker.from_input()  # from user input
                users[user.sequence_number] = user  # in the dictionary
            for i in users:
                print(users[i])
    elif (process == "5"):
        if (comp.pc_status == "OFF"):
            print("Please Turn ON Computer.")
            menu()
        else:
            print("------------\nCalculator")
            num1 = float(input("Number: "))
            while True:
                operator = input("Operator(+,-,/,*):  ")
                if operator == "+":
                    num2 = float(input("Number: "))
                    num1 = num1 + num2
                elif operator == "-":
                    num2 = float(input("Number: "))
                    num1 = num1 - num2
                elif operator == "*":
                    num2 = float(input("Number: "))
                    num1 = num1 * num2
                elif operator == "/":
                    num2 = float(input("Number: "))
                    num1 = num1 / num2
                elif operator == "=":
                    print("\n\n\tResult: {}\n------------------".format(round(num1, 5)))
                    menu()
                    break
    elif(process == "6"):
        if (comp.pc_status == "OFF"):
            print("Please Turn ON Computer.")
            menu()
        else:
            number_game()
    elif(process == "7"):
        if(comp.pc_status == "OFF"):
            print("Please Turn ON Computer.")
            menu()
        else:
            hangman_game()