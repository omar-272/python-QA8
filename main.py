def fun(list,item):
   list.append(item)

n =int(input("Enter size of List:"))
Y = []
for i in range(0,n):
    item = input("Enter item:")
    fun(Y,item)
check = input("Enter the Item You want to check :")
if check in Y:
    print("Your Item",check,"is in the List")
else:print("Your Item",check,"is not in the List")

   