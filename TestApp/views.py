from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book

# Create your views here.


def index(request):
    author = Author.objects.filter(FAN__bookname='book2')  # 根据书名反向查作者信息
    for item in author:
        print(item.name, item.mobile)

    print(author[0].FAN.all())  # 查询一个作者所有的书,通过主表查询子表(Author为主表，Book为子表)
    author02 = Author(name="测试1", mobile="01234567890")
    author02.save()
    # print(author02.book_set.all())  # 引种写法出错：Author对象无book_set属性

    book = Book.objects.filter(author__mobile='18628315368')[0]  # 根据作者信息查书信息
    print(book.bookname)

    return HttpResponse("helloword")
