import os
from PIL import Image

dir_name = "./caesar_salad"
new_dir_name = "./resized_caesar_salad"
files = os.listdir(dir_name)
for file in files:
    photo = Image.open(os.path.join(dir_name, file))
    photo_resize = photo.resize((300,300))
    photo_resize.save(os.path.join(new_dir_name, file))