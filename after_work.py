Summer = "T-Shirts, Shorts, Sun Hats, Sun Glasses"
Autumn = "Jacket, Coat, Anorak, Raincoat, Jumper, Cardigon, Trousers, Tights, Wellies, Boots, Hat, Scarf, Hood"
Winter = "Sweater, Beanie, Jacket, Mittens, Socks, Mufflers, Coat, Shawl"
Spring = "T-Shirt, Raincoat, Hat, Shirt, Rain Boots"

month = int(input("Please enter the number of month: "))

if month in [12, 1, 2]:
    print("`You are in Summer")
    print(f"These are the clothes you should wear: {Summer}")
    print("Have fun in Summer")
    
if month in [3, 4, 5]:
    print("You are in Autumn")
    print(f"These are the clothes you should wear: {Autumn}")
    print("Have fun in Autumn")
    
if month in [6, 7, 8]:
    print("You are in Winter")
    print(f"These are the clothes you should wear: {Winter}")
    print("Have fun in Winter")
    
if month in [9, 10, 11]:
    print("You are in Spring")
    print(f"These are the clothes you should wear: {Spring}")
    print("Have fun in Spring")