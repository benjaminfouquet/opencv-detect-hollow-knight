from streamlink import Streamlink
import cv2
import os
import datetime


def stream_to_url(url, quality="best"):
    """Get URL, and return streamlink URL"""
    session = Streamlink()
    streams = session.streams(url)

    if streams:
        return streams[quality].to_url()
    else:
        raise ValueError("Could not locate your stream.")


user = "twikilix"
url = (
    "https://www.twitch.tv/" + user
)  # Login to twitch TV before starting (the URL is for a random live stream).
quality = "best"

stream_url = stream_to_url(url, quality)
cap = cv2.VideoCapture(stream_url)

frame_count = 0
export_count = 0
output_folder = os.path.join(
    "stream_captured",
    user + "_" + datetime.datetime.now().strftime("%m_%d_%H_%M_%S"),
)
# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

while True:
    success, frame = cap.read()

    if not success:
        break

    cv2.imshow("frame", frame)

    if frame_count % 4 == 0:
        # Save the frame as an image
        image_path = os.path.join(output_folder, f"frame_{export_count}.jpg")
        export_count += 1
        cv2.imwrite(image_path, frame)

    # Increment the frame count
    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
