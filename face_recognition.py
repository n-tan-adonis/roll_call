import cv2
import face_recognition
import os
from datetime import datetime

import numpy as np

#Step 1: load ảnh từ kho nhận dạng
path = "pic2"
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f"{path}/{cl}")
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

#Encoding
def Mahoa(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

endcodeListKnow = Mahoa(images)
print("Ma Hoa thanh cong")
print(len(endcodeListKnow))

def roll_call(name):
    with open("diemdanh.csv", "r+") as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(",")
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time_string = now.strftime("%H:%M:%S")
            date_string = now.strftime("%d-%m-%Y")
            f.write(f"\n{name},{time_string},{date_string}")


cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frameS = cv2.resize(frame, (0,0), None, fx=0.5, fy=0.5)
    frameS = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)

    #Xác định vị trí khuôn mặt trên cam và encoding hình ảnh trên cam
    facecurFrame = face_recognition.face_locations(frameS)      #lấy từng khuôn mặt và vị trí khuôn mặt hện tại
    encodecurFrame = face_recognition.face_encodings(frameS)

    for encodeFace, faceLoc in zip(encodecurFrame, facecurFrame):       #lấy vị trí khuôn mặt và vị trí khuôn mặt hiện tại theo cặp
        matches = face_recognition.compare_faces(endcodeListKnow, encodeFace)
        faceDis = face_recognition.face_distance(endcodeListKnow, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)     #đẩy về giá trị index của faceDis nhỏ nhất

        if faceDis[matchIndex] <0.50:
            name = classNames[matchIndex]
            key = cv2.waitKey(1)
            if key == ord("c"):
                roll_call(name)
        else:
            name = "Unknow"

        #print tên lên frame
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, name, (x2, y2), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)

    cv2.imshow("Cua so hien thi", frame)
    key = cv2.waitKey(1)
    if key == ord("e"):
        break


cap.release()
cv2.destroyAllWindows()