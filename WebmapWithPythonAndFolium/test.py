import folium

location = [80, -10]
map = folium.Map(location, zoom_start=5)
fg = folium.FeatureGroup(name="Base Layer")
# add features to the feature group
fg.add_child(folium.CircleMarker(location,popup="Your location",radius=6, fill_color='red', color='red'))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))
# add features (feature group) to the map object
map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())
# translation into HTML
map.save("Map1.html")
