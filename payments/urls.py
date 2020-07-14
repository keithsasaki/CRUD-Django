from django.urls import path
from . import views

urlpatterns = [
      path('new/',views.create_payment, name='create_payment'),
      path('delete/<int:id>/',views.delete_payment,name='delete_payment'),
      path('update/<int:id>/',views.update_payment,name='update_payment'),
]
