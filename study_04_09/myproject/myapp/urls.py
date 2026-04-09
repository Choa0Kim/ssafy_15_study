# myproject/urls.py
from django.urls import path
from myapp import views

urlpatterns = [
    # 사용자가 'books/' 주소로 접근하면 views.py의 book_list 함수를 실행하라!
    path('', views.book_list, name='book_list'),
]