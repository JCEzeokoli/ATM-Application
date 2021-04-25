#Mock ATM Project

from datetime import datetime
print(datetime.now())
pin=(1234)
allowedpin=(1234)
print("Welcome, Please insert your atm card")

#User Inserts Atm card
print('kindly input your pin')
pin = int(input('Please Enter You 4 Digit Pin: '))
if (pin == allowedpin) :
                print('Welcome')
                print ("Please choose your Option \n")
                print('Please Press 1 For Withdrawal\n')
                print('Please Press 2 To Make a Deposit\n')
                print('Please Press 3 To make a complaint \n')
                option = int(input('What Would you like to choose?'))
                if option == 1:
                    print ("How much would you like to withdraw?")
                    int(input())
                    print ('Take your cash')
                
                elif option == 2:
                     print ("How much will you like to deposit")
                     oldbalance = 0
                     Deposit = int(input())
                     CurrentBalance = (oldbalance + Deposit)
                     print ('Your current balance is',CurrentBalance)
     
                elif option == 3:
                    print ('What issue will you like to report?')
                    str(input())
                    print ('Thank you for contacting us')
                    
                else:
                    print ('You have selected the wrong option, Please try again')
                    
                    
                                                    
                
else:
        print (" Your pin is incorrect, Please try again ").com




import random

database = {} #dictionary

def init():


    print("Welcome to PythonBank")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):

        login()
    elif(haveAccount == 2):

        register()
    else:
        print("You have selected invalid option")
        init()


def login():

    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)


    print('Invalid account or password')
    login()



def register():

    print("****** Create Account *******")

    email = input("email address: \n")
    first_name = input("First Name: \n")
    last_name = input("Last name: \n")
    password = input("create password\n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Congratulations!!! \n Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Keep it safe!!!")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):

        withdrawalOperation()
    elif(selectedOption == 3):

        logout()
    elif(selectedOption == 4):

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("withdrawal")


def depositOperation():
    print("Deposit")


def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()

#### ACTUAL BANKING SYSTEM #####

init()


 

    
