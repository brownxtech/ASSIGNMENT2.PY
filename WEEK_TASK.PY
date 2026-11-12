# NUMBER 1
# Shopping_list = []

# while True:
#     item = input("Enter an item: ")
#     if item == "done":
#         break
#     Shopping_list.append(item)
#     print("\nYour shopping list: ")

#     for item in Shopping_list:
#         print(item)



# NUMBER 2
# username = "admin"
# password = "1234"

# attempts = 0

# while attempts < 3:
#     user = input("Enter username: ")
#     pass_word = input("Enter password: ")

#     if user == username and pass_word == password:
#         print("Login successful")
#         print("welcome back")
#         break
#     else:
#         print("Invalid username or password.")
#         attempts += 1

#         if attempts ==3:
#             print("too many attempts.")


# NUMBER 3
number = 44

while True:
    guess = int(input("Guess the number: "))

    if guess > number:
        print("Too high!")

    elif guess < number: 
        print("Too low!")

    else:
        print("Correct! you got it.")