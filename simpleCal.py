import all_operations

print("*** Simple Calculator ***")
print("Choose an option to continue")
print("Press 1 for addition")
print("Press 2 for substraction")
print("Press 3 for multiplication")
print("Press 4 for substraction")
print("Press 5 for exiting thr calculator")

while True:
    user_command = input("Enter your choice: ")

    if user_command in ('1','2','3','4'):
        try:
            num1 = int(input("Enter the 1st number: "))
            num2 = int(input("Enter the second number: "))

            if user_command == 1:
                result1 = all_operations.addition(num1,num2)
                print(result1)
            elif user_command == 2:
                result2 = all_operations.substraction(num1,num2)
                print(result2)
            elif user_command == 3:
                result3 = all_operations.mul(num1,num2)
                print(result3)
            elif user_command == 4:
                result4 = all_operations.dev(num1,num2)
                print(result4)
        except ValueError:
            print("Invalid input, please enter numeric values")
    elif user_command == '5':
        print("Exiting the calculator")
        break
    else:
        print("Invalid choice, please enter the correct choice")

                
        
    
