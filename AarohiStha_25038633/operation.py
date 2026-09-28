from read import read, display
from write import update, invoice, note

def sell():

    data = read()
    display(data)

    customer = input("Enter the customer name: ")

    bill = ""
    total = 0
    product_added = False

    while True:

        product_id = input("Enter your product ID: ")

        found = False

        for item in data:

            if item[0] == product_id:

                found = True

                try:
                    quantity = int(input("Enter your quantity: "))
                except ValueError:
                    print("Enter a valid number.")
                    continue

                stock = int(item[3])
                price = float(item[5])

                if quantity <= 0:

                    print("The quantity should be greater than 0.")
                    continue

                elif quantity > stock:

                    print("No enough stock.")
                    continue

                else:

                    amount = quantity * price

                    discount = 0

                    if item[4] == "kg":

                        if quantity >= 50:
                            discount = amount * 5 / 100

                    else:

                        if quantity >= 100:
                            discount = amount * 5 / 100

                    final = amount - discount

                    total = total + final

                    item[3] = str(stock - quantity)

                    bill = bill + "\n"
                    bill = bill + "Product Name: " + item[1] + "\n"
                    bill = bill + "Brand: " + item[2] + "\n"
                    bill = bill + "Unit: " + item[4] + "\n"
                    bill = bill + "Quantity: " + str(quantity) + "\n"
                    bill = bill + "Price: Rs. " + str(price) + "\n"
                    bill = bill + "Discount: Rs. " + str(discount) + "\n"
                    bill = bill + "Total: Rs. " + str(final) + "\n"

                    product_added = True

                    print("Product is added to bill.")

                break

        if found == False:

            print("Product ID is not found.")

        again = input("Buy another product? (y/n): ")

        if again.lower() != "y":
            break

    if product_added == True:

        bill = bill + "\nGrand Total: Rs. " + str(total) + "\n"

        update(data)

        invoice(customer, bill)

    else:

        print("No product was sold.")


def restock():

    data = read()
    display(data)

    supplier = input("Enter your supplier name: ")

    bill = ""
    total = 0
    product_added = False

    while True:

        product_id = input("Enter your product ID: ")

        found = False

        for item in data:

            if item[0] == product_id:

                found = True

                try:
                    quantity = int(input("Enter the quantity: "))
                except ValueError:
                    print("Enter a valid number.")
                    continue

                if quantity <= 0:

                    print("The quantity should be greater than 0.")
                    continue

                else:

                    stock = int(item[3])
                    price = float(item[5])

                    amount = quantity * price

                    total = total + amount

                    item[3] = str(stock + quantity)

                    bill = bill + "\n"
                    bill = bill + "Product Name: " + item[1] + "\n"
                    bill = bill + "Brand: " + item[2] + "\n"
                    bill = bill + "Unit: " + item[4] + "\n"
                    bill = bill + "Quantity: " + str(quantity) + "\n"
                    bill = bill + "Price: Rs. " + str(price) + "\n"
                    bill = bill + "Total: Rs. " + str(amount) + "\n"

                    product_added = True

                    print("Product is added to restock.")

                break

        if found == False:

            print("Product ID is not found.")

        again = input("Restock another product? (y/n): ")

        if again.lower() != "y":
            break

    if product_added == True:

        bill = bill + "\nGrand Total: Rs. " + str(total) + "\n"

        update(data)

        note(supplier, bill)

    else:

        print("No product was restocked.")