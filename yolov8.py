from ultralytics import YOLO
import cv2
# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from scratch
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Use the model
# results = model.train(data='coco128.yaml', epochs=3)  # train the model
# results = model.val()  # evaluate model performance on the validation set
results = model('/data/dataset/nama_area_images/head/2023-02-06/ffe39fe8-5597-4ed0-8272-8b2f32bb541b.jpg')  # predict on an image
# sa = model.predict(data='bus.jpg', save=True)
# res = results[0].boxes
# print(res)
# print(sa)
# success = model.export(format='onnx')  # export the model to ONNX format