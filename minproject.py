import time
import os

c=0
balance = 10000

while True:
    pin = int(input("Enter PIN:-"))

    if pin <1000 or pin >9999:
     print("Iinvalid PIN, try again")
    c+=1

    if c>=3:
        print("Wait for 10 se")
        time.sleep(10)

        #  os.system("sudo shutdown -h now")
        break

    else:
        print("Welcome to SBI Bank")
        break

    if c < 3:
        while True:
            print("\n1. Check Amount")
            print("2.Deposite Amount")
            print("3.Withdraw Amount")
            print("4. Exit")

            choice= int(input("Enter your choice :-"))

            if choice ==1:
                print("Your account balance is : -₹",balance)

            elif choice ==2:
                amount= int(input("Enterr amount to deposite :-"))

                if amount > 0:
                    balance = balance + amount 
                    print("Amount deposited successfully")
                    print("Your new balance is :- ₹ ", balance)
                else:
                    print("Invalid amount")

            elif choice==3:
                amount=int(input("Enter amount to withdraw :-"))

                if amount > balance:
                    print("Insufficient balance")
                elif amount<=0:
                    print("Invalid amount")
                else:
                    balance = balance - amount
                    print(" Please collect your cash ")
                    print("Remaining balance is :-₹", balance)

            elif choice ==4:
                print("Thank you for using SBI Bank")
                break
            else:
                print("Invalid choice")