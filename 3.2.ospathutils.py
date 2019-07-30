import datetime
import os
import time
from os import path


def main():
    # Print the name of os
    print(os.name)

    # Check if item existance and type
    print("Item exist: " + str(path.exists("3.0.file.txt")))
    print("Item is a file: " + str(path.isfile("3.0.file.txt")))
    print("Item is a directory: " + str(path.isdir("venv")))

    # Work with filepath
    print("Item path: " + str(path.realpath("3.0.file.txt")))
    print("Item path and name: " + str(path.split(path.realpath("3.0.file.txt"))))

    # Get modification time
    t = time.ctime(path.getmtime("3.0.file.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("3.0.file.txt")))

    # Calculate how long the item was modified

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        path.getmtime("3.0.file.txt")
    )

    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


if __name__ == "__main__":
    main()
