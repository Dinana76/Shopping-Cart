
# Create a shopping cart programme thta will continously ask the user for food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At the end show the food Items and the total cast to the user

food=[]
prices=[] 
total=0

while True:
    food = input("Enter a food to buy or press q to quit")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
                           
print("-----Shopping Cart-----")

for food in foods:
    print(food)
    
    for price in prices:
        total += price
        
print(f": your total is {total}")

                   
                