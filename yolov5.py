import torch

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5x6")  # or yolov5n - yolov5x6, custom

# Images
img = "bus.jpg"  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.save('./bus_output.jpg')  # or .show(), .save(), .crop(), .pandas(), etc.