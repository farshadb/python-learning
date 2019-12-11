def greet_user(first_name, last_name):
    print(f"Hi, {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("Farshad", "Bolouri")
greet_user(last_name="Jaine", first_name="Mary")
greet_user("John", last_name="Walker")
#We shouldn't use key_world  argument before positional argument
#greet_user(first_name="John", "Walker")
print("Finish")

