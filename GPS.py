import csv
from gmplot import gmplot

# place map location
# lat, long, zoom
gmap = gmplot.GoogleMapPlotter(28.689169, 77.324448, 17)

gmap.coloricon = "https://www.googlemapsmarkers.com/v1/%s/"

with open("route.csv", "r") as route :
    reader = csv.reader(route)      # creates an iterator so that we can read the values one by one
    k = 0

    for row in reader :
    # row will contain list split by commas of csv
    # the values will be string and not float
        lat = float(row[0])
        long = float(row[1])
        
        if (k == 0) :
            gmap.marker(lat, long, "violet")  # put the marker at first lat long
            k = 1
        else :
            gmap.marker(lat, long, "blue")

gmap.marker(lat, long, "red")

gmap.draw("MyMap.html")
