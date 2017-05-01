from fancyimpute import NuclearNormMinimization
import numpy as np

from PIL import Image


def complete_image(mat_destroyed):
    mat_restored = NuclearNormMinimization().complete(mat_destroyed)
    return mat_restored.astype('uint8')


if __name__ == "__main__":
    data = np.array([[3, 4, np.nan, 1, 5],
                     [np.nan, 5, 4, np.nan, 1],
                     [1, 2, np.nan, 3, 2],
                     [np.nan, np.nan, 5, 5, 2],
                     [1, 1, 2, 3, 2]])
    mat = complete_image(data)
    print(mat)
