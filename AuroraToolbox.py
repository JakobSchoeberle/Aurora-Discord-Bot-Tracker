import os
import glob
import json
import urllib.request
from urllib.request import urlopen 
from PIL import Image

def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    frame_one = frames[0]
    pathed_filename = os.path.join("./_media", "Aurora_North.gif")
    frame_one.save(pathed_filename, format="gif", append_images=frames, save_all=True, duration=100, loop=0)
    
def jsonParser():
    url = "https://services.swpc.noaa.gov/products/animations/ovation_north_24h.json"
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    lenght=len(data)
    for index in range(500, lenght):
        x = json.dumps(data[index])
        #await ctx.send(data[0])
        y = json.loads(x)
        data_url = "https://services.swpc.noaa.gov/" + y["url"]
        image_name = "aurora_North_" + str(index) + ".jpg"
        myPath = "./image"
        pathed_filename = os.path.join(myPath, image_name)
        urllib.request.urlretrieve(data_url, pathed_filename)
    return(myPath)

def VideoProducer(t_0, t_w, f_w): # NOT DONE
    """Example."""
    GIF_Name = "Aurora_North.gif"
    return GIF_Name
