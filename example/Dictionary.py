# start using dictionary
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer['name'])
print(customer["name"])
print(customer.get("birthdate", 1982)) # get is better than [] because wont return error
customer["name"] = "Jack Smith"
customer["birthdate"] = 1982
print(customer["birthdate"])
print(customer)