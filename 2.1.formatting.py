from datetime import date
from datetime import time
from datetime import datetime


def main():
    now = datetime.now()

    # date formatting
    print(now.strftime("%a, %d, %B, %y"))
    # locale datetime
    print(now.strftime("Local date and time: %c"))
    print(now.strftime("Local date: %x"))
    print(now.strftime("Local time: %X"))
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24Hour time: %H:%M"))


if __name__ == "__main__":
    main()
