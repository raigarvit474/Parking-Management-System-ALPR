import easyocr as ocr
import cv2
import re
reader = ocr.Reader(['en'])

pattern = r'[^a-zA-Z0-9]'

def read_license_plate(processed_plate, plate_crop):
    detections= reader.readtext(processed_plate)

    if not detections:
        print("No plate detected")
        return None
    
    im2= processed_plate.copy()
    h,w,_=plate_crop.shape
    mainBoxRect = h*w
    # cv2.rectangle(im2, (0, 0), (w, h), (0, 0, 255), 2)

    # cv2.imshow('plate', im2)

    final=[]
    for detection in detections:
        bbox,text,_=detection
        x1,y1=bbox[0]
        x2,y2=bbox[2]

        width=abs(x2-x1)
        height=abs(y2-y1)
        area=width*height
        ratio=area/mainBoxRect

        if ratio>0.15:
            cleaned_string=re.sub(pattern,'',text)
            cv2.rectangle(plate_crop, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)
            final.append(cleaned_string.upper())


    return "".join(final)