from django.shortcuts import render, get_object_or_404
from .models import Route

def route_list(request):
    routes = Route.objects.all()
    return render(request, 'list.html', {
        'routes': routes,
        'LOGO_URL': 'http://127.0.0.1:9000/routes/logo.png',
        'CART_URL': 'http://127.0.0.1:9000/routes/cart.png'
    })


def cart_view(request):
    return render(request, 'cart.html')


def route_detail(request, route_id):
    # Получаем данные для маршрута по ID (например, из базы данных)
    route_data = get_route_by_id(route_id)

    return render(request, 'route_detail.html', {'route': route_data})


def get_route_by_id(route_id):
    # Пример данных для маршрута (эти данные можно брать из базы данных)
    routes = {
        1: {'title': 'ПУСКОВОЙ КОМПЛЕКС №1', 'details': 'От М-4 до 11 км А-107 — 49,5 км',
            'description': 'Важный участок с высокой пропускной способностью.',
            'notes': 'Этот участок включает несколько ключевых транспортных узлов.'},
        2: {'title': 'ПУСКОВОЙ КОМПЛЕКС №3', 'details': 'От М-11 до М-7 — 105,9 км',
            'description': 'Маршрут по важному участку.', 'notes': 'Проходит через важные транспортные узлы.'},
        # Добавь остальные маршруты
    }
    return routes.get(route_id, None)
