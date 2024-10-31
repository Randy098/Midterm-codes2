mixed_list = ["mango","grape","apple","banana","peach"]
choice = input("sort or reverse :")

if choice == 'sort':
   mixed_list.sort(key=str)
   print("Alphabetically:", mixed_list)

   mixed_list.reverse
   print("Reverse:", mixed_list)
else:
   print("sort or reverse")