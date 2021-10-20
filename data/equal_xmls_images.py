import os

xml_folder = '/home/zeb/Desktop/vixion/Quantized_project/imges_and_annos/annotations'
images_path = '/home/zeb/Desktop/vixion/Quantized_project/imges_and_annos/images'

xml_folder  = os.listdir(xml_folder)
output = [xml.split('.')[0] for xml in xml_folder]
# print(output)
counter = 0
for img in os.listdir(images_path):
	# print(xml)
	file_name = img.split('.')[0]
	# print('file_name: ', file_name)
	if file_name not in output:
		counter += 1
		print('image not in xml_folder', file_name)
		file_name = file_name + '.jpg'
		if os.path.exists(images_path + '/' + file_name):
			print("remove: ", counter)
			os.remove(images_path+ '/' +file_name)
		# print('not in')
print("number of images not in xml_folder: ", counter)