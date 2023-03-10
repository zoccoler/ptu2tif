from pathlib import Path
import numpy as np
from skimage import io
from inputs.read_ptu_data_2D import read_ptu_data_2D

# Provide local path to folder containing .ptu files
folder_path = input('Paste the path to a folder with .ptu files and hit Enter:\n')
# folder_path = r""

folder_path = Path(folder_path)

# Output tif files are saved in a folder called 'output_as_tif'
output_path = folder_path.parent / 'output_as_tif'
output_path.mkdir(exist_ok = True)

for path in folder_path.iterdir():
    if path.suffix == '.ptu':
        print(path.stem)
        image = read_ptu_data_2D(path)
        file_name = path.stem + '.tif'
        io.imsave(output_path / file_name, image)

        