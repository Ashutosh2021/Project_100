class Atm :
    def __init__(self,cardNumber,pinNumber) :
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.initialBalance=5000

    def balanceEnquiry(self) :
        print("Your Current Balance is:",self.initialBalance)

    def withdrawCash(self) :
        amountForWithdrawal = int(input("Please enter the Amount to be withdrawn: "))
        if amountForWithdrawal <= self.initialBalance :
            self.initialBalance=self.initialBalance-amountForWithdrawal
            print("Withdrawal Successful !!")
            self.balanceEnquiry()
        else : 
            print("Unable to withdraw Cash. Amount entered is greater than Current Balance")
atm1 = Atm("20202","30303")
print("Enter 1 for Balance Enquiry")
print("Enter 2 for Withdrawing Cash")
action=int(input("Please enter the number you want to continue with: "))
if action==1 :
    atm1.balanceEnquiry()
else :
    atm1.withdrawCash()