from OSMPythonTools.api import Api
from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import json
import math

'''
start = 41.761038854358034, -74.1187644365503
finish = 41.75233338913655, -74.0980332614358

~ 1.23 miles
~ 1.97 km

NOTES:

1 DEGREE OF LAT/LON == 111km
1 MINUTE IF LAT/LON == 1.85km
'''

def degrees_to_radians(degrees):
    return degrees * math.pi / 180


def distance_between_coords(start_lat, start_lon, dest_lat, dest_lon, units='metric'):
    # get distance between two coordinates, default measurement is metric
    # I so very vaguely understand this... This is the math: http://www.movable-type.co.uk/scripts/latlong.html
    earth_r_km = 6371
    earth_r_m = 3959

    r_lat = degrees_to_radians(dest_lat-start_lat)
    r_lon = degrees_to_radians(dest_lon-start_lon)

    lat1 = degrees_to_radians(start_lat)
    lat2 = degrees_to_radians(dest_lat)

    a = math.sin(r_lat/2) * math.sin(r_lat/2) + math.sin(r_lon/2) * math.sin(r_lon/2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    if units == 'metric':
        print('Distance in Kilometers')
        return earth_r_km * c
    if units == 'imperial':
        print('Distance in Miles')
        return earth_r_m * c


# overpass = Overpass()  # read-only
# nominatim = Nominatim()  # search OSM indexes
# api = Api()  # full OSM API
#
# # way = api.query('relation/4560843')
# nom_query = nominatim.query('41.742501, -74.085034')
# # print(way)
# # print("\n\nDone!")
#
# # print(way.tag('amenity'))
# # print(way.tag('addr'))
# # print(way.tag('name'))
# # print(way.tag('addr:state'))
# print(nom_query.toJSON())
# print(nom_query.displayName())
start = "41.761038854358034, -74.1187644365503"
finish = "41.75233338913655, -74.0980332614358"
print(f"starting coords: {start}\n")
print(f"destination coords: {finish}\n")
print(distance_between_coords(41.761038854358034, -74.1187644365503, 41.75233338913655, -74.0980332614358, 'imperial'))
print()
print(distance_between_coords(41.761038854358034, -74.1187644365503, 41.75233338913655, -74.0980332614358, 'metric'))
