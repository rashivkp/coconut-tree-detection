# Setup Script for aws ami `ami-06bfad7c` in eu-east-1. it has ubuntu 16.04, cuda 9.1, tensorflow
# I had tried g2, t2 type instances

git clone https://github.com/tensorflow/models.git
cd models/research
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
echo "export PYTHONPATH=\"\$PYTHONPATH:`pwd`:`pwd`/slim\"" >>~/.bashrc

git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
cp -r pycocotools ../../
cd ../../

wget https://github.com/google/protobuf/releases/download/v3.5.1/protoc-3.5.1-linux-x86_64.zip
unzip -d protobuf protoc-3.5.1-linux-x86_64.zip

export PATH="$PATH:`pwd`/protobuf/bin"
echo "export PATH=\"\$PATH:`pwd`/protobuf/bin\"" >>~/.bashrc

protoc object_detection/protos/*.proto --python_out=.

pip install pillow
pip install lxml
pip install jupyter
pip install matplotlib

# for downloading model to use in pipeline config as fine_tune_checkpoint
wget http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet50_coco_2018_01_28.tar.gz
tar -xvf faster_rcnn_resnet50_coco_2018_01_28.tar.gz -C ./
