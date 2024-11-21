import os
import glob
import json
import urllib.request
from urllib.request import urlopen 
from PIL import Image

def ImageRetriever(imagepath: str, mediapath: str):
    """Goes to (https://services.swpc.noaa.gov) to retrieve images using the url path to that image and the path to where to download it to"""
    data_url = "https://services.swpc.noaa.gov/" + imagepath
    pathed_filename = os.path.join(mediapath, imagepath.rsplit('/', 1)[1])
    urllib.request.urlretrieve(data_url, pathed_filename)
    return pathed_filename

'''def ImageRetriever(imagepath: str, imagename: str, mediapath: str):
    """Goes to (https://services.swpc.noaa.gov) to retrieve images using the url path to that image and the path to where to download it to"""
    data_url = "https://services.swpc.noaa.gov/" + imagepath
    pathed_filename = os.path.join(mediapath, imagename)
    urllib.request.urlretrieve(data_url, pathed_filename)
    return pathed_filename'''

def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    frame_one = frames[0]
    pathed_filename = os.path.join("./_media", "Aurora_North.gif")
    frame_one.save(pathed_filename, format="gif", append_images=frames, save_all=True, duration=100, loop=0)
    
def jsonParser(myPath):
    jsonurl = "https://services.swpc.noaa.gov/products/animations/ovation_north_24h.json"
    jsons = urlopen(jsonurl)
    jsondata = json.loads(jsons.read())
    lenght=len(jsondata)
    for index in range(0, lenght):
        x = json.dumps(jsondata[index])
        #await ctx.send(data[0])
        y = json.loads(x)
        data_url = "https://services.swpc.noaa.gov/" + y["url"]
        image_name = "aurora_North_" + str(index) + ".jpg"
        pathed_filename = os.path.join(myPath, image_name)
        urllib.request.urlretrieve(data_url, pathed_filename)
    return(myPath)
'''
def jsonParser(jsonurl: str, mediapath: str):
    json = urlopen(jsonurl)
    jsondata = json.loads(json.read())
    jsonlength = len(jsondata)
    for index in range(500, jsonlength):
        x = json.dumps(jsondata[index])
        #await ctx.send(data[0])
        y = json.loads(x)
        data_url = "https://services.swpc.noaa.gov/" + y["url"]
        image_name = "aurora_North_" + str(index) + ".jpg"
        pathed_filename = os.path.join(mediapath, image_name)
        urllib.request.urlretrieve(data_url, pathed_filename)
    return()
'''
def VideoProducer(t_0, t_w, f_w): # NOT DONE
    """Example."""
    GIF_Name = "Aurora_North.gif"
    return GIF_Name
