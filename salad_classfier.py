import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from pathlib import Path
import glob
import os

np.set_printoptions(suppress=True)

model = tensorflow.keras.models.load_model('/tmp/converted_savedmodel/model.savedmodel/')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

from_dir = Path("./mixed_salad")
caesar_to_dir = Path("classfied_caesar_salad")
caprese_to_dir = Path("classfied_caprese_salad")

for image_path in from_dir.glob("*.jpg"):
    im = Image.open(image_path)
    size = (224, 224)
    image = ImageOps.fit(im, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    caesar = prediction[0, 0]
    capreze = prediction[0, 1]

    ftitle, fext = os.path.splitext(image_path)

    if caesar > capreze:
        print("シーザー")
        caesar_save_path = caesar_to_dir / image_path.name
        im.save(caesar_save_path)
    else:
        print("カプレーゼ")
        caprese_save_path = caprese_to_dir / image_path.name
        im.save(caprese_save_path)

caesar_num = sum(os.path.isfile(os.path.join(caesar_to_dir, name)) for name in os.listdir(caesar_to_dir))
caprese_num = sum(os.path.isfile(os.path.join(caprese_to_dir, name)) for name in os.listdir(caprese_to_dir))
print("number of classfied files[caesar] : " + str(caesar_num))
print("number of classfied files[caprese] : " + str(caprese_num))