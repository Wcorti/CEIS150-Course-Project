# Summary: This module contains the user interface and logic for a console-based version of the stock manager program.
# Author: Wesley Corti
# Date: 9/20/2022

from datetime import date, datetime
from stock_class import Stock, DailyData
from account_class import  Traditional, Robo
import matplotlib.pyplot as plt
import csv

def add_stock(stock_list):
      option = ""
      while option != "0":
        print("Adding a stock")
        symbol = input("Enter symbol: ").upper()
        while symbol == "": # input validation loop
            print("Symbol is blank.")
            symbol = input("Enter symbol: ").upper()
        name = input("Enter company name: ")
        while name == "": # input validation loop
            print("Company name is blank.")
            name = input("Enter company name: ")
        goodinput = False # input validation loop
        while not goodinput:
            try:
                shares = float(input("Enter shares: "))
                if shares > 0:
                    goodinput = True
                else:
                    print("Please enter only positive numbers.")
            except ValueError:
                print("Please enter only positive numbers.")
        new_stock = Stock(symbol, name, shares)
        stock_list.append(new_stock)
        option = input("Press enter to add anoter stock or 0 quit:")

# Remove stock and all daily data
def delete_stock(stock_list):
    print("Delete stock ----")
    print("Stock list: [ ", end="")
    for stock in stock_list:
        print(stock.symbol, " ",end="")
    print("]")
    symbol = input("Which stock do you want to delete: ").upper()
    found = False
    i =0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
        i = i + 1
    if found == True:
        print("Deleted", symbol)
    else:
        print("Symbol not found")
    _=input("Press enter to continue")
    
# List stocks being tracked
def list_stocks(stock_list):
    print("Stock list ----")
    print("SYMBOL\t\tNAME\t\tSHARES")
    print("=======================================")
    for stock in stock_list:
        print(stock.symbol," " * (14-len(stock.symbol)),stock.name," " * (14-len(stock.name)),stock.shares)
    print()
    _=input("Press enter to continue")

# Add Daily Stock Data
def add_stock_data(stock_list):
    print("Add Daily Stock Data ----")
    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ",symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        goodinput4 = False # input validation loop
        while not goodinput4 :
            if data == "":
                goodinput4 = True
                print("Date Entry Complete")
                _ = input("*** Press Enter to Continue ***")
                break 
            try:
                date, price, volume = data.split(",")
                daily_data = DailyData(datetime.strptime(date,"%m/%d/%y"),float(price),float(volume))
                current_stock.add_data(daily_data)
                data = input("Enter Date,Price,Volume: ")
            except ValueError:
                print("ERROR enter Data per instructions")
                print("Enter Data Separated by Commas - Do Not use Spaces")
                print("Enter a Blank Line to Quit")
                print("Enter Date,Price,Volume")
                print("Example: 8/28/20,47.85,10550")
                data = input("Enter Date,Price,Volume: ")
    else:
        print("Symbol Not Found ***")
        _= input("Press Enter to Continue ***")

# Function for Retirement account 
def investment_type(stock_list):
    print("Investment Account ---")
    goodinput1 = False # input validation loop
    while not goodinput1:
        try:
            balance = float(input("What is your initial balance: "))
            if balance > 0:
                goodinput1 = True
            else:
                print("Please enter only positive numbers.")
        except ValueError:
            print("Please enter only positive numbers.")
    number = input("What is your account number: ")
    acct= input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        goodinput2 = False 
        while not goodinput2: # input validation loop
            try:
                years = float(input("How many years untill retirement: "))
                if years > 0:
                    goodinput2 = True
                else:
                    print("Please enter only postive numbers.")
            except ValueError:
                print("Please enter only postive numbers.")
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ",robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list=[]
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [",end="")
            for stock in stock_list:
                print(stock.symbol," ",end="")
            print("]")
            symbol = input("Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol =="0":
                break
            goodinput = False # input validation loop
            while not goodinput:
                try:
                    shares = float(input("Enter shares: "))
                    if shares > 0:
                        goodinput = True
                    else:
                        print("Please enter only positive numbers.")
                except ValueError:
                    print("Please enter only positive numbers.")
            found = False
            for stock in stock_list:
              if stock.symbol == symbol:
                  found = True
                  current_stock = stock
            if found == True:
                current_stock.shares += shares 
                temp_list.append(current_stock)
                print("Bought ",shares,"of",symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)

# Function to create stock chart
def display_stock_chart(stock_list,symbol):
    date = []
    price = []
    volume = []
    company = ""
    for  stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)
    plt.plot(date, price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(company)
    plt.show()

# Display Chart
def display_chart(stock_list):
    print("Stock Chart--")
    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Which stock do you want to use for a chart?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        display_stock_chart(stock_list, current_stock.symbol)
        _=input("Press Enter to Continue ***")
    else:
        print("Symbol Not Found ***")
        _=input("Press Enter to Continue ***")

# Get price and volume history from Yahoo! Finance using CSV import.
def import_stock_csv(stock_list):
    print("This method is under construction")
    
# Display Report 
def display_report(stock_list):
    print("This method is under construction")

# Main menu     
def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option =="0":
            print("Goodbye")
            break
        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
           add_stock_data(stock_list) 
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:
            print("Goodbye")

# Begin program
def main():
    stock_list = []
    main_menu(stock_list)

# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()