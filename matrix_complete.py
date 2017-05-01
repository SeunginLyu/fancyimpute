from fancyimpute import NuclearNormMinimization
import numpy as np
from PIL import Image


def complete_image(mat_destroyed):
    mat_restored = NuclearNormMinimization().complete(mat_destroyed)
    return mat_restored.astype('uint8')


if __name__ == "__main__":

    data = np.array([[3, 4, 1, 1, 5, 2, 3, 4, np.nan, 5],
                     [1, 5, 4, 2, 1, 3, 1, np.nan, 2, 1],
                     [1, 2, 4, 3, 2, np.nan, 2, 4, 4, 5],
                     [5, 4, 5, 5, 2, 2, 4, np.nan, 1, 3],
                     [1, np.nan, 2, 4, 2, np.nan, 1, 3, 5, 2],
                     [3, 4, np.nan, 1, np.nan, 1, 5, 4, 2, 3],
                     [1, 3, 5, np.nan, 3, np.nan, 2, 4, 1, 5],
                     [1, 2, np.nan, 4, np.nan, 3, 2, 4, 4, 1],
                     [2, 5, 1, 2, 4, np.nan, 2, 1, np.nan, np.nan],
                     [4, 1, 3, 2, 5, 3, np.nan, 2, 3, 1]])
    mat = complete_image(data)
    print(mat)
