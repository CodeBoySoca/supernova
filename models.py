from pymongo import MongoClient
from dotenv import load_dotenv
from passlib.hash import pbkdf2_sha256
import os

load_dotenv('.env')
client = MongoClient(os.getenv('MONGO_URI'))
db = client.supernova
portfolio = db['portfolio']
assets = db['assets']


class Asset:
    def retrieve():
        cursor = assets.find({})
        items = []
        for document in cursor:
            items.append(document)
        return items
                
class Account:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def create(email, password):
        pass

    def find(email, password):
        pass
    
    def cancel(email, password):
        pass


class Portfolio(Account):
    def __init__(self, name, shares, price, purchase_date):
        self.name = name
        self.shares = shares
        self.price = price
        self.purchase_date = purchase_date
    
    def buy_share(name, shares, price, purchase_date):
        pass

    def sell_share(name, number_of_shares):
        pass


class InvestmentCalculator:
    def adjust_item_percentage():
        pass

    def get_percentage():
        pass

    def item_value():
        pass

    def portfolio_value():
        pass

    def adjust_market_price():
        pass

# class Portfolio:
#     _fields = {
#       'name',
#       'email',
#       'password',
#       'funds',
#       'assets'
#     }

# class Assets(SubFrame):
#     _fields = {
#         'name',
#         'shares',
#         'price' ,
#         'purchase_date'
#     }