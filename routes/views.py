# views.py
from django.shortcuts import render
from .models import get_all_routes, get_route_by_id

def route_list(request):
    routes = get_all_routes()
    return render(request, 'list.html', {
        'routes': routes,
        'LOGO_URL': 'http://127.0.0.1:9000/routes/logo.png',
        'CART_URL': 'http://127.0.0.1:9000/routes/cart.png'
    })

def cart_view(request):
    return render(request, 'cart.html')

def route_detail(request, route_id):
    route_data = get_route_by_id(route_id)
    return render(request, 'route_detail.html', {'route': route_data})