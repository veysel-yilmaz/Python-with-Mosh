"""prices = [10, 20, 30]
for item in prices:
    print(sum(item))"""
#answer:
prices = [10, 20, 30]
total = 0 # initially set to zero
for price in prices:
    #total = price
    total += price
#print(total)
print(f"Total: {total}")