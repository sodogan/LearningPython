import urllib.request
import json


def main():
    url_data = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.geojson"

    web_url = urllib.request.urlopen(url_data)
    if (web_url.getcode() == 200):
        data = web_url.read()
        result_json = json.loads(data)
        if "title" in result_json["metadata"]:
            title = result_json["metadata"]["title"]
            print("Feed title: {}".format(title))

        count = result_json["metadata"]["count"]
        print(f'{count} events recorded.')

        for i in result_json["features"]:
            print(f' - {i["properties"]["place"]}')
        print("\n----------\n")

        # print the events that only have a magnitude greater than 4
        for i in result_json["features"]:
            if i["properties"]["mag"] > 4:
                print("{:2.1f} at {}".format(i["properties"]["mag"], i["properties"]["place"]))
        print("\n----------\n")

        # print the events that were reportedly felt by someone
        print("Events that were felt")
        for i in result_json["features"]:
            felt_reports = i["properties"]["felt"]
            if felt_reports is not None and felt_reports > 0:
                print("{:2.1f} at {} was reported {} times"
                      .format(i["properties"]["mag"],
                              i["properties"]["place"],
                              felt_reports))


    else:
        print("Received error, cannot parse results")


if __name__ == "__main__":
    main()
