price = float(input("Enter the price: "))



if price < 0:
    discounted_price = price  
elif price >= 300:
    discounted_price = price * 0.7  
elif price >= 200:
    discounted_price = price * 0.8  
elif price >= 100:
    discounted_price = price * 0.9  
else:
    discounted_price = price * 0.95  

print("Discounted price:", discounted_price)