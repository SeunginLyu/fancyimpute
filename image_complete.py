from fancyimpute import NuclearNormMinimization
import numpy as np

from PIL import Image


def load_destroyed_image_matrix(dir):
    pic = Image.open(dir)
    pic = pic.convert("L")
    pix = np.array(pic, float)
    new_pic = Image.fromarray(pix.astype('uint8'))
    new_pic.save("new_destroyed.png")
    for x in np.nditer(pix, op_flags=['readwrite']):
        if x[...] < 10.0:
            x[...] = np.nan

    return pix


def complete_image(mat_destroyed):
    mat_restored = NuclearNormMinimization().complete(mat_destroyed)
    return mat_restored.astype('uint8')


if __name__ == "__main__":
    original_img_dir = ""
    destroyed_img_dir = "destroyed_2.png"
    restored_img_dir = "restored.png"

    data = load_destroyed_image_matrix(destroyed_img_dir)
    mat = complete_image(data)
    print(mat)
    completed_pic = Image.fromarray(mat)
    completed_pic.save(restored_img_dir)
