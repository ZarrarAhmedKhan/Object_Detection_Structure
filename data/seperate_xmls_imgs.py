import glob
import os
import shutil

path_to_data = '/home/zeb/Desktop/new_projects/mountain_dew/Object_Detection/data/Mountain Dew Commercial data/test'

img_format = ['jpg', 'JPG', 'jpeg']

if not os.path.exists(path_to_data + '/annotations/'):
	os.mkdir(path_to_data+'/annotations/')
xml_folder_path = path_to_data + '/annotations/'

if not os.path.exists(path_to_data + '/images/'):
	os.mkdir(path_to_data + '/images/')
images_folder_path = path_to_data + '/images/'

def main(remove_previous_xmls = False, remove_previous_images = False):	
	img_counter = 0
	xml_counter = 0
	for file in glob.glob(path_to_data+ '/*'):

		if '.xml' in file:
			xml_counter += 1
			shutil.copy2(file, xml_folder_path)
			# print(file)
			if remove_previous_xmls:
				os.remove(file)
		if file.split('.')[-1] in img_format:
			img_counter += 1
			shutil.copy2(file, images_folder_path)
			if remove_previous_images:
				os.remove(file)
			# print(file)
	print("total_images: ",img_counter)
	print("total annotations: ", xml_counter)
	print('Done')

if __name__ == '__main__':
	remove_previous_xmls = True
	remove_previous_images = True
	main(remove_previous_xmls, remove_previous_images)

