class Checking_Account:
    def __init__(
        self, acc_holder, acc_number=1234, balance=0.00, monthly_charges={}
    ):
        self.acc_holder = acc_holder
        self.acc_number = acc_number
        self.balance = balance
        self.monthly_charges = monthly_charges

    def intrest(self):
        previous_balance = self.balance
        self.balance = self.balance * 1.025
        print(
            f"Your monthly intrest raised your balance of £{previous_balance} too £{self.balance}"
        )

    def show_balance(self):
        print(f"Your balance is £{self.balance}")

    def monthly_out_going(self):
        key = self.monthly_charges.keys()
        value = self.monthly_charges.values()
        self.balance = [self.balance - payment for payment in value]
        # self.balance = self.balance - payment
        print(
            f"Your monthly charge of {value} to {key} left your account. Your new balance is £{self.balance} "
        )

    def deposit(self, inGoing):
        self.balance = self.balance + inGoing
        print(
            f"You have depoisted £{inGoing} into your account, your new balance is £{self.balance}"
        )
    
    def withdraw(self, outGoing):
        self.balance = self.balance - outGoing
        print(
            f"You withdrew £{outGoing} from your account, your new balance is £{self.balance}"
        )


class Savings_Account(Checking_Account):
    def __init__(
        self,
        acc_holder,
        acc_number=1234,
        balance=0
    ):

        super().__init__(acc_holder, acc_number, balance)
        self.acc_holder = acc_holder
        self.acc_number = acc_number
        self.balance = balance

    def intrest(self):
        previous_balance = self.balance
        self.balance = self.balance * 1.08
        print(
            f"Your yearly intrest raised your balance of £{previous_balance} too £{self.balance}"
        )


class Student_Account(Savings_Account):
    def __init__(self, acc_holder, acc_number=1234, balance = 0.00, age = 0, max_credit=-50):
        super().__init__(acc_holder, acc_number, balance)
        self.acc_holder = acc_holder
        self.acc_number = acc_number
        self.balance = balance
        self.age = age
        self.max_credit = max_credit
    
    def age_check(self):
        if self.age <= 18:
            difference = 18 - self.age
            print (f"Unfortauntly you are unable to use the account without an adult, please try again in {difference} years")
        else:
            print("You have been grated a student account, your age is within the limits of our student bank account")

    def withdraw(self, outGoing):
        proposed_balance = self.balance - outGoing
        avalible_balance = self.balance - self.max_credit
        if proposed_balance < (self.max_credit):
              print(f"You are unable to go into more credit that £{self.max_credit}.\nYour avalible balance is {avalible_balance}")
        else:
            self.balance = proposed_balance
            print(f"You withdrew £{outGoing} from your account, your new balance is £{self.balance}")




lees_checking_acc = Checking_Account(
    acc_holder="Jonathan Lees",
    acc_number=3431235,
    balance=5000,
    monthly_charges={"SkySports": 30},
)

lees_saving_acc = Savings_Account(
    acc_holder="Jonathan Lees", acc_number=343123534, balance=75000
)

lees_student_acc = Student_Account(
    acc_holder="Jonathan Lees Jr.", acc_number=165544332, balance=10.50, age= 30
)

lees_jr_student_acc = Student_Account(
    acc_holder="Jonathan Lees Jr.", acc_number=165544332, balance=0.25, age= 11
)