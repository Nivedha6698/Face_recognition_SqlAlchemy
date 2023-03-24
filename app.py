import face_recognition
import cv2
from models.sqlalchemy import session, Face

video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

# Extract features from the captured image
face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)

faces = session.query(Face).all()
for face in faces:
    stored_face = face_recognition.face_encodings(face.features)
    matches = face_recognition.compare_faces(stored_face, face_encodings[0])
    if matches[0]:
        print("Match found for " + face.name)
        result = session.query(Face).filter_by(id=face.id).first()
        print(result.name)
        break
else:
    name = input("Enter the name for the new face: ")
    face_features = face_encodings[0].tolist()
    new_face = Face(name=name, features=face_features)
    session.add(new_face)
    session.commit()
    print("New face added to the database")

session.close()
