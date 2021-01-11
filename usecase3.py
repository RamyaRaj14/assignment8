# menu based Calc for 2 numbers

choice = 0

while True:
    print ("Welcome to calculator")
    print("your options are:")
    print(" ")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit calculator")

    choice = input("choose your option: ")
    try:
        if choice == 1:
            add1 = input("add this: ")
            add2= input("to this: ")
            print(add1, "+", add2, "=", add1+ add2)
        elif choice == 2:
            sub1 = input("Subtract this ")
            sub2 = input("from this")
            print(sub1, "-", sub2, "=", sub1 - sub2)
        elif choice == 3:
            mul1 = input("Multiply this: ")
            mul2 = input("with this: ")
            print(mul1, "x", mul2, "=", mul1 * mul2)
        elif choice == 4:
            div1 = input("Divide this: ")
            div2 = input("by this: ")
            if div2 == 0:
                print("Error! Cannot divide by zero!")
            else:

                print(div1, "/", div2, "=", div1 * div2)
        elif choice == 5:
            break
        else:
            print("%d is not valid input. Please enter 1, 2 ,3 ,4 or 5." % choice)

    except ValueError:
        print("%r is not valid input.  Please enter 1, 2, 3, 4 or 5." % choice)
    print("Thank you for using calculator")
    