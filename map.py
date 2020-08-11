import folium
from folium import *
from random import randint
from generator_mapy import geografy
from Lista import dostepnosc, nazwa_ob_kult, ob_kul, icon, kolory


def Maps():
    # obsługa błędu

    gdansk_map = folium.Map(
        location=[54.346320, 18.649246],
        zoom_start=15,
        position="relative",
        control_scale=True,
    )
    # folium.Map(location=[54.346320, 18.649246],zoom_start=120)
    length = len(ob_kul)
    index_map = 0
    index_long = 0
    index_lon = 1
    while index_map != length:
        poup = dostepnosc[index_map]


        index = 0
        for index in range(length):
            index_kolor = randint(0, 2)
            color = kolory[index_kolor]
            index += 1
        ikonka = icon[index_map]
        toolip = nazwa_ob_kult[index_map]
        lon = geografy[index_long]
        long = geografy[index_lon]

        index_map += 1
        index_lon += 2
        index_long += 2
        index_map2 = 0

        if index_map2 != length:
            #
            folium.Marker(
                location=[lon, long],
                popup=poup,
                tooltip=toolip,
                icon=folium.Icon(icon=ikonka, prefix="fa", color=color),
            ).add_to(gdansk_map)
            index_map2 += 1
    print("Zapisz mapę")
    gdansk_map.save("gdanska_mapa_attainability.html")


Maps()
