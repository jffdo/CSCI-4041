import random, timeit


def mystery1(vals):
    #     diff = 0
    #     for i in range(len(vals)):
    #         for j in range(len(vals)):
    #             if vals[i] - vals[j] > diff:
    #                 diff = vals[i] - vals[j]
    #     return diff
    return max(vals) - min(vals)


def mystery2(filename):
    # time = {}
    # with open(filename) as fp:
    #     text = fp.read()
    #     for ltr in text:
    #         time[ltr] = text.count(ltr)
    # return time
    time = {}
    with open(filename, encoding="utf8") as file:
        text = file.read()
        for ltr in text:
            if ltr in time:
                time[ltr] += 1
            else:
                time[ltr] = 1
    return time


def mystery3(filename):
    # storage = []
    # with open(filename) as fp:
    #     for line in fp:
    #         items = line.split()
    #         name = items[0]
    #         time = int(items[1])
    #         if time >= len(storage):  # Need more spots in storage
    #             x = time - len(storage) + 1
    #             extend = [""] * x  # Makes a list of x empty strings
    #             storage = storage + extend
    #         storage[time] = name
    # sort_list = []
    # for spot in storage:
    #     if spot != "":  # Ignore empty spots
    #         sort_list.append(spot)
    # return sort_list
    storage = []
    with open(filename, encoding="utf8") as file:
        for line in file:
            items = line.split()
            storage.append(items)
    for i in range(len(storage)):
        for j in range(len(storage) - 1, i, -1):
            if storage[j][1] < storage[j - 1][1]:
                temp = storage[j]
                storage[j] = storage[j - 1]
                storage[j - 1] = temp
    for count, value in enumerate(storage):
        storage[count] = value[0]
    return storage


if __name__ == "__main__":
    lst = [random.randint(0, 9999999) for i in range(1000)]
    time1 = timeit.timeit("mystery1(lst)", globals=globals(), number=10)
    out = mystery1(lst)
    print("mystery1(lst) output:", out)
    print("mystery1(lst) runtime:", time1, "seconds")
    print("\n------------------\n")
    time2 = timeit.timeit('mystery2("wizard.txt")', globals=globals(), number=10)
    out = mystery2("wizard.txt")
    print("mystery2('wizard.txt') output:", out)
    print("mystery2('wizard.txt') runtime:", time2, "seconds")
    print("\n------------------\n")
    time3 = timeit.timeit('mystery3("screentime_ms.txt")', globals=globals(), number=10)
    out = mystery3("screentime_ms.txt")
    print("mystery3('screentime_ms.txt') output:", out)
    print("mystery3('screentime_ms.txt') runtime:", time3, "seconds")
