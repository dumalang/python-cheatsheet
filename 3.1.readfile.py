from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar


def main():
    # Open file for writing or reate it if it doesn't exist
    # f = open("3.0.file.txt", "w+")

    # Open file for appending text to the end
    f = open("3.0.file.txt", "a")

    # Write some lines of data to the file
    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")

    # Close the file while done
    f.close()

    # Read mode
    f = open("3.0.file.txt", "r")

    # Open the file back up and read the contents
    if f.mode == "r":
        # contents = f.read()
        # print(contents)

        # fl = f.readlines()

        # for i in f.readlines():
        #     print("Read Line: " + i)

        # Read string in lenght of param
        fls = f.readline(5)
        print(fls)

    f.close()

if __name__ == "__main__":
    main()
