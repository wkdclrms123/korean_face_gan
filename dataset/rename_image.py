#fix github page
import os

path = "./images_face_only/"
img_count = 0
for filename in os.listdir(path):
    os.rename(path+filename, path+'seed_'+str(img_count)+'.jpg')
    img_count += 1
