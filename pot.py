import csv

def is_valid_crs(crs):
    with open('station_codes.csv', 'r') as station_codes:
        reader = csv.reader(station_codes, delimiter=',', quotechar='|')
        for station in reader:
            if station[1] == crs.strip().upper():
                return True
    return False
