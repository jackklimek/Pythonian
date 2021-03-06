class atm():     #creates a class called atm

    print ("Welcome to Jack's ATM!")
    print ("Please insert your card")
    restart = 'yes'
    atm_pin = 9999         #stores the assigned values to restart, atm_pin, and balance
    balance = 2000.00
    transaction=["View balance", "Withdraw money", "Deposit money", "Transfer money", "Change pin", "Quit"]      #stores multiple values to transaction
    pin=input("Please enter your pin number ")
    if pin:
        print ('You have entered your pin correctly\n')     #if pin is entered correctly, it will take you to the transactions page, otherwise it will commit to the else condition
        while restart not in ['n', 'no', 'NO', 'N']:
            print ("Please choose your transaction:")
            print ("1. View balance")
            print ("2. Withdraw money")
            print ("3. Deposit money")          #transaction page
            print ("4. Transfer money")
            print ("5. Change pin")
            print ("6. Quit")
            trans = int(input("Transaction: "))
            if trans == 1:
                print ('\nYour current balance is $',balance,'\n')    #prints the current balance 
                restart = input('Would you like to go back? ')       
                if restart in ['n', 'NO', 'no', 'N']:             #if you type yes, the program will take you back to the transaction page
                    print ('Thanks for using Jacks ATM!')
                    break
            elif trans == 2:
                withdrawl = float(input('Enter the amount you would like to Withdraw to proceed. :\n$10/$20/$40/$60/$80/$100 '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl         #when amount to withdrawl is chosen, the value will be subracted from the balance
                    print ('Collect your cash. Your balance is now $',balance) 
                    restart = input('Would you like to go back? ')
                    if restart in ['n', 'NO', 'no', 'N']:
                        print ("Thanks for using Jack's ATM!")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print ('Invalid amount... To proceed please choose a valid amount ')     #if the amount chosen isnt a valid number, the program will ask to enter a valid number
                    restart = ('yes')

            elif trans == 3:
                deposit = float(input("enter the amount you would like to deposit "))        #float is used to describe any moneytary value that can be deposited in the balance
                balance = balance + deposit
                print ('\nYour deposit has been successfully deposited. Your new balance is $',balance) 
                restart = input('Would you like to go back? ')
                if restart in ['n', 'NO', 'no', 'N']:
                    print ('Thanks for using Jacks ATM!')
                    break
            elif trans == 4:
                transfer = float(input("enter the amount you would like to transfer "))
                balance = balance - transfer
                print ('\nYour transfer has been successfully initiated. Your new balance is $',balance) 
                restart = input('Would you like to go back? ')
                if restart in ['n', 'NO', 'no', 'N']:
                    print ('Thanks for using Jacks ATM!')
                    break
            elif trans == 5:
                change = float(input("Enter new pin:"))
                if (0000 < change and change < 9999):          #pin number can be changed to any value between 0000 and 9999
                    pin = change
                    print ('Your pin has been successfully changed. Thanks for using Jacks ATM!')
                    restart = input('Would you like to go back? ')
                    if restart in ['n', 'NO', 'no', 'N']:
                        print ('Thanks for using Jacks ATM!')
                else:
                    print ("Invalid pin number... To proceed please choose a valid pin number")
            elif trans == 6:
                quit = input("Type y to quit ")          #typing "y" will quit the program
                if quit == ('y'):
                    print ("Thanks for using Jack's ATM!")
                    break
    else:
        print ("Wrong pin. Please try again...")

atm()