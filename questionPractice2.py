# create account class with 2 attributes - balance & account no create methods for debit credit and printing the balance
class Account:
    def __init__(self,accbalance,accNum):
        self.__accbalance = accbalance
        self.__accNum = accNum
        
    def getBalanceDetails(self,accNum):
        if(accNum == self.__accNum):
            return self.__accbalance
        else:
            return f"incorrect account number"
        
    def debitMoney(self,accNum,debitMoney):
        if(self.__accNum == accNum):
            if(debitMoney > self.__accbalance):
                return f"not enough money to withdraw"
            else:
                self.__accbalance -= debitMoney
    
    def creditMoney(self,accNum,creditMoney):
        if(creditMoney > 99):
            if(self.__accNum == accNum):
                self.__accbalance += creditMoney
                return f"money added succesfully"
        else:
            return f"invalid amount to credit"

person1 = Account(20000,123)
person1.creditMoney(123,450000)
print(person1.getBalanceDetails(123))