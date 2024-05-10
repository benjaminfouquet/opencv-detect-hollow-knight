### Object Detection on live feed

#### Dataset generation
`stream-capturer.py` captures frame by frame live stream from my own twitch account `twikilix` if its live using Streamlink, and stores them in the stream_captured folder.

- Start OBS and launch livestream on twitch on `twikilix` account
- `python stream-capturer.py` in terminal
- captures 1/4 frame, stores them in ``stream_captured/twikilix_{datetime}``

#### Labelling
Done on `makesense.ai`. Problem: ORDER OF LABELS IS IMPORTANT. Adapted from https://www.youtube.com/watch?v=RSXgyDf2ALo [1].

- Labels should be in the same order for all pictures.

#### Model training YOLO
#### OpenCV Detector
Follow guide in window_capture, also adapted from [1].

#### Live Object Detection
TODO.

### Other folders
Other folders `twitch_recorder` and `window_capture` are legacy code from research on the topic.