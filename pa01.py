import csv


def find_closest(filename):
    table = []

    with open(filename, encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Ignore the first row
        for line in csvreader:
            table.append([line[0], float(line[1])])

    account1_name = ""
    account2_name = ""
    closest = float("inf")

    for index in range(len(table) - 1):
        account = table[index]
        for i in range(index + 1, len(table)):
            distance = abs(account[1] - table[i][1])
            if distance < closest:
                closest = distance
                account1_name = account[0]
                account2_name = table[i][0]

    return [account1_name, account2_name]


if __name__ == "__main__":
    find_closest("bank1.csv")
    find_closest("bank2.csv")
    find_closest("bank3.csv")
    find_closest("bank4.csv")
    find_closest("bank5.csv")
    find_closest("bank6.csv")
