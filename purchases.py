number_purchases=int(input("Number of purchases: "))
sales_tax=float(input("Sales tax: "))

people=[]
costs=[]

for w in range(number_purchases):
    person=input("Customer: ")
    cost=float(input("Cost: "))
    people.append(person)
    costs.append(cost)

def add_tax(costs,sales_tax):
    sales_cost=[]
    for item in costs:
        sales_cost.append((item*sales_tax)+item)
    return sales_cost

sales_cost=add_tax(costs,sales_tax)

bob_sales=sales_cost[0]+sales_cost[2]
alice_sales=sales_cost[1]

final_sale={}

final_sale["Bob"]=bob_sales
final_sale["Alice"]=alice_sales

print(final_sale)
