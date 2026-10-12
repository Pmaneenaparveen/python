user_input=input("enter a number:")
number=eval(user_input)
if type(number)==int:
    print(number,"is an integer")
elif type(number)==float:
    print(number,"is a float")
elif type(number)==complex:
    print(number,"is a complex number")


