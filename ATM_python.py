'''
features:
* Pin Auth
* Your balance
* Withdraw
* Deposit Funds
* Return Card
'''

print("Welcome to your Bank ATM!")
restart = 'Y'
chances = 3
balance = 1010.10
while chances >= 0:
    pin = int(input("Please enter your 4 digits PIN: "))
    if pin == 1234:
        print("You entered your PIN correctly!\n")
        while restart not in ('n', 'NO', 'no', 'N'):
            print("Please press 1 for your Balance\n")
            print("Please press 2 To Make a Withdraw\n")
            print("Please press 3 To Pay in\n")
            print("Please press 4 To Return Card\n")
            option = int(input("What would you like to choose?: "))
            if option == 1:
                print('Your balance is Rs', balance, '\n')
                restart = input("Would you like to go back? (Y/N): ")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank You!")
                    break

            elif option == 2:
                option2 = 'y'
                withdrawl = float(
                    input('How much Would you like to withdraw?\n$10/$20/$40/$60/$80/$100 for other enter 1: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print("Your balance is now: ", balance)
                    restart = input("Would you like to go back?(Y/N): ")
                    if restart in ('n', 'NO', 'no', 'N'):
                        print("Thank you!")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print("Invalid amount! Please Re-Try\n")
                    restart = 'y'
                elif withdrawl == 1:
                    withdrawl = float(input("Please enter Desired amount: "))

            elif option == 3:
                Pay_in = float(input("How much would you like to pay in?: "))
                balance = balance + Pay_in
                print('\nYour Balance is now $', balance)
                restart = input("Would you like to go back? (Y/N): ")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank you!")
                    break

            elif option == 4:
                print("Please wait while your card is Returned... \n")
                print("Thank you for your service!")
                break

            else:
                print("Please enter a correct number!\n")
                restart = 'y'

    elif pin != 1234:
        print("Incorrect password!")
        chances = chances - 1
        if chances == 0:
            print("\nNo more tries")
            break
