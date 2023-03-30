import cv2
# load some pre-trained data on face frontal from opencv ( haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# choose an image to detect faces in
# img = cv2.imread('busy-street-in-city-at-sunny-day-usa-manhattan-New-york-City.jpg')
# to capture video from default webcam
# webcam = cv2.VideoCapture(0)

# """
# to capture video from default webcam
while True:
    # grab the current frame
    (grabbed, frame) = webcam.read()

    # must convert to black and white
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces
    face_coordination = trained_face_data.detectMultiScale(gray_img)

    # loop over the detected faces
    for (x, y, w, h) in face_coordination:
        # draw a rectangle around the faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 256, 0), 2)

    # show the frame
    cv2.imshow('Clever programing for face detection', frame)
    key = cv2.waitKey(1)

    # if you press 0 it will stop the program because waitKey also capture the key that wos pressed on keyboad
    if key == 0:
        break
# """

"""
# must convert to black and white
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
face_coordination = trained_face_data.detectMultiScale(gray_img)

# loop over the detected faces
for (x, y, w, h) in face_coordination:
    # draw a rectangle around the faces
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# to show image for a fraction of seconds
cv2.imshow('Clever programing for face detection', img)
# to keep the image until any key is not pressed
cv2.waitKey()

# to see if the code is running correctly
print("code completion")
print("There wos no problem with the code...\n")
"""
