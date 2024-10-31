name = ["senjoo","totoy","olaso","alinar","cornelio"]

userdata = input("do you want to remove any elemenet of this list : ")

if userdata == "yes":
    userdata = input("what name you want to remove?")

name.remove(userdata)

print(name)