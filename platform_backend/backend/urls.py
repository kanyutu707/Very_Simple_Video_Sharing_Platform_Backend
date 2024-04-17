from django.urls import path, include
from .views import(
    ProductListApiView,
    SysUserApiView
    
)

urlpatterns=[
    path('api', ProductListApiView.as_view()),
    path('users', SysUserApiView.as_view())

]