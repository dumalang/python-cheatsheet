def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else

    # no switch case block on python, there is only if, elif and else

    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print(st)

    # conditional statement let you use "a if C else b"
    st = "x is less than y" if (x < y) else "x is greater than or the same as y"

    print(st)


main()
