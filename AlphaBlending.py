from PIL import Image

src1 = np.array(Image.open('lena.jpg'))
src2 = np.array(Image.open('rocket.jpg').resize(src1.shape[1::-1], Image.BILINEAR))

print(src1.dtype)
# uint8

dst = src1 * 0.5 + src2 * 0.5

print(dst.dtype)
# float64

Image.fromarray(dst.astype(np.uint8)).save('image_alpha_blend.jpg')
