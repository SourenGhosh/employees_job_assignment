from django.urls import path
from .import views
urlpatterns = [

#    path('new1/', views.manage_data1, name="manage_data1"),
    path('post/', views.indexView, name='indexView'),
    path('post/<str:pk_test>/', views.indexView1, name='indexView1'),
    path('updateJoballocation/<str:pk>/', views.updateJoballocation, name='updateJoballocation'),
]