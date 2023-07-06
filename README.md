# 心电心音管理系统服务端

## 1项目介绍
这是一个基于Django的心电心音管理系统的服务端页面，其主要功能有：

1.与心电心音采集的客户端进行数据交互，实现数据的上传和下载

2.患者、模型、医院等信息的管理

3.调用模型分析患者的心电心音数据，并返回给客户端

[答辩PPT](心电监测平台项目答辩.pdf)

[项目报告](心脏生理信号监测诊断系统的开发_项目报告.pdf)

----------------------------------------
## 2项目展示
首页：
![首页.png](img%2F%E9%A6%96%E9%A1%B5.png)

医院名单：
![医院名单.png](img%2F%E5%8C%BB%E9%99%A2%E5%90%8D%E5%8D%95.png)

医院增加列表：
![医院增加爱页面.png](img%2F%E5%8C%BB%E9%99%A2%E5%A2%9E%E5%8A%A0%E7%88%B1%E9%A1%B5%E9%9D%A2.png)

模型列表：
![模型列表.png](img%2F%E6%A8%A1%E5%9E%8B%E5%88%97%E8%A1%A8.png)

患者列表：
![患者列表.png](img%2F%E6%82%A3%E8%80%85%E5%88%97%E8%A1%A8.png)

权限分组列表
![组列表.png](img%2F%E7%BB%84%E5%88%97%E8%A1%A8.png)

----------------------------------------
## 3.文件结构
```

├── app   #项目应用      
│   ├── hospital   #医院管理模块
│   │   ├── admin.py  #后台管理页面admin的配置项
│   │   ├── apps.py 
│   │   ├── migrations  #数据库迁移文件
│   │   ├── models.py   #数据库模型
│   │   ├── resources.py 
│   │   ├── Serializer.py #序列化
│   │   ├── urls.py       #url配置
│   │   └── views.py      #视图函数,处理请求,返回响应
│   ├
│   ├── model_classification  #模型管理模块
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── keras_predict
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── Serializer.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── patient        #患者管理模块
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       ├── models.py
│       ├── Serializer.py
│       ├── urls.py
│       └── views.py
│      
├── db.sqlite3   #数据库文件
├── django_ECG   #项目配置文件
│   ├── asgi.py  #异步请求处理
│   ├── __init__.py  
│   ├── __pycache__
│   ├── settings.py  #项目配置,包括数据库配置,静态文件配置,模板文件配置,中间件配置,
│   ├                   缓存配置,日志配置,第三方应用配置,自定义应用配置,国际化配置  十分重要
│   ├── urls.py      #路由配置
│   └── wsgi.py      #wsgi请求处理
├
├── img
├── __init__.py
├── manage.py              #项目启动文件
├── README.md              #项目说明文件
├── requirements.txt       #项目依赖文件
├
└── static                 #静态文件    
    ├── admin              #后台管理页面静态文件,主要是后台的前端文件
    │   ├── css
    │   ├── fonts
    │   ├── img
    │   ├── js
    │   └── simpleui-x     #后台管理页面的主题
    ├── doctor        #医生管理模块上传的文件
    │   └── 2023
    ├── models_file 
    ├── patient       #患者管理模块上传的文件
    │   └── 2023
    ├── rest_framework   #rest_framework框架的静态文件
    │   ├── css
    │   ├── docs
    │   ├── fonts
    │   ├── img
    │   └── js
    └── upload    #其余上传的文件
      
```

----------------------------------------
## 4.模型调用
模型调用的接口在model_classification文件夹下的views.py文件中

客户端使用GET请求传data给服务端，服务器调用模型进行分析，返回分析结果给客户端。

ECGModelInferenceView为调用ECG模型的接口
```python3
from model_classification.ECG.ECGModelTest import ecg_inference
class ECGModelInferenceView(APIView):
    def get(self, request):
        #客户端将数据以{data:array}参数传入,通过get请求获取数据
        data_input = request.GET["data"]
        result = ecg_inference(data_input)
        return Response(result)
```
模型推理：
```python3
def ecg_inference(input_data):
    model = load_model('model_classification/ECG/ECGmodel_cp1.h5')
    pred = model.predict(input_data)
    pred_class = pred.argmax(axis=-1)
    result=pred_class[0]
    return result
```
----------------------------------------
HSModelInferenceView为调用HS模型的接口
```python3
from model_classification.HS.HSModelTest import hs_inference
class HSModelInferenceView(APIView):
    def get(self, request):
        #客户端将数据以{data:array}参数传入，通过get请求获取数据
        data_input=request.GET["data"]
        result = hs_inference(data_input)
        return Response(result)
```
模型推理：
```python3
def hs_inference(input_data):
    model = load_model('model_classification/HS/HSmodel_cp01.h5')
    test_predictions = model.predict(input_data)
    result = np.argmax(test_predictions)
    return result
```
---------------------------------------


## 5.开发环境
主要依赖包：
* python==3.9.16
* django==2.2.28
* djangorestframework==3.14.0
* django-simpleui==2023.3.1
* sqlite3  
* 其余详见requirements.txt


pycharm：
![编辑页面.png](img%2F%E7%BC%96%E8%BE%91%E9%A1%B5%E9%9D%A2.png)


数据库可视化面板：dbeaver
![数据库管理页面.png](img%2F%E6%95%B0%E6%8D%AE%E5%BA%93%E7%AE%A1%E7%90%86%E9%A1%B5%E9%9D%A2.png)

----------------------------------------
## 6.项目部署
目前已完成服务端在局域网下与客户端进行数据传输，并已测试完成。若要部署到公网，需要进行以下操作：

可以直接部署到阿里云或腾讯云，具体操作见：https://cloud.tencent.com/document/product/213/6090

需要域名且备案，由于备案未成功，后续可再次进行尝试

平台的部署教程较多，这里不再赘述。
参考链接：
https://blog.csdn.net/qq_45660133/article/details/123391558

----------------------------------------
## 7.后续工作
1.增加django_dicom模块,实现dicom文件的上传和下载，以及在线显示：https://github.com/TheLabbingProject/django_dicom

2.增加django-mri模块,实现mri文件的上传和下载:https://github.com/TheLabbingProject/django_mri 

(目前这两个模块不完善，需要做进一步适配)

3.增加django-echarts模块,实现echarts图表的首页展示:

4.实现模型的自由切换
