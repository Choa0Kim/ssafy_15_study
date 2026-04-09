from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render
from .models import Book  # Model에서 데이터를 가져오기 위해 임포트

def book_list(request):
    # 1. Model을 통해 DB에서 모든 책 데이터를 읽어옵니다. (Read Data)
    books = Book.objects.all()
    
    # 2. Template(html)에 데이터를 실어서 보냅니다.
    # render 함수가 '데이터 + HTML'을 버무려 HTTP Response를 생성합니다.
    return render(request, 'myapp/book_list.html', {'books': books})