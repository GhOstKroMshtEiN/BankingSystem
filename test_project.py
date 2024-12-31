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
            return f'Вы превысисли лимит снятия денег, повторите попытку {Today_data + value_day}'
        
        return 'Лимит обновлен'
        
 
    def deposit(self, amount):
        if amount > 0:
            self.__InfoAmount += amount
            self.__HistoryAllOpp.append(f'Депозит: +{amount}')
            return self.__InfoAmount
        else:
            raise ValueError('Сумма депозита должна быть положительной')
        
    def withdraw(self, amount):
        reset_message = self.ResetLimit()
        try:
            if amount > 0:
                if self.__InfoAmount <= amount:
                    raise ValueError('У вас нет средств для снятия денег')
                
                
                elif self.__daily_withdraw >= self.__daily_limit:
                    return reset_message
                                    
                else:
                    self.__daily_withdraw += 1
                    self.__InfoAmount -= amount
                    self.__HistoryAllOpp.append(f'Снятие: -{amount}')
                    return self.__InfoAmount
                
            else:
                raise ValueError('Сумма снятия не должна быть отрицательной')
            
        except ValueError as a:
            return f'Ошибка: {a}'
            
    def get_balance(self):
        return f'Ваш баланс состовляет {self.__InfoAmount}'
    
    def get_account_number(self):
        if "Ошибка:" in self.__accountNumber:
            return self.__accountNumber
        
        return f'Ваш личный номер аккаунта: {self.__accountNumber}'
    
    def apply_interest(self):
        amount_bid = self.__bid_for_the_year
        value_bid = self.__InfoAmount * (amount_bid / 100)
        valueAmount = value_bid + self.__InfoAmount
        self.__HistoryAllOpp.append(f'Надбавка за процент: +{int(value_bid)}%')
        return f'За 5% годовых мы прибавли к вашей сумме {int(value_bid)}%\nваш баланс состовляет {int(valueAmount)} руб'
    
    def ViewHistory(self):
        if not self.__HistoryAllOpp:
            return f'У вас отсутствует история операций'

        
        return f'Все проведенные операци:\n{"\n".join(self.__HistoryAllOpp)}'
        
        
    """def __str__(self):
        return f"Account Number: {self.__accountNumber}, Balance: {self.__InfoAmount}"""


def UserInpSeting(Input):
    lst = []
    counter = 0
    try:
        for elem in Input:
            counter += 1
            if counter >= 10:
                raise ValueError('Вы привысили лимит ввода номера аккаунта')
            lst.append(elem)
            
        Value = "".join(lst)
        return Value

    except ValueError as e:
        return f'Ошибка: {e}'
    
UserInput = input('Введите ваш номер счета: ') 
account_user1 = Account(accountNumber=UserInpSeting(UserInput), InfoAmount=100)

print(account_user1.withdraw(20))
print(account_user1.withdraw(20))
print(account_user1.apply_interest())
print(account_user1.deposit(20))
print(account_user1.ViewHistory())


print(account_user1.get_account_number())
        