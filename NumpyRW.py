import numpy as np
 
import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt
 
face = scipy.misc.face(gray=True)
lx, ly = face.shape

crop_face = face[lx//6:-lx//6, ly//6:-ly//6]

flip_lr_face = np.fliplr(face)

rotate_face = ndimage.rotate(face, 60)
rotate_face_noreshape = ndimage.rotate(face, 60, reshape=False)

plt.figure(figsize=(12.5, 2.5))

plt.subplot(151)
plt.imshow(crop_face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(152)
plt.imshow(face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(153)
plt.imshow(flip_lr_face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(154)
plt.imshow(rotate_face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(155)
plt.imshow(rotate_face_noreshape, cmap=plt.cm.gray)
plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0,
                    right=1)

plt.show()