from flask import Flask, Response
import cv2
from roboflow import Roboflow
import supervision as sv

rf = Roboflow(api_key="YOUR_API_KEY_HERE")
project = rf.workspace().project("chicken-counting-cfwaq")
model = project.version(1).model

app = Flask(__name__)
cap = cv2.VideoCapture(0)

annotator = sv.BoxAnnotator()
frame_count = 0
skip_frames = 5  
detections = None
annotated_frame = None
def generate_frames():
    global frame_count, detections, annotated_frame

    while True:
        success, frame = cap.read()
        if not success:
            break

        if frame_count % skip_frames == 0:
            result = model.predict(frame, hosted=False)
            detections = sv.Detections.from_inference(result)
            annotated_frame = annotator.annotate(scene=frame, detections=detections)
        else:
            if detections is not None:
                annotated_frame = annotator.annotate(scene=frame, detections=detections)
            else:
                annotated_frame = frame

        ret, buffer = cv2.imencode('.jpg', annotated_frame, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        frame_count += 1

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return '<h2>Live Optimized Detection</h2><img src="/video" width="720">'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #chicken-detorctor-3000
