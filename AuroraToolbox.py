import glob
from PIL import Image

def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.jpg")]
    frame_one = frames[0]
    frame_one.save("Aurora_North.gif", format="GIF", append_images=frames,
               save_all=True, duration=100, loop=0)
    
def VideoProducer(t_0, t_w, f_w):
    """Example."""
    GIF_Name = "Aurora_North.gif"
    return GIF_Name
