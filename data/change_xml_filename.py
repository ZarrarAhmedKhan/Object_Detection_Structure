import os
import glob
import xml.etree.ElementTree as ET

xml_path = '/home/zeb/Desktop/vixion/Quantized_project/imges_and_annos/annotations'

counter = 0

for xml in glob.glob(xml_path + '/*'):
	# print(xml)
	filtered_xml = xml.split('/')[-1].split('_')[0]
	if filtered_xml == 'a':
		print("xml_name : ", xml)
		tree = ET.parse(xml)
		root = tree.getroot()
		filename = root.find('filename')
		filename_text = root.find('filename').text
		if filename_text.split('.')[0] != xml.split('/')[-1].split('.')[0]:
			filename.text = filename_text.split('.')[0].lower()  +'.jpg'
			print('file_name : ', filename.text)
			counter += 1
			tree.write(xml)
print('Total changed filename: ', counter)