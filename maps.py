import folium
# from map import gdansk_map
from generator_mapy import geografy_c

maps = folium.Map(location=[54.346320, 18.649246])
folium.Map(location=[54.346320, 18.649246],zoom_start=25)
index_long = 0
index_lon = 1
lon = geografy_c[index_long]
long = geografy_c[index_lon]
for index_map2 in range(3):
    folium.Marker(
        location=[lon, long],
        popup="tekst",
        tooltip="tekst",
        icon=folium.Icon(icon="thumbs-up", prefix='fa')).add_to(maps)
    index_map2 += 1
maps.save("mapa2.html")