#Jonathan Lindahl
#Hw 7

def tester():
    dict = startUp()
    print()
    if dict == None:
        return
    pin, msg = verifyPin(dict)
    if pin == None:
        print(msg)
        return 'Goodbye'
    name = msg

    while True:
        print()
        choice = displayMenu(name)
        if choice == 1:
            deposit(pin, dict)
        elif choice == 2:
            withdraw(pin, dict)
        elif choice == 3:
            b = balance(pin, dict)
            msg = 'Current balance is ${:,.2f}'
            print('\n',msg.format(b))
        elif choice == 4:
            reply = quit(pin, dict)
            if reply == 'n':
                pass
            else:
                return 'Goodbye'
    return



def startUp():
    infile = open('accounts.csv', 'r')
    d = {}
    lines = infile.readlines()
    for line in lines:
        lst = line.strip().split(',')
        pin = lst[0]
        name = lst[1]
        last = lst[2]
        balance = float(lst[3])

        data = [name, last, balance]

        d[pin] = data
       
 

    infile.close()
    return d
    


def verifyPin(d):
    wrong = 0
    msg = 'Please call customer support at 800-000-0000'

    while wrong <= 2:
        if wrong == 0:
            print("Welcome -- Enter pin number")

        pin = input()
        
        if pin in d:
            return(pin, d[pin][0])
        else:
            wrong += 1 
            if wrong < 3:
                print('Invalid pin, try again: ')
                   
        
    return(None, msg)

    

def displayMenu(name):
    print(f"{name}:")
    print("1. Deposit\n2. Withdraw\n3. Balance\n4. Quit")
    return verifyMenuChoice()


def verifyMenuChoice():
    num = [1,2,3,4]
    

    while True:
        print()
        choice = input('Enter choice: ')
        if int(choice) in num:
            return int(choice)
        else:
            print('Enter 1 or 2 or 3 or 4, try again')
    return
   

def verifyAmount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount < 0:
                print("Negative amount. Try again.")
            else:
                return amount
        except ValueError:
            print("Invalid amount. Use digits only.")


def deposit(pin,d):
    amount = verifyAmount()
    d[pin][2] += amount


def withdraw(pin, d):
    while True:
        amount = verifyAmount()
        if amount > d[pin][2]:
            print("Insufficient funds to complete the transaction, try again")
        else:
            d[pin][2] -= amount
            break


def balance(pin, d):
    return d[pin][2]


def quit(pin, d):
    choice = input("Do you want to leave the application? (y/n): ")
    if choice.lower() == "y":
        receipt(pin, d)
    return choice

def receipt(pin, d):
    import datetime
    date = datetime.date.today()
    name = f"{d[pin][0]} {d[pin][1]}"
    balance = d[pin][2]
    
    print()
    print("ABC Bank Branch Receipt".center(40))
    print("123 Bank St.".center(40))
    print("Anytown, USA".center(40))
    print()
    print(f"Date: {date}")
    print(f"Name: {name}")
    print(f"Available Balance: ${balance:.2f}")
    print()
    print("Thank you for using the ABC Banking System")





    
        
