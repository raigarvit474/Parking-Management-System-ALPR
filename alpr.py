import os
import cv2
from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
from util import read_license_plate

load_dotenv()
CLIENT=InferenceHTTPClient(

    api_url="https://detect.roboflow.com",
    api_key=os.getenv("ROBOFLOW_API_KEY")
)

def scan_plate(car):
    # car2="mages-of-Indian-license-plates.png"
    print("Extracting plate ...")
    result = CLIENT.infer(car,model_id="licence-plate-dausq/2")

    if not result:
        return None
    
    predictions = (result['predictions'][0])

    cX=int(predictions['x'])
    cY=int(predictions['y'])
    width=int(predictions['width'])
    height=int(predictions['height'])

    x1=cX-width/2
    y1=cY-height/2
    x2=cX+width/2
    y2=cY+height/2

    image = cv2.imread(car)

    plate_crop= image[int(y1):int(y2), int(x1+5):int(x2-5)]
    # cv2.imshow("Plate Crop", plate_crop)

    gray=cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
    blur= cv2.GaussianBlur(gray, (5, 5), 0)

    plate_number=read_license_plate(blur, plate_crop)

    return plate_number
