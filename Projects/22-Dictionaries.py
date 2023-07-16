"""Name: John Smith
Email: john@gmail.com
Phone: 1234"""
#name, email and phone are keys and each key is associated
#with a value, which requires dictionaries
customer = {
    "name": "John Smith",
    "age": 30, #if we add age:40, it is not allowed, no duplicates!
    "is_verified": True
}
print(customer["name"])
#print(customer["birthdate"]) #generates keyerror, or the same error with "Name" with capital N
print(customer.get("birthdate"))#wont generate error,will return none
#none is the absence of a value
print(customer.get("birthdate", "Jan 1 1980"))
customer["name"] = "Jack Smith"
print(customer["name"])

