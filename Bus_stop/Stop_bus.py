from requests import get
from geopy.distance import distance
URL = 'https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json'
bus_stop_get = get(URL)
bus_stop_data_json = bus_stop_get.json()
bus_stop_date = bus_stop_data_json["2020-08-15"]['stops']
names = []
distance_t = []
index =0
homne = (54.408938, 18.569061)

