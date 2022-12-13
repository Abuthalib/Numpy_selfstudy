# Import the necessary libraries
import cv2
import face_recognition

# Load the image of the person you want to recognize
image = cv2.imread('person.jpg')

# Run the face recognition algorithm on the image
face_locations = face_recognition.face_locations(image)

# Loop through the detected faces
for face_location in face_locations:
  # Get the coordinates of the face
  top, right, bottom, left = face_location

  # Draw a rectangle around the face
  cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

# Show the detected faces
cv2.imshow('Faces', image)
cv2.waitKey(0)
