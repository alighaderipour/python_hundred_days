inty = 5
litsy = [6, 7]
stringy = "hi"
import folium

azores = folium.folium.Map(location=(38, -37), zoom_start=6)


"""
Objects: 5, [6, 7] , "hi", folium.folium.Map(location=(38, -37), zoom_start=6 , 38, -37, 6
--> ALL OBJECTS HAVE A TYPE
"""
print(type(inty))
print(type(litsy))
print(type(stringy))
print(type(folium.folium.Map(location=(38, -37), zoom_start=6)))
print(type(5))
print(type([6, 7]))
