#menu based ATM App with Deposit and Withdraw functions
class LimitExceedException(Exception):
 def __init__(self,amount):
    
    print("\n Amount Deposited:",amount)
class InvalidMinimumException(Exception):
 def __init__(self,amount):
     
    if self.balance>=amount: 
        self.balance-=amount 
        print("\n You Withdrew:", amount) 
class  InsufficientFundException(Exception):
 def __init__(self,amount):
    print("Insufficient")

amount = float(input("Enter amount to be Withdrawn: "))
if amount>10000:
 raise LimitExceedException("Limit exceed")
elif amount<100:
 raise InvalidMinimumException("Minimum amount")
elif amount<balance:
 raise  InsufficientFundException("Insufficient")

else:
 print("bye")
