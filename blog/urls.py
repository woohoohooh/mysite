from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/archive/', views.post_archive, name='post_archive'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/in_archive/<int:pk>', views.post_in_archive, name='post_in_archive'),
    path('post/un_archive/<int:pk>', views.post_un_archive, name='post_un_archive'),
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'),
    path('post/start/', views.start, name='start'),
    path('index/', views.index, name='index'),
    path('parsing_time/', views.parsing_time, name='parsing_time'),
    path('percent_step1/', views.percent_step1, name='percent_step1'),
    path('percent_step2/', views.percent_step2, name='percent_step2'),
    path('percent_step3/', views.percent_step3, name='percent_step3'),
    path('percent_step4/', views.percent_step4, name='percent_step4'),
    path('percent_step5/', views.percent_step5, name='percent_step5'),
]