from rest_framework.views import APIView
from django.http import JsonResponse
import base64
import numpy as np
import cv2

def loadBase64Img(uri):
    nparr = np.fromstring(base64.b64decode(uri), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


class Gangnam_Style(APIView):
    def post(self, request):
        # https://www.python2.net/questions-894144.htm  
        # 요거 보고 하려는데 잘 이해가 안됩니다 ㅠ

        # TODO : try except 처리 (status 400)
        jsonData = request.data[0]
        image = loadBase64Img(jsonData['image'])

        # TODO : projector.py의 함수 여기에 넣기
        # toonify 코드를 참고하기 (로컬에서 왜 안돌아가니ㅠ)
        data = {
            "image": image,
            "response": 1,#if response==1, status 200
        }
        return JsonResponse(data, status=200)
        """
        image = Image.open(BytesIO(base64.b64decode(data['image'])))
        nparr = np.fromstring(base64.b64decode(image), np.uint8)
        image = cv2.imdecode(nparr, cv2.COLOR_BGR2RGB)
        """
