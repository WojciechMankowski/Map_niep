from folium import Map, Marker, Icon, FeatureGroup, LayerControl
from Museum.geographical_coordinates import *
from Museum.Information import *
from Cinema.geographical_coordinates import *
from Cinema.Information import *

index_m = 0
index_c = 0
index_lon = 0
index_long = 1
index_lon_c = 0
index_long_c = 1
index_nazwa = 0
index_nazwa_c = 0
pr = True
gdansk_map = Map(location=[54.346320, 18.649246],zoom_start=15)

muzeum_grups = FeatureGroup(name="Muzea w Gdańsku")
cinema_grups = FeatureGroup(name="Kina w Gdańsku")
for index_m in enumerate(adres_museum):
   lon = muzeum[index_lon]
   long = muzeum[index_long]
   tooltip = name_museum[index_nazwa]
   my_icon = ikonka_museum[index_nazwa]
   popup = availability_museum[index_nazwa]
   Marker(location=[lon, long],
          popup=popup,
          tooltip=tooltip,
          icon=Icon(icon=my_icon, prefix="fa",color="darkblue")).add_to(muzeum_grups)
   index_lon += 2
   index_long += 2
   index_nazwa += 1

while pr:
    if index_lon_c != 10 or index_long_c != 11:
        lon_c = cinema[ index_lon_c]
        long_c = cinema[ index_long_c]
        tooltip_c = name_cinema[index_nazwa_c]
        my_icon_c = ikonka_cinema[0]
        popup_c = availability_cinema[index_nazwa_c]
        Marker(location=[lon_c, long_c], popup=popup_c,
               tooltip=tooltip_c,
               icon=Icon(icon=my_icon_c, prefix="fa", color="darkblue")).add_to(cinema_grups)
        Marker(location=[54.348807, 18.643805],
               popup= "Kino znajduje się w centrum handlowym na poziomie +2. Wydzielone są miejsca na wózki. Toalety są dostosowane do osób z niepełnosprawnością znajdują się zaraz obok sal. Winda obsługuje wszystkie piętra.",
               tooltip='Kino Helios "Forum Gdańsk"',
               icon=Icon(icon=my_icon_c, prefix="fa", color="darkblue")).add_to(cinema_grups)
        index_lon_c += 2
        if index_long_c == 11:
            index_long_c += 0
        else:
            index_long_c += 2

    else:
        pr = False
    index_nazwa_c += 1



muzeum_grups.add_to(gdansk_map)
cinema_grups.add_to(gdansk_map)
LayerControl().add_to(gdansk_map)
print("Zapisz")
gdansk_map.save("maps_gdansk.html")

