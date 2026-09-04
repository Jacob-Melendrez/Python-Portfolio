def shipping_cost(weight):
    if weight < 5:
        cost = 6
    elif weight >=5 and weight < 20:
        cost = 12
    else:
        cost = 25
    return cost

print(shipping_cost(3))
print(shipping_cost(15))
print(shipping_cost(20))
