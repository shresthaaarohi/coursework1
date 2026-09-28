def read():

    data = []

    file = open("hardware.txt", "r")

    for line in file:
        item = line.strip().split(",")
        data.append(item)

    file.close()

    return data


def display(data):

    print("\n========Show the Product List ======")
    print("ID\tName\tBrand\tStock\tUnit\tPrice")

    for item in data:
        print(
            item[0] + "\t" +
            item[1] + "\t" +
            item[2] + "\t" +
            item[3] + "\t" +
            item[4] + "\t" +
            item[5]
        )