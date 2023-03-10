import numpy as np
from .readPTU_FLIM import PTUreader
def read_ptu_data_2D(path):
    ptu_file = PTUreader(path, print_header_data = False)
    image, _ = ptu_file.get_flim_data_stack()
    # move x,y to the end
    image = np.moveaxis(image, [0, 1], [-2, -1])
    return image