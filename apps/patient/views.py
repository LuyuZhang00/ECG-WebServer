from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import PatientManage
from .Serializer import PatientManageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class PatientManageViewSet(ModelViewSet):
    queryset = PatientManage.objects.all()
    serializer_class = PatientManageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorldView(APIView):
    def get(self, request):
        msg = {"message": "Hello, World!"}
        return Response(msg)
    def post(self, request):
        msg = {"message": "Hello, post!"}
        print(request.data)
        print(request)
        return Response(msg)

class People(APIView):
    def get(self, request):
        patient_list = PatientManage.objects.first()
        serializer = PatientManageSerializer(instance=patient_list, many=False)
        return Response(serializer.data)

    def post(self,request):
        """添加一条数据"""

        # 1. 获取客户端提交的数据，实例化序列化器，获取序列化对象
        serializer =PatientManageSerializer(data=request.data)
        # 2. 反序列化[验证数据、保存数据到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 3. 返回新增的模型数据给客户单
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class People1(APIView):
    def get(self, request):
        msg = {"patient": {
                            "patient_id": "3",
                            "patient_name": "张三",
                            "patient_age": "20"},

                "doctor": {
                            "doctor_id": "1",
                            "doctor_name": "李四",
                            "doctor_age": "30"},

                "model": {
                            "model_name": "transformer",
                            "model_describe": "这是一个深度学习模型"},
                "result": {
                            "result_name": "心电图",
                            "result_id": "1",
                            "result_describe":"正常"}
               }
        return Response(msg)
    def post(self, request):
        print(request)
        msg = {"message": "Hello, post!"}
        return Response(msg)

"""GenericViewSet 通用视图集"""
from rest_framework.viewsets import GenericViewSet
class PatientGenericViewSet(GenericViewSet):
    queryset = PatientManage.objects.all()
    serializer_class = PatientManageSerializer
    def list(self, request):
        """获取所有数据"""
        # 1. 从数据库中读取模型列表信息
        queryset = self.get_queryset() # GenericAPIView提供的get_queryset
        # 2. 序列化
        serializer = self.get_serializer(instance=queryset, many=True)
        # 3. 转换数据并返回给客户端
        return Response(serializer.data)
    def create(self,request):
        """添加一个数据"""
        # 1. 获取客户端提交的数据，实例化序列化器，获取序列化对象
        serializer = self.get_serializer(data=request.data)
        # 2. 反序列化[验证数据、保存数据到数据库]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 3. 返回新增的模型数据给客户单
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, pk):
        """获取一个数据"""
        # 1. 使用pk作为条件获取模型对象
        instance = self.get_object()
        # 2.序列化
        serializer = self.get_serializer(instance=instance)
        # 3. 返回结果
        return Response(serializer.data)
    def update(self,request, pk):
        """更新一个数据"""
        # 1. 使用pk作为条件获取模型对象
        instance = self.get_object()
        # 2. 获取客户端提交的数据
        serializer = self.get_serializer(instance=instance, data=request.data)
        # 3. 反序列化[验证数据和数据保存]
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # 4. 返回结果
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def destory(self, request, pk):
        """删除一个数据"""
        # 1. 根据PK值获取要删除的数据并删除
        self.get_object().delete()
        # 2. 返回结果
        return Response(status=status.HTTP_204_NO_CONTENT)