count = [0, 1, 2]
password = "secure123"
user_input = input("Enter password here: ")

for i in count:
    if user_input == password:
        print("Access granted")
        break
    else:
        print("Access denied. Try again.")
        user_input = input("Enter password here: ")
        count[i] += 1

        if count[i] == 2:
            print("Too many unsuccessful attempts. Access denied. Try again in 24hrs")

        
