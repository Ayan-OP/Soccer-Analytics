from ultralytics import YOLO

model = YOLO('yolov8m')

results = model.predict('C:/Users/ayaan/Downloads/football_analysis_OP/input_videos/08fd33_4.mp4', save = True)

print(results[0])
print('***********************************************************************************************************************')
for box in results[0].boxes:
    print(box)