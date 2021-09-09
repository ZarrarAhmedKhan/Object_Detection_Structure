# Object_Detection

Prerequisites files 

1. Label_map.pbtxt (placed inside the input folder)

2. tf.record (placed inside the input folder)

How to train the Object_detection tensorflow Api (tf1==1.15)?

1. Placed the using model config in the config folder and change different paths inside it.

2. Change path in the file "run_train" and run it.

## object detection folder (Google Colab)

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

### go inside models/research directory

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

So, run this file "run_eval". 

on Google Colab, first you give permission to bash file , like this

!chmod +x run_eval

!sed -i -e 's/\r$//' run_eval

!./run_eval
