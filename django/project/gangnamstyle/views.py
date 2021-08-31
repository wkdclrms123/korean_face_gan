from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
import base64
import request, json
import numpy as np
import cv2
# Create your views here.


class Gangnam_Style(View):

    def post(self, request):
        # https://www.python2.net/questions-894144.htm  
        # 요거 보고 하려는데 잘 이해가 안됩니다 ㅠ
        image = request.POST

        image = Image.open(BytesIO(base64.b64decode(data['image'])))
        nparr = np.fromstring(b64decode(data['image']), np.uint8)
        image = cv2.imdecode(nparr, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image)

    


        return