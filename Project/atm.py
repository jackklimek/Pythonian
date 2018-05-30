class atm():

    print ("Welcome to Jack's ATM!")
    print ("Please insert your card")
    restart = 'yes'
    atm_pin = 9999
    balance = 2000.00
    transaction=["View balance", "Withdraw money", "Deposit money", "Transfer money", "Change pin", "Quit"]
    pin=input("Please enter your pin number ")
    if pin:
        print ('You have entered your pin correctly\n')
        while restart not in ['n', 'no', 'NO', 'N']:
            print ("Please choose your transaction:")
            print ("1. View balance")
            print ("2. Withdraw money")
            print ("3. Deposit money")
            print ("4. Transfer money")
            print ("5. Change pin")
            print ("6. Quit")
            trans = int(input("Transaction: "))
            if trans == 1:
                print ('\nYour current balance is $',balance,'\n')
                restart = input('Would you like to go back? ')
                if restart in ['n', 'NO', 'no', 'N']:
                    print ('Thanks for using Jacks ATM!')
                    break
            elif trans == 2:
                withdrawl = float(input('Enter the amount you would like to Withdraw to proceed. :\n$10/$20/$40/$60/$80/$100 '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print ('Collect your cash. Your balance is now $',balance) 
                    restart = input('Would you like to go back? ')
                    if restart in ['n', 'NO', 'no', 'N']:
                        print ("Thanks for using Jack's ATM!")
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print ('Invalid amount... To proceed please choose a valid amount ')
                    restart = ('yes')

            elif trans == 3:
                deposit = float(input("enter the amount you would like to deposit "))
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
                if (0000 < change and change < 9999):
                    pin = change
                    print ('Your pin has been successfully changed. Thanks for using Jacks ATM!')
                    restart = input('Would you like to go back? ')
                    if restart in ['n', 'NO', 'no', 'N']:
                        print ('Thanks for using Jacks ATM!')
                else:
                    print ("Invalid pin number... To proceed please choose a valid pin number")
            elif trans == 6:
                quit = input("Type y to quit ")
                if quit == ('y'):
                    print ("Thanks for using Jack's ATM!")
                    break
    else:
        print ("Wrong pin. Please try again...")

atm()