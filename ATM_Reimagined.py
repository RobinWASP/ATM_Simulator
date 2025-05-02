# WELCOME TO THE ATM REIMAGINED! (MY VERY FIRST PYTHON PROJECT!) This Project was Originaly prototyped at October 2024 and Reimagined at May 2 2025
import random
user_balance = random.randint(1, 500000)

card = input("Do you have a card (Y / N)?: ").lower().strip()

if(card == "y"):
    user_code = int(input("Please Enter Your Passcode: "))
    name = input("Please Enter your Name: ")
    if(len(str(user_code)) <= 6): #i MIGHT HAVE TO IMPLEMENT A FOR LOOP FOR THIS IF STATEMENT, TOMORROW MAYBE
        print("Code Accepted!")
    
        print("Hello and Welcome to your Account!", name)

        choice_list = ("1. Check Balance" , "2. Withdraw Cash" , "3. Change Password", "4. Release Card", "5. Print Invoice")

        print(choice_list)
    
        user_choice = int(input("What would you like to do?: "))
    
        choices_dict = {
            1: "Check Balance",
            2: "Withdraw Cash",
            3: "Change Password",
            4: "Release Card",
            5: "Print Invoice"
        }
        while True:
            if(user_choice == 1):

                print("YOU ARE NOW CHECKING YOUR BALANCE")
                print("Your Current Balance is: ", round(user_balance,1), "Philippine Pesos")
                print(choice_list)
            
                user_choice = int(input("What would like to do next?: "))

            elif(user_choice == 2):

                print("YOU ARE NOW WITHDRAWING YOUR CASH", "\n Your Current Balance is: ", user_balance, "Philippine Peso")

                withdraw_ammount = int(input("How Much would you like to Withdraw?"))

                current_cash = user_balance - withdraw_ammount 

                print("Your Current balance is NOW AT:", current_cash)
                user_choice = int(input("What would like to do next?: "))

            elif(user_choice == 3):

                print("YOU ARE NOW ABOUT TO CHANGE YOUR PASSWORD")

                old_pass = int(input("Please Enter your OLD PASSCODE"))
                new_pass = int(input("Please Enter your NEW PASSCODE"))

                print("Your Passcode has been Successfully Changed!")

                user_choice = int(input("What would like to do next?: "))

            elif(user_choice == 4):

                print("CARD IS NOW RELEASING, DON'T FORGET TO TAKE YOUR CARD!")  
                break  

            elif(user_choice == 5):

                print("You currently have", round(user_balance ,5))
                break

            else:
                print("User Choice is invalid")
    else:
       print("PassCode TOO LONG!")      
               
else:
    print("You MUST POSSESS A CARD to access this ATM")


# FUTURE IMPLEMENTATIONS:
# Make sure to only make the user enter ONLY NUMBERS ON PASSCODES
# USE FOR LOOPS FOR INVALID INPUTS FOR PASSCODE SUCH A`S LETTERS OR OVER 7 DIGITS
# IMPLEMENT A FEATURE THAT THE USERS INFO MUST TIE TO THEIR NAME (ADVANCED)