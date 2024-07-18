# Allen Xu
# Basic update Python script for Fractracker map


# import modules
import pandas as pd
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection


## Variables- Naturally, replace all with the info of your account.

itemid = '4e29c8c2fa17435393c508dae0dbe68f'  #itemid of the feature layer being overwritten


# ArcGIS Online credentials:
# This is a throwaway ArcGIS Developer account I made for free. Feel free to try it on your own or use my account.

profile = 'https://allenxdev.maps.arcgis.com/'
user = 'allenxdev'
password = 'arcpytest123456'

csv_file = r"C:\Users\USER\Documents\school\FRACTRACKER internship\tidied_data.csv"
# "csv_file" is the path of the .csv file that is replacing
# the source data of the feature layer. MUST BE THE SAME FILE NAME AND TYPE AS SOURCE (tidied_data.csv)


# ArcGIS login

gis = GIS(profile, user, password)

#Overwriting

current_layer = gis.content.get(itemid)

current_layer_flc = FeatureLayerCollection.fromitem(current_layer)

current_layer_flc.manager.overwrite(csv_file)
