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

final_sale={}

for w, person in enumerate(people):
    if person in final_sale:
        final_sale[person]+=sales_cost[w]
    else:
        final_sale[person]=sales_cost[w]

print(final_sale)
