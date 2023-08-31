import os
import cv2

path="images/"

images = []

for file in os.listdir (path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        filename=path+"/"+file
        print (filename)
        images.append(filename)
        count = len(images)
       
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, layers = frame.shape
size = (width,height)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0,count):
     print(images[i])
     frame = cv2.imread(images[i])
     out.write(frame)

    
out.release() # Liberar el video generado
print("Listo")
