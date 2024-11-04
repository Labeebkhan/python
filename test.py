#Banking Application
#To Check Balance
def show_balance(balance):
    print("**********************")
    print(f'Your Current Balance = ${balance}')

#To Deposit The Amount
def Deposit():
    deposit = float(input("Enter The Ammount To Deposit = "))
    if deposit <0:
        print("That's not valid")
    else:
        return deposit 
    
#To Withdraw Amount 
def withdraw():
    print('******************')
    amount = int(input("Enter The Amount = $"))
    if balance <= 0:
        print(f"You're current Balance = ${balance}")
    else:
        print(f"You've Withdrawl Amount = ${amount}")        
    return amount


balance = 0
condition = True
print('''*********************
  Banking Programme
*********************''')
while condition:
    choice = int(input("Enter Your Choice (1-4): "))
    if choice <=4:
        if choice == 1:
            show_balance(balance)
        elif choice ==2:
            balance += Deposit()
        elif choice == 3:
            balance -=withdraw()
            print(f"You're Remainning Balance ${balance}")
        else:
            print("Exited!!")
            break
    else :
        print("Select Right Option")
print("Thankyou For Choosing Us 🙂")