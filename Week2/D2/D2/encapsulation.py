class ATMaccount:

    available_acc_num = 555


    def __init__(self, holder) -> None:
        self.holder = holder 
        self.__account_number = ATMaccount.available_acc_num  #__ = private attribute
        self._balance = 50 #protected
        ATMaccount.available_acc_num += 1


my_account = ATMaccount('Juliana Schmidt')
print(my_account.__dict__)

other_account = ATMaccount('John Doe')
print(other_account.__dict__)

print(my_account._balance)
# print(my_account.__account_number) #error: no attribute
print(my_account._ATMaccount__account_number)

