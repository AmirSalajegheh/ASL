# American Sign Language (ASL) Recognition



This project detects and recognizes American Sign Language letters in real-time using a YOLO-based object detection model. It can recognize hand gestures from a live webcam feed.



## Features



* Real-time ASL recognition via webcam.

* YOLOv8-based object detection model.

* Trainable on custom datasets using Roboflow integration.



## Installation



Clone the repository:



```bash

git clone https://github.com/AmirSalajegheh/ASL.git

cd ASL

```



Install required Python packages:



```bash

pip install -r requirements.txt

```



## Usage



### Webcam Detection



Run the `main.py` script to start real-time recognition from your webcam:



```bash

python main.py

```



Detected letters will be shown on the screen and saved in `asl\_detection.mp4`.



### Training the Model



You can train a YOLOv8 model on the ASL dataset using the provided Jupyter notebook `training.ipynb`.

You can refer to `test.gif` as an example input/output visualization.



## Author



Developed by \*\*Amir Salajegheh\*\* 🚀

