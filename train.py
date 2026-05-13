from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("ultralytics/cfg/models/ext/coordatt-yolo26.yaml")

    results = model.train(
        # You should change this to the path where you downloaded the dataset
        data="C:\\Users\\Christian\\Downloads\\ultralytics\\ultralytics\\data\\skyfusion.v1i.yolov11\\data.yaml",
        epochs=10,
        imgsz=640,
        batch=2,
        project="runs/final_project",
        name="coordatt_exp2",
        plots=True,
        cache=False,
        amp=True,
    )