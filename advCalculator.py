import all_functions

print("***Calcultor Pro***")
print("Chooes an option to continue")
print("Press 1 to add")
print("Press 2 to substract")
print("Press 3 to multiplicate")
print("Press 4 to devide")
print("Press 5 to get the power")
print("Press 6 to get the sqaure root")
print("Press 7 to to get the sine value")
print("Press 8 to to get the cosine value")
print("Press 9 to to get the tanget value")
print("Press 10 to exit")

while True:
    user_input = input("Enter the operation number: ")

    if user_input in ('1','2','3','4','5'):
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))

            if user_input == '1':
                result1 = all_functions.add(num1,num2)
                print(result1)
            
            elif user_input == '2':
                result2 = all_functions.sub(num1,num2)
                print(result2)

            elif user_input == '3':
                result3 = all_functions.mul(num1,num2)
                print(result3)

            elif user_input == '4':
                result4 = all_functions.dev(num1,num2)
                print(result4)
            
            elif user_input == '5':
                result5 = all_functions.pow(num1,num2)
                print(result5)

        except ValueError:
            print("Invalid operation choice! Choose the correct option please!")
    elif user_input =='6':
        try:
            num3 = float(input("Enter the number: "))
            result6 = all_functions.root(num3)
        except ValueError:
            print("Invalid input, Please enter numeric values!")

    elif user_input in ('7','8','9'):
        try:
            num4 = float(input("Enter the numeric value: "))
            if user_input =='7':
                result7 = all_functions.sine(num4)
                print(result7)
            elif user_input =='8':
                result8 = all_functions.cos(num4)
                print(result8)
            elif user_input == '9':
                result9 = all_functions.tan(num4)
                print(result9)
        except ValueError:
            print("Inavlid input, Please enter numeric values")
    
    elif user_input == '10':
        print("Exiting the calculator!")
        break
    else:
        print("Invaild operation selection! Try again")
        


            