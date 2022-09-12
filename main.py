import random
import os
from ast import literal_eval

def geDetails():
    infoDict = {}
    infoDict["fname"] = input("Enter Your First Name : ")
    infoDict["lname"] = input("Enter Your Last Name : ")
    infoDict["fatherName"] = input("Enter Your Father's Name : ")
    infoDict["aadharNum"] = int(input("Enter Your Aadhar Card Number : "))
    infoDict["minimumAmount"] = int(input("Enter Minimum Amount : "))
    return infoDict

def getCardDetails():
    cardInfo = {}
    cardInfo["cardNum"] = int(input("Enter Your Card Number : "))
    cardInfo["cardOwnerName"] = input("Enter Card Owner Name (Name on the Card) : ")
    cardInfo["cardCvv"] = int(input("Enter Your Card's CVV : "))
    cardInfo["pinNum"] = int(input("Enter Your Card's Pin Number : "))
    return cardInfo    
    

def closeBankAccount():
    mainFile = []
    enteredFile = []
    info = geDetails()
    info["accountNum"] = int(input("Enter Your Account Number : "))
    accountNumber = info["accountNum"]
    if os.path.exists(f"accInfo/{accountNumber}.txt"):
        with open(f"accInfo/{accountNumber}.txt",'r') as f:
            content = f.read()
        if str(info) in content:
            os.remove(f"accInfo/{accountNumber}.txt")
            print("Account Closed ! Thank You !!")
        else:
            print("You Have Entered Wrong Details !")
    else:
        print("File Not Found !")

def applyForAIOCard():
    print("Enter Details to Confirm it's You : ")
    forCardInfo = geDetails()
    forCardInfo["accountNum"] = int(input("Enter Your Bank Account Number : "))
    accountNumber = forCardInfo["accountNum"]

    if os.path.exists(f"accInfo/{accountNumber}.txt"):
        with open(f"accInfo/{accountNumber}.txt",'r') as f: # by default file operation is in read mode
            content = f.read()
        # print(content)
        # print(forCardInfo)
        if str(forCardInfo) in content:
            print("Account Matched !")
            temp = input("Type Yes To apply for the All in One Card !")
            if temp.lower() == 'yes':
                cardInfoDict = {}
                cardInfoDict["cardNumber"] = random.randint(111111111111, 999999999999)
                cardInfoDict["cardOwnerName"] = forCardInfo['fname'].upper()
                cardInfoDict["cardCvv"] = random.randint(111, 999)
                cardInfoDict["pinNum"] = random.randint(1111, 9999)

                for items in cardInfoDict.items():
                    print(items)
                
                with open(f'cardsInfo/{accountNumber}AIO.txt','w') as f:
                    f.write(str(cardInfoDict))
                print("Your Card is Activated From Now ! Thank You !!")    
        else:
            print("It Seems That You have Entered Wrong Detials !")
    else:
        print("Account Not Found !")        

def withDrawMoney():
    cardInfoDetails = getCardDetails()
    cardAccNum = 0
    files = os.listdir('cardsInfo/')
#    print(files)
    
    for fileName in files:
        with open(f"cardsInfo/{fileName}") as f:
            content = f.read()
        # print(content)            
        print("Entered Details : ")
        print(cardInfoDetails)
        if str(cardInfoDetails) in content:
            cardAccNum = fileName
            
    with open(f"accInfo/{cardAccNum}") as f:
            rawContent = f.read()
    content = literal_eval(rawContent)
    balance = content['minimumAmount']
    print(f"Balance in Your Account : {balance}")
    
    withDrawAmount = int(input("Enter Amount Which You want To Withdraw : "))
    remainingAmount = 0
    if withDrawAmount <= balance:
        remainingAmount = balance - withDrawAmount
        print(f"{withDrawAmount} INR is Withdrawed from {balance} INR and the Remaining Amount is {remainingAmount} INR")
    else:
        print(f"Insufficient Bank Balance i.e - Your Account Balance {balance}")
    

# Main Program
print("Welcome to Central Bank")
print("\n------------------------------------------")
print('''
    Operation :
    1. Open Bank Account
    2. Close Bank Account
    3. Apply For All In One Card
    4. Withdraw Money
    5. Deposit Money
    6. Feedback
''')
choice = int(input("\nEnter Your Choice : "))

if choice == 1:
    print("\nChoice : Open Bank Account\n")
    accInfo = geDetails()
    accInfo["accountNum"] = random.randint(111111111111,999999999999)
    accNum = accInfo["accountNum"]
    with open(f"accInfo/{accNum}.txt",'w') as f:
        f.write(str(accInfo))
    print(f"Your Account Number : {accNum}")
    print("Account Created !")
elif choice == 2:
    closeBankAccount()
elif choice == 3:
    applyForAIOCard()
elif choice == 4:
    withDrawMoney()
elif choice == 5:
    pass
elif choice == 6:
    pass
else:
    pass
