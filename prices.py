#CEIS150 Wesley Corti

count = 0
sum = 0
name = input("What is your full name: ")
min_price = float(input("What is the minimum price: "))
price_list = [1.5, 10.0, 15.6, 33.5, 69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2, 300.55]
for price in price_list:
    sum += price
    for i in price_list: 
            if i>min_price:
                count = count+1
print("Hello",name,"the minimum price is ",min_price)
print("There are" ,count,"prices greater than the minimum price")
print("The total price is ",sum)