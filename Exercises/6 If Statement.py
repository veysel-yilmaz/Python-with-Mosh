Price = 1000000
is_good_credit = True
if is_good_credit:
    print(Price * 0.9)
else: # syntax error has shown due to the missing colon
    print(Price * 0.8)
# Answer:
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")