class Bank:
    totalBalance = 0
    loanAmount = 0
    loanFeature = True

    @staticmethod
    def showLoan_feature():
        if Bank.loanFeature:
            return "ON"
        else:
           return "OFF"


class User():
    
    def __init__(self,name, age, gender) -> None:
        self.userName= name
        self.userAge = age
        self.userGender=gender
        self.__userBalance = 0
        self.__userLoan = 0
        self.tansaction = []

    def depsitAmount(self,amount):
        
        if amount>0:
            self.__userBalance +=amount
            Bank.totalBalance +=amount
            self.tansaction.append(("Deposit: ", amount))
            print("Deposit Successful")

        else:
            print("Invalid amount")
            self.tansaction.append(("Faild operation", amount))

    def withdrawAmount(self, amount):
        
        if self.__userBalance>=amount:
            self.__userBalance -= amount
            self.tansaction.append(("Withdraw: ", amount))
            print("Withdraw Successful")
        else:
            self.tansaction.append(("Faild operation", amount))
            print("Your Balance is Low")
    
    def transfer(self, toName, amount):
        if self.__userBalance>=amount:
            self.__userBalance-=amount
            self.tansaction.append((f"Transfer to {toName}", amount))
        else:
            self.tansaction.append(("Faild Transfer", amount))
            print("You have not sufficient Balance")

    def transactionHistory(self):
        for history in self.tansaction:
            print(history)

    def userDetails(self):
        print("Personal Details: ")
        print("-------------------------")
        print("Name: ", self.userName)
        print("Age: ", self.userAge)
        print("Gender: ", self.userGender)
        print("Balance: ", self.__userBalance)
        print("Loan: ", self.__userLoan)



class Admin():

    @staticmethod
    def admin_account(name, age, gender):
        return User(name, age, gender)

    
    @staticmethod
    def switch_loan(value):
        Bank.loanFeature = value

    @staticmethod
    def bank_details():
        print("Bank Details")
        print("----------------------")
        print("Total Balance: ",Bank.totalBalance)
        print("Loan Amount: ",Bank.loanAmount)
        print("Loan Feature: ",Bank.showLoan_feature())



# admin = Admin.admin_account("arif", 24, "Male")
# admin.userDetails()

# Admin.bank_details()
user1 =  User("Raisa", 24, "Female")
user1.depsitAmount(20100)

user2 = User("Arif", 14, "Male")
user2.depsitAmount(5000)

user2.withdrawAmount(100000)

user2.transactionHistory()


