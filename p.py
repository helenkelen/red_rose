#show user text for add first number
print("Enter first number")

#get first user number
firstusernumber = int(input())

#user choose do
print("Enter +, -, *, /")

#operator
useroperator = input()

#show user text for add second number
print("Enter second number")

#get second user number
secondusernumber = int(input())

if(useroperator == "+"):
    adding = firstusernumber + secondusernumber
    print(adding)
elif(useroperator == "-"):
    subt = firstusernumber - secondusernumber
    print(subt)
elif(useroperator == "*"):
    mult = firstusernumber * secondusernumber
    print(mult)
elif(useroperator == "/"):
    div = firstusernumber / secondusernumber
    print(div)
    