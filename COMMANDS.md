# Commands Used

We used AWS spot instance for training. And we used a [setup script](setup.sh) install the requirements.

### Upload Setup script and Run it in server
`scp -i ~/.ssh/private-key.pem coconut_model/setup.sh ubuntu@server`

### parallely upload our dataset
`scp -i ~/.ssh/private-key.pem coconut_model.zip ubuntu@server`

### Run this in server
`ssh -i ~/.ssh/private-key.pem ubuntu@server`
`cd coconut_model/`

### tmux, check ram, memory usage
- `tmux`
- `nvidia-smi`
- `df -h`


### testing installation
`python tools/model_builder_test.py`

### Creating Records
`python tools/create_pascal_tf_record.py --label_map_path=label_map.pbtxt --data_dir=VOCdevkit --year=VOC2012 --set=train --output_path=pascal_train.record`

`python tools/create_pascal_tf_record.py --label_map_path=label_map.pbtxt --data_dir=VOCdevkit --year=VOC2012 --set=val --output_path=pascal_val.record`

### pipeline configuration
```
PWD=$(echo "`pwd`" | sed 's/\//\\\//g')
sed -i "s/PATH_TO_BE_CONFIGURED/$PWD/g" faster_rcnn_resnet50_coco.config
sed -i 's/MODEL_DOWNLOADED/faster_rcnn_resnet50_coco_2018_01_28/g' faster_rcnn_resnet50_coco.config
```

### Training
`python tools/train.py --logtostderr --pipeline_config_path=faster_rcnn_resnet50_coco.config --train_dir=train_dir`

### Evaluation
`python tools/eval.py --logtostderr --pipeline_config_path=faster_rcnn_resnet50_coco.config --checkpoint_dir=train_dir --eval_dir=val_dir`

### exporting model for inference
`python tools/export_inference_graph.py --input_type image_tensor --pipeline_config_path=faster_rcnn_resnet50_coco.config --trained_checkpoint_prefix=train_dir/model.ckpt-ZZZ --output_directory output_inference_graph.pb`
