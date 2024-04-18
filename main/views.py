from django.shortcuts import render


def home(request):
    """Вью-функция для главной страницы."""
    return render(request, template_name='main/index.html')


def contacts(request):
    """Вью-функция для страницы контактов."""
    return render(request, template_name='main/contacts.html')


def hello(request):
    """
    Вью-функция для вывода приветствия.
    Обрабатывает параметры из GET-запроса.
    """
    name = request.GET.get('name')
    message = request.GET.get('message')
    if not name or not message:
        return render(request, template_name='main/hello.html', context={'error_message': "Не все поля заполнены."})
    return render(request, template_name='main/hello.html', context={'name': name, 'message': message})
