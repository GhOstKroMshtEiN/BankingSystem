from datetime import datetime
from datetime import timedelta


class Account():
    def __init__(self, accountNumber, InfoAmount=0):
        self.__accountNumber = accountNumber
        self.__InfoAmount = InfoAmount
        self.__daily_withdraw = 0
        self.__daily_limit = 2
        self.__bid_for_the_year = 10
        self.__HistoryAllOpp = []
        self.__reset_date_limit = 0
        self.__last_withdraw_date = None
    
    def ResetLimit(self):
        Today_data = datetime.now().date()
        
        if self.__last_withdraw_date != Today_data:
            self.__daily_limit = self.__reset_date_limit
            self.__last_withdraw_date = Today_data
            
        if self.__daily_withdraw >= self.__daily_limit:
            value_day = timedelta(days=1)
            return f'You have exceeded the withdrawal limit, try again on {Today_data + value_day}'
        
        return 'Limit has been reset'
        
    def deposit(self, amount):
        if amount > 0:
            self.__InfoAmount += amount
            self.__HistoryAllOpp.append(f'Deposit: +{amount}')
            return self.__InfoAmount
        else:
            raise ValueError('Deposit amount must be positive')
        
    def withdraw(self, amount):
        reset_message = self.ResetLimit()
        try:
            if amount > 0:
                if self.__InfoAmount <= amount:
                    raise ValueError('You do not have sufficient funds for withdrawal')
                
                elif self.__daily_withdraw >= self.__daily_limit:
                    return reset_message
                                    
                else:
                    self.__daily_withdraw += 1
                    self.__InfoAmount -= amount
                    self.__HistoryAllOpp.append(f'Withdrawal: -{amount}')
                    return self.__InfoAmount
                
            else:
                raise ValueError('Withdrawal amount must not be negative')
            
        except ValueError as a:
            return f'Error: {a}'
            
    def get_balance(self):
        return f'Your balance is {self.__InfoAmount}'
    
    def get_account_number(self):
        if "Error:" in self.__accountNumber:
            return self.__accountNumber
        
        return f'Your account number is: {self.__accountNumber}'
    
    def apply_interest(self):
        amount_bid = self.__bid_for_the_year
        value_bid = self.__InfoAmount * (amount_bid / 100)
        valueAmount = value_bid + self.__InfoAmount
        self.__HistoryAllOpp.append(f'Interest added: +{int(value_bid)}%')
        return f'For 5% annual interest, we added {int(value_bid)}% to your amount.\nYour balance is now {int(valueAmount)} currency units.'
    
    def ViewHistory(self):
        if not self.__HistoryAllOpp:
            return f'You have no transaction history'

        return f'All transactions:\n{"\n".join(self.__HistoryAllOpp)}'


def UserInpSeting(Input):
    lst = []
    counter = 0
    try:
        for elem in Input:
            counter += 1
            if counter >= 10:
                raise ValueError('You have exceeded the input limit for the account number')
            lst.append(elem)
            
        Value = "".join(lst)
        return Value

    except ValueError as e:
        return f'Error: {e}'
    
UserInput = input('Enter your account number: ') 
account_user1 = Account(accountNumber=UserInpSeting(UserInput), InfoAmount=100)
 