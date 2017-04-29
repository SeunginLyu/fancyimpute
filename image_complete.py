from fancyimpute import NuclearNormMinimization
import numpy as np

from PIL import Image


def load_original_image_matrix(dir):
    return mat_original


def load_destroyed_image_matrix(dir):
    pic = Image.open(dir)
    pic = pic.convert("L")
    pix = np.array(pic)
    for x in np.nditer(pix, op_flags=['readwrite']):
        if x[...] < 20.0:
            x[...] = 0.0
    new_pic = Image.fromarray(pix, "L")
    new_pic.save("new_destroyed.png")

    pix = np.array(pic, float)
    for x in np.nditer(pix, op_flags=['readwrite']):
        if x[...] < 20.0:
            print(x[...])
            x[...] = np.nan
    return pix


def complete_image(mat_destroyed):
    mat_restored = NuclearNormMinimization().complete(mat_destroyed)
    return mat_restored


if __name__ == "__main__":
    original_img_dir = ""
    destroyed_img_dir = "destroyed.png"
    restored_img_dir = "restored.png"

    data = load_destroyed_image_matrix(destroyed_img_dir)
    complete_image(data)
