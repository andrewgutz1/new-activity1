user_num = int(input("How many numbers do you want to enter? "))
listnum = []

for i in range(user_num):
    numbers = int(input("Enter a number: "))
    listnum.append(numbers)  
    
    if numbers > 0: 
        print("The number is positive")
    elif numbers < 0:  
        print("The number is negative")
    else: 
        print("The number is zero")
        listnum.append(numbers)

print(listnum)

for data in listnum:
    if data > 0:
        print(data, "This number is positive")
    elif data < 0:
        print(data, "This number is negative")