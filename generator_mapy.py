from geopy.geocoders  import *
from Lista import ob_kul, nazwa_ob_kult

geolocator = Nominatim(user_agent="map-test")
geografy = []
longer = len(ob_kul)
for index_geografy in range(longer):
    location = geolocator.geocode(ob_kul[index_geografy])
    X = location.latitude
    Y = location.longitude
    geografy.append(X)
    geografy.append(Y)
    # print(ob_kul[i])
    index_geografy += 1
