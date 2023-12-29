# CUDA_VISIBLE_DEVICES=0 python train.py --img 640 --batch 8 --epochs 100 --data ./data/ua_detrac.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --cache
CUDA_VISIBLE_DEVICES=0 python train.py --img 640 --batch 8 --epochs 200 --data ./data/ua_detrac.yaml --cfg ./models/yolov5l.yaml --weights yolov5l.pt --cache