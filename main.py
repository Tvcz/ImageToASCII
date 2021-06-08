import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
from tqdm import tqdm
from math import floor
from skimage import filters
from skimage.io import imread
from skimage.transform import resize


# How to add new characters:
#  1. Make 16x16 image of character in rgb format, black and white ([255, 255, 255] and [0, 0, 0]).
#  2. Add to character_images folder.
#  3. Name image [character].png OR add to special_characters dictionary.
#  4. You should be ready to go. Double check that it appears in differences dictionary and has some normal value (not 0 or 256).
#
#  Side note: You can limit the characters used to a certain selection by doing the reverse.

class ImageToASCII:

    def __init__(self):
        running_directory = os.path.dirname(__file__)
        self.character_directory = os.path.join(running_directory, "character_images")

    # input_path is path to image
    # width is horizontal resolution (in pixels) the image should be scaled to (0 for original size)
    # show_image_progress determines where matplotlib is used to show preparation of image (for debugging)
    def ascify(self, input_path, width=0, show_image_progress=False):
        image = imread(input_path)

        print(f"\n--Ascifying \"{input_path}\"--")

        # resizes input image to a reasonable size for the program to work with 
        if width != 0:
            print("Scaling image to appropriate size...")
            if image.shape[1] > width:
                image = resize(image, (round(image.shape[0] * (width / image.shape[1])), width), anti_aliasing=True)

        if show_image_progress:
            plt.imshow(image)
            plt.show()

        # COLORMAP!!!!!!
        print("Applying grayscale colormap...")
        color_map = plt.get_cmap("gray")
        image = color_map(image)
        image = (image[:, :, 0, :3] * 255).astype(np.uint8)

        # runs edge detect
        print("Running sobel edge detect...")
        image = filters.sobel(image)
        
        # stretch because characters are skinny
        print("Stretching image...")
        image = resize(image, (image.shape[0], image.shape[1] * 2), anti_aliasing=True)
        
        # fix image because previous two function calls will make it float in range (0, 1)
        image = (image[:, :, :3] * 255).astype(np.uint8)

        if show_image_progress:
            plt.imshow(image)
            plt.show()

        # posterizes image
        print("Reducing input to black/white...")
        black_limit = 30
        image = image[:,:,:3]
        for row in range(len(image)):
            for column in range(len(image[row])):
                if image[row, column][0] > black_limit and image[row, column][1] > black_limit and image[row, column][2] > black_limit:
                    image[row, column] = [255, 255, 255]
                else:
                    image[row, column] = [0, 0, 0]

        if show_image_progress:
            plt.imshow(image)
            plt.show()

        # loads character images into memory
        print("Loading characters...")
        character_arrays = {}
        for filename in os.listdir(self.character_directory):
            target_file_path = os.path.join(self.character_directory, filename)
            character_array = imread(target_file_path)
            character_arrays[Path(target_file_path).stem] = character_array

        character_image = []
        # iterates through 16x16 chunks of image and finds the closest character to match
        print("Beginning conversion of image...\n")
        # total is probably messsed up but its close enough 
        with tqdm(total = floor(len(image) / 16) * floor(len(image[0]) / 16)) as progress_bar:
            for row in range(16, len(image), 16):
                character_row = []
                for column in range(16, len(image[row]), 16):
                    character_row.append(self.closest_character(image[row-16:row, column-16:column], character_arrays))
                    progress_bar.update(1)
                character_image.append(character_row)

        return character_image


    def closest_character(self, input_array, character_arrays):
        black_2d_array = np.full((16, 16, 3), 0)

        differences = {"black": self.difference(input_array, black_2d_array)}
        special_characters = {"black": " ", "asterisk": "*", "forward_slash": "/", "back_slash": "\\", "colon": ":", "comma": ",", "period": ".", "question_mark": "?", "right_arrow": ">", "left_arrow": "<", "double_quote": "\"", "single_quote": "'", "tilda": "~", "a_upper": "A", "b_upper": "B", "c_upper": "C", "d_upper": "D", "e_upper": "E", "f_upper": "F", "g_upper": "G", "h_upper": "H", "i_upper": "I", "j_upper": "J", "k_upper": "K", "l_upper": "L", "m_upper": "M", "n_upper": "N", "o_upper": "O", "p_upper": "P", "q_upper": "Q", "r_upper": "R", "s_upper": "S", "t_upper": "T", "u_upper": "U", "v_upper": "V", "w_upper": "W", "x_upper": "X", "y_upper": "Y", "z_upper": "Z" }

        for character_key in character_arrays:
            character_array = character_arrays[character_key]
            differences[character_key] = self.compare(input_array, character_array)

        character = min(differences, key=differences.get)

        if character in special_characters:
            character = special_characters[character]

        return character


    def compare(self, input_array, character_array):
        padded_input_array = np.pad(input_array, 1, mode="constant", constant_values=0)[:, :, 1:4]

        differences = []

        for r_displacement in range(3):
            for c_displacement in range (3):
                r_low = r_displacement
                r_high = len(padded_input_array)-(2-r_displacement)
                c_low = c_displacement
                c_high = len(padded_input_array[0])-(2-c_displacement)

                differences.append(self.difference(padded_input_array[r_low:r_high, c_low:c_high], character_array))

        return min(differences)


    def difference(self, input_array, character_array):
        return np.count_nonzero(input_array != character_array)

image_path = "door.jpg"

ascii = ImageToASCII()
image = ascii.ascify(image_path)

output_file = f"{Path(image_path).stem}.txt"

with open(output_file, "w+") as file:
    for row in image:
        file.write("".join(row) + "\n")
        print("".join(row))

print(f"\nOutput saved to \"{output_file}\"")