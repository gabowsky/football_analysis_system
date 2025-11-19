This project focuses on analyzing football (soccer) match footage using computer vision and machine learning techniques.
The goal is to detect, track, and extract meaningful insights from ball movement and player interactions.

# Project Overview
The system processes video frames from a camera feed and performs the following main tasks:
  - Object detection (ball, players, goals, etc.) using a YOLO model
  - Object tracking across frames
  - Ball trajectory analysis and event detection
  - Visualization of bounding boxes, tracks, and statistics

# Technologies Used
  - Python 3
  - OpenCV for video processing
  - Ultralytics YOLO for object detection
  - Supervision (ByteTrack) for object tracking
  - NumPy / Pandas for data manipulation

# Future Improvements
  - Player team classification
  - Heatmap generation
  - Real-time tracking on Raspberry Pi
  - Shot detection using speed estimation
