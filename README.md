# Object_Detection

Prerequisites files 

Go inside the Data folder:

### generate_labelmap_from_csv

*python3 generate_labelmap_from_csv.py -c path to csv*
> It will generate the label_map.pbtxt

> Label_map.pbtxt (placed inside the input folder)

### generate_tfrecord 
*python3 generate_tfrecord.py --csv_input=train.csv  --output_path=../inputs/train.record --label_map=inputs/label_map.pbtxt*
>It will generate .tfrecord file
>(placed inside the input folder)

## Additional work (not necessary)
*If xml_filenme specified inside xml file is not equal to xml filename*

*like this 

*<annotation>*
  
*<folder/>*
  
*<filename>mtn-dew-commrcial_mp4-1_jpg.rf.c0138c8a518b9a1ab0dc1400ac1a85aa.jpg</filename>*
  
> Use this script change_xml_filename.py

How to train the Object_detection tensorflow Api (tf1==1.15)?

1. Placed the using model config in the config folder and change different paths inside it.

2. Change path in the file "run_train" and run it.

# Copy Object Detection folder (Google Colab)

First, outside this "Object_Detection_Structure" folder, clone tensorflow/models

!git clone https://github.com/tensorflow/models.git

I am using tensorflow 1, so

!pip3 uninstall -y tensorflow==2.6.0

!pip3 install tensorflow-gpu==1.15

install some libraries

!sudo apt-get install protobuf-compiler python-pil python-lxml python-tk

!pip3 install --user Cython

!pip3 install --user contextlib2

!pip3 install --user jupyter

!pip3 install --user matplotlib

!sudo -H pip3 install numpy==1.17.4

## Go inside models/research directory

%cd '/models/research'

!protoc object_detection/protos/*.proto --python_out=.

!cp object_detection/packages/tf1/setup.py .

!export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

!python3 setup.py build

!python3 setup.py install

%cd slim

!python3 setup.py build

!python3 setup.py install

After that, copy "object_detection" folder inside "research" folder to "Object_Detection_Structure" folder

change the paths as mentioned at the top of the readme and run this file "run_train" to start training

!bash run_train

After training completed, you have to evaluate the training results.

## Evaluation of training

So, run this file "run_eval". 

on Google Colab, first you give permission to bash file , like this

!chmod +x run_eval

!sed -i -e 's/\r$//' run_eval

!./run_eval

see good our model is trained, some evaluation measure concepts https://www.jeremyjordan.me/evaluating-a-machine-learning-model/

## Export the Frozen_graph

Set the path in "run_export" bash file. pipeline_config should use "pipeline.config" which is present in "train" folder.

!chmod +x run_export

!sed -i -e 's/\r$//' run_export

!./run_export

Now you get the frozen_graph.pb thats it. you can now infernce your model on any image or video.

## Inference on Image 

set paths in the "Image_Detection_through_frozenfile" file.

!python3 Image_Detection_through_frozenfile.py -i input.jpg -o output.jpg

Similarly for the video...
