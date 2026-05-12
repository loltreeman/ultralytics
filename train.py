from ultralytics import YOLO

model = YOLO("ultralytics/cfg/models/ext/coordatt-yolo26.yaml")

results = model.train(
    data="ultralytics\\ultralytics\\data\\skyfusion.v1i.yolov11\\data.yaml", 
    epochs=50,
    imgsz=640,
    batch=16,
    project="runs/final_project",
    name="coordatt_exp",
    plots=True,
)