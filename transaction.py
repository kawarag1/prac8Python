import os
import pickle
import tempfile

class Transaction:
    def __init__(self, amount, date, currency="USD", usd_conversion_rate = 1, description = None):
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description

    @property
    def amount(self):
        return self.__amount
    
    @property
    def date(self):
        return self.__date
    
    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate


    @property
    def description(self):
        return self.__description
    
    @property 
    def usd(self):
        return self.__amount * self.__usd_conversion_rate



class Account():
    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__transactions = []

    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_name(self):
        return self.__account_name
    

    @account_name.setter
    def account_name(self, value):
        if len(value) < 4:
            raise ValueError("Название счёта не должно быть меньше 4-х символов")
        self.__account_name = value


    def _len(self):
        return len(self.__transactions)
    

    @property
    def balance(self):
        return sum(transaction.usd for transaction in self.__transactions)


    @property
    def all_usd(self):
        return all(transaction.currency == "USD" for transaction in self.__transactions)
    

    def apply(self, transaction):
        self.__transactions.append(transaction)

    def save(self):
        file_name = f"{self.__account_number}.acc"
        with open(file_name, "wb") as file:
            pickle.dump(self.__account_number, self.__account_name, self.__transactions, file)

    def load(self):
        file_name = f"{self.__account_number}.acc"
        with open(file_name, "rb") as file:
            self.__account_number, self.__account_name, self.__transactions = pickle.load(file)




transaction = Transaction(100, "2023-10-01", "EUR", 1.1, "Sample transaction")
print(transaction.amount)  
print(transaction.date)     
print(transaction.currency)  
print(transaction.usd_conversion_rate)  
print(transaction.description)  
print(transaction.usd)  



















