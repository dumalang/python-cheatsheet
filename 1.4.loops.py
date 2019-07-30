def main():
    x = 0

    # define while loop
    while (x < 5):
        print(x)
        x = x + 1

    print("=" * 10)

    x = 0

    # define for loop
    for x in range(5, 10):
        print(x)

    print("=" * 10)

    # use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    print("=" * 10)

    # use the break and continue statements
    for x in range(5, 10):
        if (x == 5): continue
        if (x == 8): break
        print(x)

    print("=" * 10)

    # using the enumerate() function to get index
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for index, day in enumerate(days):
        print(index, day)

    print("=" * 10)


main()
