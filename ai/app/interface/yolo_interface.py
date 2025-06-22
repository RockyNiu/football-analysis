from pathlib import Path
from ultralytics import YOLO

ROOT_DIR = Path(__file__).parent.parent.parent
VIDEOS_DIR = ROOT_DIR / "videos"
MODEL = 'yolo12x.pt'

model = YOLO(MODEL)

video_path = VIDEOS_DIR / "08fd33_4.mp4"
print(f"Processing video: {video_path}")
print(f"Root directory: {ROOT_DIR}")
print(f"Videos directory: {VIDEOS_DIR}")

output_dir = ROOT_DIR / "results" / "yolo_detections"
output_dir.mkdir(parents=True, exist_ok=True)

results = model.predict(
    str(video_path), 
    save=True, 
    save_txt=True,
    project=str(output_dir.parent),
    name=output_dir.name 
)

print(f"\n🎯 Detection Results:")
print(f"Number of frames processed: {len(results)}")

for i, result in enumerate(results):
    print(f"\nFrame {i+1}:")
    if result.boxes is not None and len(result.boxes) > 0:
        for j, box in enumerate(result.boxes):
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            coords = box.xyxy[0].tolist()
            class_name = model.names[cls_id]  # Get class name
            print(f"  Detection {j+1}: {class_name} (ID: {cls_id}) - Confidence: {conf:.2f} - Box: {coords}")
    else:
        print(f"  No detections in this frame")

# Show where results are saved
print(f"\n📁 Results saved to:")
print(f"   - Custom output directory: {output_dir}")
print(f"   - Annotated video and text files in: {output_dir}")
print(f"   - Root directory: {ROOT_DIR}")

# List the actual output directory
if output_dir.exists():
    print(f"   - Results directory contents:")
    files = list(output_dir.glob("*"))
    for file in files:
        print(f"     • {file.name}")