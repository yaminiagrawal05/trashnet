import os
from datetime import datetime

for image_file_name in os.listdir(path_to_image):
    if image_file_name.endswith(".jpg"):
        now = datetime.now().strftime('%Y%m%d-%H%M%S-%f')

        im = Image.open(path_to_image+image_file_name)
        new_width  = 32
        new_height = 32
        im = im.resize((new_width, new_height), Image.ANTIALIAS)
        im.save(path_to_image + now + '.jpg')
