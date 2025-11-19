from ultralytics import YOLO

model = YOLO('models/best.pt')

results = model.predict('input_videos/real_madrid_clip.mp4', save=True)
print(results[0])
print('====================================')

for box in results[0].boxes:
    print(box)

