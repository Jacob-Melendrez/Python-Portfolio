capitals ={
    'AK':'Juneau',
    'AL':'Montgomery',
    'AR':'Little Rock',
    'AZ':'Phoenix',
    'CA':'Sacramento',
    'CO':'Denver',
}

print()
print(capitals['AK'])
print()

capitals['US'] = 'Washington DC'

print() 
print(capitals['US'])
print() 

del capitals['AK']

for state in capitals:
    print(state)

print()

for capital in capitals.values():
    print(capital)
# These are the 
print()
print(capitals.keys())
print()
print(capitals.values())
print()
print(capitals.items())
print()
