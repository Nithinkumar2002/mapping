import folium
import pandas
map=folium.Map(location=[0,-0], zoom_start=6 ,tiles="Stamen Terrain ")

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
ele=list(data["ELEV"])
name=list(data["NAME"])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'orange'
    else:
        return 'red'

fgv=folium.FeatureGroup(name="VOLCANOES")

for lt,ln,name,el in zip(lat,lon,name,ele):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6 , popup="name: "+name+"  elevation:" + str(el)+"m" ,fill_color=color_producer(el) , color='black' ,fill_opacity=0.7 ))#for circles as markers
fgp=folium.FeatureGroup(name="POPULATION")
fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000< x['properties']['POP2005'] <20000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map2.html")
