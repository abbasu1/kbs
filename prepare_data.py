import os
import shutil
import random

# Paths
BASE_DIR = "/home/ackerman/Downloads/semester 8/KBS/App/kbs"
DATASET_SOURCE = os.path.join(BASE_DIR, "datasets/COVID-19_Radiography_Dataset")
TARGET_DIR = os.path.join(BASE_DIR, "dataset")

CLASSES = ["Normal", "Pneumonia", "Lung_Opacity"]
SPLIT_RATIO = 0.8

def prepare_data():
    if os.path.exists(TARGET_DIR):
        print(f"Cleaning up existing target directory: {TARGET_DIR}")
        shutil.rmtree(TARGET_DIR)

    for split in ["train", "test"]:
        for cls in CLASSES:
            os.makedirs(os.path.join(TARGET_DIR, split, cls), exist_ok=True)

    for cls in CLASSES:
        src_path = os.path.join(DATASET_SOURCE, cls)
        if not os.path.exists(src_path):
            print(f"Warning: Source path {src_path} not found.")
            continue

        images = [f for f in os.listdir(src_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        random.shuffle(images)

        split_idx = int(len(images) * SPLIT_RATIO)
        train_images = images[:split_idx]
        test_images = images[split_idx:]

        print(f"Processing class {cls}: {len(train_images)} train, {len(test_images)} test")

        for img in train_images:
            shutil.copy(os.path.join(src_path, img), os.path.join(TARGET_DIR, "train", cls, img))

        for img in test_images:
            shutil.copy(os.path.join(src_path, img), os.path.join(TARGET_DIR, "test", cls, img))

    print("Data preparation complete.")

if __name__ == "__main__":
    prepare_data()
