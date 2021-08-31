import cv2
import os
import numpy as np
from retinaface import RetinaFace
from retinaface.commons import postprocess
from PIL import Image

face_detector = RetinaFace.build_model()

path = "./images/"
files = os.listdir(path)
img_count = 0

for file in files:
    try:
        img = cv2.imread(path+file, cv2.IMREAD_COLOR)
        print(file)
        base_img = img.copy()
        img_region = [0, 0, img.shape[0], img.shape[1]]
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        obj = RetinaFace.detect_faces(img_rgb, model=face_detector, threshold=0.9)

        resp = []
        detected_face = None
        if type(obj) == dict:
            print("detected face count :", len(obj))
            for key in obj:
                identity = obj[key]
                facial_area = identity["facial_area"]

                y = facial_area[1]
                h = facial_area[3] - y
                x = facial_area[0]
                w = facial_area[2] - x
                img_region = [x, y, w, h]

                # 저화질 이미지는 삭제 (양질의 이미지 획득 조절 가능)
                print(facial_area)
                if h < 100 or w < 100:
                    print("skip")
                    continue

                #헤어 스타일 까지 포함할 수 있도록 h_cut setting
                h_cut = int(h * 0.25)
                w_cut = int(w * 0.25)

                #detected_face = img[int(y):int(y+h), int(x):int(x+w)] #opencv
                detected_face = img[facial_area[1]-h_cut: facial_area[3]+h_cut, facial_area[0]-w_cut: facial_area[2]+w_cut]

                landmarks = identity["landmarks"]
                left_eye = landmarks["left_eye"]
                right_eye = landmarks["right_eye"]
                nose = landmarks["nose"]
                #mouth_right = landmarks["mouth_right"]
                #mouth_left = landmarks["mouth_left"]

                #detected_face = postprocess.alignment_procedure(detected_face, right_eye, left_eye, nose)

                resp.append((detected_face, img_region))
    except:
        pass

    if len(resp) > 0:
        for res in resp:
            try:
                detected_face = cv2.cvtColor(res[0], cv2.COLOR_RGB2BGR)
                #detected_face = np.resize(detected_face, (540, 540))
                #cv2.imwrite('./images_face_only/'+str(img_count)+'.jpg', detected_face)
                Image.fromarray(detected_face)\
                    .resize((256, 256), Image.NEAREST)\
                    .save('./images_face_only/'+str(img_count)+'.jpg')
                img_count += 1
            except:
                print("no detected face")

    if img_count == 8:
        break

