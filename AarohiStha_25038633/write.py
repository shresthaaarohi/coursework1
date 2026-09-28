import os
from datetime import datetime


def update(data):

    file = open("hardware.txt", "w")

    for item in data:
        file.write(item[0] + ",")
        file.write(item[1] + ",")
        file.write(item[2] + ",")
        file.write(item[3] + ",")
        file.write(item[4] + ",")
        file.write(item[5] + "\n")

    file.close()


def invoice(name, bill):

    os.makedirs("invoices", exist_ok=True)

    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(
        "invoices",
        name + "_invoice_" + date_time + ".txt"
    )

    file = open(filename, "w")

    file.write("========================================\n")
    file.write("       BUILDING HARDWARE STORE\n")
    file.write("========================================\n")
    file.write("Customer: " + name + "\n")
    file.write("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    file.write("========================================\n")

    file.write(bill)

    file.write("\n========================================\n")

    file.close()

    print("Invoice is created successfully.")
    print("Invoice saved in:", filename)


def note(name, bill):

    os.makedirs("restocks", exist_ok=True)

    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(
        "restocks",
        name + "_restock_" + date_time + ".txt"
    )

    file = open(filename, "w")

    file.write("========================================\n")
    file.write("       BUILDING HARDWARE STORE\n")
    file.write("========================================\n")
    file.write("Supplier: " + name + "\n")
    file.write("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    file.write("========================================\n")

    file.write(bill)

    file.write("\n========================================\n")

    file.close()

    print("Restock note created successfully.")
    print("Restock note saved in:", filename)