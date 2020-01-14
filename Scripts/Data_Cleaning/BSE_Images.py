# This script takes the original BSE image and splits it into smaller chunks for analysis in the neural network.
# Original Images *around* 5645x5596x1 px

# IMPORTS
import numpy as np
import math
from PIL import Image

# CONSTANTS
DATA_PATH = "../../Original_Data/BSE/"
PX_SQUARE_IMAGE_SIZE = 1000
SAVE_TEST_PATH = "../../Junk_Folder/"
SAVE_TRAIN_PATH = "../../Train/"


# SPLITTER
def bse_image_split(file_name, save_folder_path, px_square_size):
    # import image and convert to a numpy array
    image = Image.open(DATA_PATH + file_name)
    image = np.array(image, dtype=np.uint8)

    # create new image for split to go into
    split_image_arr = np.zeros([px_square_size, px_square_size], dtype=np.uint8)

    # find the number of split images that are possible
    images_vertical = math.floor(len(image) / px_square_size)
    images_horizontal = math.floor(len(image[0])/px_square_size)

    # split the original image and saves to file path
    for image_number_vertical in range(1, images_vertical+1):
        for image_number_horizontal in range(1, images_horizontal+1):
            for row in range(px_square_size * (image_number_horizontal - 1), px_square_size * image_number_horizontal):
                for column in range(px_square_size * (image_number_vertical - 1), px_square_size * image_number_vertical):
                    split_image_arr[row - (px_square_size * (image_number_horizontal - 1))][column - (px_square_size * (image_number_vertical - 1))] = image[row][column][0]
            split_image = Image.fromarray(split_image_arr)
            split_image.save(save_folder_path +
                             'BSE_' +
                             'testing_vert_' + str(image_number_vertical) +
                             '_hori_' + str(image_number_horizontal) +
                             '_size_' + str(px_square_size) + 'x' + str(px_square_size) +
                             '_.png')

# MAIN
if __name__ == "__main__":
    bse_image_split("G-E8_1_BSE_XZ_middle_highres.png", SAVE_TEST_PATH, PX_SQUARE_IMAGE_SIZE)

    print("done")
