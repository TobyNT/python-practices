import folium
import pandas

map = folium.Map(location=[10.7859228, 106.7031945], zoom_start=6, tiles='OpenStreetMap')
fg = folium.FeatureGroup(name="My Map")

volcanoes = pandas.read_csv("volcanoes.txt")

latList = list(volcanoes["LAT"])
lonList = list(volcanoes["LON"])
elevList = list(volcanoes["ELEV"])

def colorize_evelvation(elev):
  if elev < 1000:
    return 'green'
  elif elev < 3000:
    return 'orange'
  else:
    return 'red'

for lat,lon, elev in zip(latList, lonList, elevList):
  fg.add_child(folium.Marker(location=[lat, lon], popup=str(elev) + " m", icon=folium.Icon(color=colorize_evelvation(elev))))

map.add_child(fg)

map.save("Map1.html")