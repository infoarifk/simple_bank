class Bank:
    totalBalance = 0
    loanAmount = 0
    loanFeature = True


class User():
    __userBalance = 0
    __userLoan = 0
    def __init__(self,name, age, gender) -> None:
        self.userName= name
        self.userAge = age
        self.userGender=gender

    def depsitAmount(self,amount):
        self.deposit = amount
        if self.deposit>0:
            self.__userBalance +=self.deposit
            print("Deposit Successful")
        else:
            print("Invalid amount")

    def withdrawAmount(self, amount):
        self.withdraw = amount
        if self.__userBalance>=self.withdraw:
            self.__userBalance -= self.withdraw
            print("Withdraw Successful")
        else:
            print("Your Balance is Low")

    def userDetails(self):
        print("Personal Details: ")
        print("-------------------------")
        print("Name: ", self.userName)
        print("Age: ", self.userAge)
        print("Gender: ", self.userGender)
        print("Balance: ", self.__userBalance)
        print("Loan: ", self.__userLoan)

# user1 = User("Mst. Shakira Mostarin Raisa", 22, "Female")
# user1.depsitAmount(6000)
# user1.withdrawAmount(500)
# user1.userDetails()



user1 = User("Mst. Shakira Mostarin Raisa", 22, "Female")
user1.depsitAmount(6000)
user1.withdrawAmount(500)
user1.userDetails()



