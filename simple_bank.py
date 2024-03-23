class User():
    __userBalance = 0
    __userLoan = 0
    def __init__(self,name, age, gender) -> None:
        self.userName= name
        self.userAge = age
        self.userGender=gender

    def __depsitAmount(self,amount):
        self.deposit = amount
        if self.deposit>0:
            self.__userBalance +=self.deposit
            print("Deposit Successful")
        else:
            print("Invalid amount")

    def __withdrawAmount(self, amount):
        self.withdraw = amount
        if self.__userBalance>=self.withdraw:
            self.__userBalance -= self.withdraw
            print("Withdraw Successful")
        else:
            print("Your Balance is Low")

    def __userDetails(self):
        print("Personal Details: ")
        print("-------------------------")
        print("Name: ", self.userName)
        print("Age: ", self.userAge)
        print("Gender: ", self.userGender)
        print("Balance: ", self.__userBalance)
        print("Loan: ", self.__userLoan)
