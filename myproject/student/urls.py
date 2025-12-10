from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('addstudent/', views.add_student),
    path('addition/',views.addition),
    path('delete/<int:id>/',views.del_student),
    path('editstudent/<int:id>/', views.edit_student),
    path('update/<int:id>/', views.update_student)

]