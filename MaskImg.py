import numpy as np
from PIL import Image

src = np.array(Image.open('lena.jpg'))
mask = np.array(Image.open('horse_r.png').resize(src.shape[1::-1], Image.BILINEAR))

print(mask.dtype, mask.min(), mask.max())


mask = mask / 255

print(mask.dtype, mask.min(), mask.max())

dst = src * mask

Image.fromarray(dst.astype(np.uint8)).save('image_mask.jpg')