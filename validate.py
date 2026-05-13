from ultralytics import YOLO

if __name__ == '__main__':
    # Change this to the path where you saved the best.pt file after training
    model = YOLO("C:\\Users\\Christian\\Downloads\\ultralytics\\runs\\detect\\runs\\final_project\\coordatt_exp2\\weights\\best.pt")
    metrics = model.val(
        # You should change this to the path where you downloaded the dataset
        data="C:\\Users\\Christian\\Downloads\\ultralytics\\ultralytics\\data\\skyfusion.v1i.yolov11\\data.yaml"
    )

    print("mAP50:", metrics.box.map50)
    print("mAP50-95", metrics.box.map)
    print("Precision:", metrics.box.mp)
    print("Recall:", metrics.box.mr)