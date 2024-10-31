numbers = [10,20,30,40,50]

username = input("do you want to delete your array ? :")

if username == "yes":
    numbers.clear()
elif username == "no":
    userdata = input("add new data : ")
    numbers.append(userdata)

print(numbers)