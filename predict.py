# -*- coding: utf-8 -*-
"""predict.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wLGQrlxOTkauCrG_sU5pPe2KfBWz2K8q
"""

pip install ultralytics

from google.colab import drive
drive.mount('/content/drive')

cd /content/drive/MyDrive/yolov8

from ultralytics import YOLO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

model = YOLO("/content/drive/MyDrive/yolov8/runs/detect/train2/weights/best.pt")
results = model("/content/drive/MyDrive/yolov8/dung.png")

# Duyệt qua các kết quả dự đoán
for r in results:
    # Vẽ kết quả dự đoán lên hình ảnh
    im_array = r.plot()
    im_array_rgb = im_array[..., ::-1]  # Đảo ngược kênh màu từ BGR sang RGB
    # Hiển thị hình ảnh
    plt.imshow(im_array_rgb)
    plt.axis('off')
    plt.show()

model = YOLO("/content/drive/MyDrive/yolov8/runs/detect/train2/weights/best.pt")
results = model("/content/drive/MyDrive/yolov8/no_right.webp")

# Duyệt qua các kết quả dự đoán
for r in results:
    # Vẽ kết quả dự đoán lên hình ảnh
    im_array = r.plot()
    im_array_rgb = im_array[..., ::-1]  # Đảo ngược kênh màu từ BGR sang RGB
    # Hiển thị hình ảnh
    plt.imshow(im_array_rgb)
    plt.axis('off')
    plt.show()
    # Lưu hình ảnh với kết quả dự đoán
    #im = Image.fromarray(im_array_rgb)
    #im.save("/content/drive/MyDrive/yolov8/kq_dung.png")

model = YOLO("/content/drive/MyDrive/yolov8/runs/detect/train2/weights/best.pt")
results = model("/content/DA2.png")

# Duyệt qua các kết quả dự đoán
for r in results:
    # Vẽ kết quả dự đoán lên hình ảnh
    im_array = r.plot()
    im_array_rgb = im_array[..., ::-1]  # Đảo ngược kênh màu từ BGR sang RGB
    # Hiển thị hình ảnh
    plt.imshow(im_array_rgb)
    plt.axis('off')
    plt.show()
    # Lưu hình ảnh với kết quả dự đoán
    #im = Image.fromarray(im_array_rgb)
    #im.save("/content/drive/MyDrive/yolov8/kq_dung.png")

