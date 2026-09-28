from read import read, display
from operation import sell, restock
while True:
    print("========== Hardware Store Management System ===========")
    print("1. Show the Products")
    print("2. Sell the Product")
    print("3. Restock the Product")
    print("4. Exit the  program")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = read()
        display(data)

    elif choice == "2":
        sell()

    elif choice == "3":
        restock()

    elif choice == "4":
        print("Thank you .")
        break

    else:
        print("Invalid.")
