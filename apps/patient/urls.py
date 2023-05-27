from django.urls import path
from . import views
from django.urls import path, re_path
from .views import HelloWorldView,People1,People,PatientGenericViewSet

urlpatterns = [
    # path('patient/', views.PatientManageViewSet.as_view()),
    path('hello/', HelloWorldView.as_view()),
    path('people/', People.as_view()),
    path('people1/', People1.as_view()),


    path("peopleset/", views.PatientGenericViewSet.as_view({
        "get": "list",
        "post": "create",
    })),

    re_path("^peopleset/(?P<pk>\d+)/$", views.PatientGenericViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy",
    })),
    ]

from rest_framework.routers import SimpleRouter,DefaultRouter

router = DefaultRouter()
router.register(r'patient', views.PatientManageViewSet, basename='patient')
urlpatterns += router.urls