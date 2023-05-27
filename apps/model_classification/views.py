import cv2
from rest_framework.viewsets import ModelViewSet
from .models import ModelManage
from .Serializer import ModelManageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np

# class PatientManageViewSet(ModelViewSet):
#     queryset = ModelManage.objects.all()
#     serializer_class = ModelManageSerializer

#
from model_classification.keras_predict.inference import KerasPredict


class ModelInferenceView(APIView):
    def get(self, request):
        model_path = request.data['model_path']
        image_path = request.data['image_path']
        result = KerasPredict(model_path, image_path)

        return Response(result)


from model_classification.HS.HSModelTest import hs_inference


class HSModelInferenceView(APIView):
    def get(self, request):
        i =request.GET["data"]
        print(i)
        dataset = np.load('/home/bme/Documents/bme_ECG/django_ECG/apps/model_classification/HS/testdata20.npy')
        test_data = dataset[0:1, :, :]
        result = hs_inference(test_data)
        return Response(result)


from model_classification.ECG.ECGModelTest import ecg_inference

class ECGModelInferenceView(APIView):
    def get(self, request):
        # data_input = request.data
        print(request)
        i = request.GET["data"]
        im_gray = cv2.imread(r'/home/bme/Documents/bme_ECG/django_ECG/apps/model_classification/ECG/Data/A/' + str(i) + '.png')
        im_gray = im_gray.reshape((1, 128, 128, 3))
        data_input = im_gray
        result = ecg_inference(data_input)
        
        return Response(result)


# class HSModelInferenceView(APIView):
#     def get(self, request):
#         i = request.GET["data"]
#         print(i)
#         dataset = np.load('/home/bme/Documents/bme_ECG/django_ECG/apps/model_classification/HS/testdata20.npy')
#         test_data = dataset[0:1, :, :]
#         result = hs_inference(test_data)
#         return Response(result)
#
#
# from model_classification.ECG.ECGModelTest import ecg_inference
#
#
# class ECGModelInferenceView(APIView):
#     def get(self, request):
#         """
#         get请求，测试时使用了图片序号，后续可直接传入图片
#         :param request:
#         :return:
#         """
#         print(request)
#         i = request.GET["data"]
#         im_gray = cv2.imread(
#             r'/home/bme/Documents/bme_ECG/django_ECG/apps/model_classification/ECG/Data/A/' + str(i) + '.png')
#         im_gray = im_gray.reshape((1, 128, 128, 3))
#         data_input = im_gray
#         result = ecg_inference(data_input)
#
#         return Response(result)