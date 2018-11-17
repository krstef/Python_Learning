from geopy.geocoders import ArcGIS
import pandas
#create arcgis object
nom = ArcGIS()
#call geocode method and pass string address as an argument
n = nom.geocode("Krapinska ulica 45, 10000 Zagreb", 1)
#apply longitude and alititude methods on n object 
print("Krapinska 45 is on following address: ", n.longitude, n.latitude)

csv_data = pandas.read_csv("testexample.csv")
csv_data["Address"] = csv_data["Address"] + ", " + csv_data["City"] + ", " + \
    csv_data["State"] + ", " + csv_data["Country"]

""" Create new column named 'Coridantes' and store there data from 'Address'    \
    column on which has been applied nom.geocode method                         \
    geocode returns geo informations about address """
csv_data ["Cordinates"] = csv_data["Address"].apply(nom.geocode)

csv_data["Latitude"] = csv_data["Cordinates"].apply(lambda x: x.latitude if \
    x !=None else None)

csv_data["Longitude"] = csv_data["Cordinates"].apply(lambda x: x.longitude if \
    x !=None else None)

print(type(csv_data["Cordinates"]))
