import urllib.request
import json
# import dml


"""
#parcel geojson data
url = "http://bostonopendata-boston.opendata.arcgis.com/datasets/b7739e6673104c048f5e2f28bb9b2281_0.geojson"

response = urllib.request.urlopen(url).read()

l = json.loads(response.decode('utf-8'))

print(l.keys())

#property assessment data
url1 = "https://data.boston.gov/datastore/odata3.0/fd351943-c2c6-4630-992d-3f895360febd?format=json"
response = urllib.request.urlopen(url1).read()

"""

#Census tract data
urlDataMech = "http://datamechanics.io/data/gasparde_ljmcgann_tlux/boston_census_track.json"
geojason = urllib.request.urlopen(urlDataMech).read()
data = json.loads(geojason.decode('utf-8'))

print(data)

# property assessment data
# url1 = "https://data.boston.gov/datastore/odata3.0/fd351943-c2c6-4630-992d-3f895360febd?$format=json"
# response = urllib.request.urlopen(url1).read()
# g = json.loads(response)
# g = g['value']





