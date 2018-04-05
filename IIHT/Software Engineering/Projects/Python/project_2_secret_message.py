# /usr/bin/env python3.5

import re 
import os
"""
Encapsulated version of the Project:

Remove all digits from each photo filename in the folder.

"""


# 0 Approach: ( Mad Approach don't do this in production code :))


# dir_ = '/home/choupi/Downloads/prank/prank/'
# import re 
# import os
# [os.rename(dir_ + fname, dir_ + re.sub(r'\d', '', fname)) for fname in os.listdir(dir_)] 



# Second Approach secret message project 2


def secret_message(directory_name):

	"""
	This function will remove all digits on a file names in a given directory.
	"""
	filenames = os.listdir(directory_name) # filenames in a directory => llist

	for filename in filenames:

		new_filename = re.sub(r'\d', '', filename) # replacing all digits in filename => str
		os.rename(directory_name + filename, directory_name + new_filename) # renaming each filename => NoneType



# First Approach:

import os # Importing os module.

def secret_message(directory_path):

	
	"""
	
	This function will remove all digits on a file name in a given directory.

	"""
	
	filenames_of_photos = os.listdir(directory_path) # filenames_of_photos in a directory => list object(container, iterable)

	number_of_photos_files = len(filenames_of_photos) # number of photo file in the folder => int object(integers)

	new_filenames_of_photos = [] # Initializing new photos filenames container => list object()

	first_counter = 0 # Initializing a counter at 0 => int object



	while first_counter < number_of_photos_files:

		a_photo_filename = filenames_of_photos[first_counter] # photo_file_name => str object(container, iterable)



#====================== Start of character checking process ==========================

		number_of_characters = len(a_photo_filename) # number of characters in each photo filename => str object

		renamed_photo_filename = '' # Initializing an empty new filename

		second_counter = 0 # initializing a counter at 0 => int object



		while second_counter < number_of_characters:

			character = a_photo_filename[second_counter] # a character from a photo filename => str object

			# if not character.isnumeric(): # Charater checking

			list_of_digits = ['0','1','2','3','4','5','6','7','8','9']

			if character not in list_of_digits:

				renamed_photo_filename += character # concatenate the character to the renamed_photo_filename 

			second_counter += 1 # incrementing the second counter by 1

#====================== End of character checking process ==========================



		new_filenames_of_photos.append(renamed_photo_filename) # Adding new filename to new photos filenames container
		
		first_counter += 1 # incrementating the first counter by 1



#====================== Start of file renaming process ==========================

	third_counter = 0 # Initializing a third counter

	while third_counter < number_of_photos_files:

		os.rename(directory_path + filenames_of_photos[third_counter], directory_path + new_filenames_of_photos[third_counter]) # renaming each file name

		third_counter += 1 # Increamenting third counter by 1

#====================== End of file renaming process ==========================








dir = '/home/choupi/Downloads/prank/prank/'

print(secret_message(dir))

# directory = os.listdir(dir)
# print(directory)
# new_filename = re.sub(r'\d', '', directory[0]) # directory[0] 74tel aviv.jpg
# print(os.rename(dir + directory[0], dir + re.sub(r'\d', '', directory[0])))
# secret_message(dir)
