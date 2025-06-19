from Bank_accounts import *

Dave = BankAccount(1000,"Dave")
Sare = BankAccount(2000,"Sare")
Dave.getBalance()
Dave.deposit(5000)
Sare.deposit(700)
Sare.deposit(700)
Sare.deposit(-400)
Dave.withdraw(1000)
Dave.transfer(9000,Sare )
Jim = InterestRewardsAcc(1000,"Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100,Dave)
Blaze = SavingsAcct(1000,"Blaze")
Blaze.getBalance()
Blaze.deposit(1000)
Blaze.deposit(900)
Blaze.withdraw(2885)
Blaze.transfer(100,Dave )



 
