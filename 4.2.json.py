import json
import urllib.request


def printResults(data):
    # print(data)
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print(str(count))

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print('-' * 10)

    # print the event that only have a magnitude greater than 4

    for i in theJSON["features"]:
        if (i["properties"]["mag"] >= 4.0):
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print('-' * 10)

    # print only the events where at least 1 person reported feeling something
    print("Events that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None):
            if (feltReports > 0):
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")


def main():
    webUrl = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson")

    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)


if __name__ == "__main__":
    main()
