import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)

    color = (0, 255, 0)                #Color of the Rectangle
    for (x, y, w, h) in faces:

        Start_index_X = x
        Start_index_Y = y
        End_index_X = x + w
        End_index_Y = y + h
        cv2.rectangle(frame, (Start_index_X, Start_index_Y), (End_index_X, End_index_Y), color, 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        img_item = "myitem.png"
        cv2.imwrite(img_item, roi_gray)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()