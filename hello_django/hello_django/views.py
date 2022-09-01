from django.http import HttpResponse
from django.shortcuts import render


def about(request):  # содержит в себе информацию, какой был запрос, что надо для этого запроса и т.д.
    a = 6 + 5
    return render(request, 'about.html', {'gretting': a})  # импортирует из django http-ответ, который возвращает строку в скобках


def home(request):
    return HttpResponse('This is my home')
