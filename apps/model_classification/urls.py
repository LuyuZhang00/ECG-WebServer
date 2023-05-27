from django.urls import path
from . import views
from django.urls import path
# from views import ModelInferenceView,HSModelInferenceView,ECGModelInferenceView
urlpatterns = [
    # path('patient/', views.PatientManageViewSet.as_view()),
    path('predict/', views.ModelInferenceView.as_view()),
    path('hspredict/', views.HSModelInferenceView.as_view()),
    path('ecgpredict/', views.ECGModelInferenceView.as_view())
    ]

from rest_framework.routers import SimpleRouter,DefaultRouter

router = DefaultRouter()
# router.register(r'modelclassification', views.PatientManageViewSet, basename='model_classification')

urlpatterns += router.urls