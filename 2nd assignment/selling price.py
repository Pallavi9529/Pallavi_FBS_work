#WAP to calculate selling price of book based on cost price and discount
cost_price=int(input("enter the cost price:"))
discount=int(input("enter the discount:"))
dis_amount=(discount/100*cost_price)
selling_price=(cost_price-discount)
print("selling price of the book:",selling_price)