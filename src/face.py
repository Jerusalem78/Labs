import face_recognition

sergey_image = face_recognition.load_image_file(r"src\img\simonovsergey-profile_image-21712b2a00d343db-300x300.jpeg")
sergey1_image = face_recognition.load_image_file(r"src\img\sergey.jpg")
ozon_image = face_recognition.load_image_file(r"src\img\ozon.jpg")

sergey_encoding = face_recognition.face_encodings(sergey_image)[0]
sergey1_encoding = face_recognition.face_encodings(sergey1_image)[0]
ozon_encoding = face_recognition.face_encodings(ozon_image)[0]

results = face_recognition.compare_faces([sergey_encoding], sergey1_encoding)
results2 = face_recognition.compare_faces([ozon_encoding], sergey1_encoding)

print(results)
print(results2)