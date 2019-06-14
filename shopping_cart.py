# shopping_cart.py
import datetime
import csv
import pandas as pd

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
Pounds_banana = 1.0

while True:
    x = input("Please input a product identifier, or 'DONE' if there are no more items:")
    if x.lower() == "done":
        break
    if [p for p in products if str(p["id"]) == str(x)]:   
        Cart.append(x)
        # if p["price_per"] == "pound": TODO 
        #     Pounds_banana = input("Please input the number of pounds: ")
        # else:
        #     continue
    else: # input not equal to 'done' or an existing product identifier, then ask for an input again
        # matching_products = [p for p in products if str(p["id"]) == str(x)]
        # matching_prod = matching_products[0]
        # print("SELECTED PRODUCTS:", matching_prod["name"], "("+str("${0:.2f}".format(matching_prod["price"]))+")")
        # Total_products += 1
        # Total_price += matching_prod["price"]
        # Cart.append(x)
        print("Hey, are you sure that product identifier is correct? Please try again!")
        continue
#print(Cart)

## Checkpoint 2: Printing the Receipt
print("---------------------------------")
print("Uno Dos Tres Grocery")
print("WWW.UNO-DOS-TRES.COM")
print("---------------------------------")
now = datetime.datetime.now()
print("Checkout at:", now.strftime("%Y-%m-%d %I:%M %p"))
print("---------------------------------")
print("SELECTED PRODUCTS:")

for item in Cart:
    matching_products = [p for p in products if str(p["id"]) == str(item)]
    matching_prod = matching_products[0]
    price = str("${0:.2f}".format(matching_prod["price"]*Pounds_banana))
    print(" ...", matching_prod["name"], "("+price+")")
    Total_products += 1
    Total_price += matching_prod["price"]

print("---------------------------------")
print("TOTAL ITEMS IN CART:", str(Total_products))
print("SUBTOTAL:", str("${0:.2f}".format(Total_price)))
nyc_tax = Total_price*0.08875
print("NYC TAX:",str("${0:.2f}".format(nyc_tax)))
sum_total = Total_price+nyc_tax
print("TOTAL:",str("${0:.2f}".format(sum_total)))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")

###########OUTPUT RESULT###########
# Please input a product identifier, or 'DONE' if there are no more items:5
# Please input a product identifier, or 'DONE' if there are no more items:11
# Please input a product identifier, or 'DONE' if there are no more items:12
# Please input a product identifier, or 'DONE' if there are no more items:20
# Please input a product identifier, or 'DONE' if there are no more items:done
# ---------------------------------
# Uno Dos Tres Grocery
# WWW.UNO-DOS-TRES.COM
# ---------------------------------
# Checkout at: 2019-06-14 11:18 AM
# ---------------------------------
# SELECTED PRODUCTS:
#  ... Green Chile Anytime Sauce ($7.99)
#  ... Peach Mango Juice ($1.99)
#  ... Chocolate Fudge Layer Cake ($18.50)
#  ... Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
# ---------------------------------
# TOTAL ITEMS IN CART: 4
# SUBTOTAL: $32.73
# NYC TAX: $2.90
# TOTAL: $35.63
# ---------------------------------
# THANKS, SEE YOU AGAIN SOON!
# ---------------------------------
###########END OUTPUT RESULT###########


## TODO: Handling Pricing per Pound

