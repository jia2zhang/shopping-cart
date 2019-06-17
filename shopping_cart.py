# shopping_cart.py
import datetime
import csv
import pandas as pd
import os #to help us navigate to the new receipts folder later

#from pprint import pprint
## Alternative 1 Data Setup: Keeping a list of products within the source code
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Organic Bananas", "department": "fruits", "aisle": "organic produce", "price": 0.79, "price_per": "pound"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

## TODO: Alternative 2 Data Setup: Read .csv data file -- THIS IS INCOMPLETE
# products = pd.read_csv("C:/Users/Jz67807/Documents/GitHub/shopping-cart/data/products.csv")
csv_file_path = "data/products.csv"

with open(csv_file_path,"r") as csv_file:
    reader = csv.reader(csv_file)
## TODO: Alternative 3 Data Setup: Referencing Google Sheets Datastore -- THIS NEEDS TO BE CODED

# print(products)
# print(type(products))

## Checkpoint 1: Capturing User Inputs & Look-up Products
Total_products = 0
Total_price = 0
Cart = []
# Pounds_banana = 1.0

def to_usd(cost):
    return str("${0:,.2f}".format(cost))


while True:
    x = input("Please input a product identifier, or 'DONE' if there are no more items:")
    if x.lower() == "done":
        break
    Valid_product_identifier = False
    for p in products:
        if str(p["id"]) == str(int(x)): # making sure to trim off leading 0 in front of 'x'
            Valid_product_identifier = True
            if p["price_per"] == "pound":
                Pounds_banana = float(input("Please input number of pounds, e.g. 5.4: "))
                # price = "%.2f" % float(p["price"]*Pounds_banana)
                price = p["price"]*Pounds_banana
                Cart.append(p["name"]+", "+to_usd(price))
                Total_price += price
            else:
                price = to_usd(p["price"])
                Cart.append(p["name"]+", "+price)
                Total_price += p["price"]
            Total_products += 1
    if Valid_product_identifier == False:
        print("Hey, are you sure that product identifier is correct? Please try again!")
        continue
#print(Cart)

## Checkpoint 2: Printing the Receipt
os.chdir("receipts") # navigate to the "receipts" folder
file_name = ""+datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"

with open(file_name, "w") as file: #write the receipt to the "receipts" folder
    file.write("---------------------------------\n")
    file.write("Uno Dos Tres Grocery\n")
    file.write("WWW.UNO-DOS-TRES.COM\n")
    file.write("---------------------------------\n")  
    file.write("Checkout at: "+ datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p"))
    file.write("\n---------------------------------\n")
    file.write("SELECTED PRODUCTS:")

    for item in Cart:
        file.write("\n ..." + item)
        # matching_products = [p for p in products if str(p["id"]) == str(item)]
        # matching_prod = matching_products[0]
        # price = str("${0:.2f}".format(matching_prod["price"]*Pounds_banana))
        # print(" ...", matching_prod["name"], "("+price+")")
        # Total_products += 1
        # Total_price += matching_prod["price"]

    file.write("\n---------------------------------")
    file.write("\nTOTAL ITEMS IN CART: "+ str(Total_products))
    file.write("\nSUBTOTAL: " + to_usd(Total_price))
    nyc_tax = Total_price*0.08875
    file.write("\nNYC TAX: " + to_usd(nyc_tax))
    sum_total = Total_price+nyc_tax
    file.write("\nTOTAL: " + to_usd(sum_total))
    file.write("\n---------------------------------")
    file.write("\nTHANKS, SEE YOU AGAIN SOON!")
    file.write("\n---------------------------------")

with open(file_name, "r") as file: #Finally print out the receipt after finish writing to "receipts" folder
    contents = file.read()
    print(contents)
###########OUTPUT RESULT###########
# Please input a product identifier, or 'DONE' if there are no more items:21
# Please input number of pounds, e.g. 5.4: 2.0 
# Please input a product identifier, or 'DONE' if there are no more items:02
# Please input a product identifier, or 'DONE' if there are no more items:1
# Please input a product identifier, or 'DONE' if there are no more items:17
# Please input a product identifier, or 'DONE' if there are no more items:7
# Please input a product identifier, or 'DONE' if there are no more items:done
# ---------------------------------
# Uno Dos Tres Grocery
# WWW.UNO-DOS-TRES.COM
# ---------------------------------
# Checkout at: 2019-06-16 07:00 PM
# ---------------------------------
# SELECTED PRODUCTS:
#  ...Organic Bananas, $1.58
#  ...All-Seasons Salt, $4.99
#  ...Chocolate Sandwich Cookies, $3.50
#  ...Rendered Duck Fat, $9.99
#  ...Pure Coconut Water With Orange, $3.50
# ---------------------------------
# TOTAL ITEMS IN CART: 5
# SUBTOTAL: $23.56
# NYC TAX: $2.09
# TOTAL: $25.65
# ---------------------------------
# THANKS, SEE YOU AGAIN SOON!
# ---------------------------------
###########END OUTPUT RESULT###########


## TODO: Handling Pricing per Pound - CHECK
## TODO: Writing Receipts to File - CHECK
## TODO: Refractor price-formatting logic into a function called something like to_usd() - CHECK

