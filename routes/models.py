# models.py
from typing import Dict, List


class Route:
    def __init__(self, id: int, name: str, distance_km: float, gas_stations_count: int = 0,
                 map_image: str = None, photo: str = None, details: str = '',
                 description: str = '', notes: str = ''):
        self.id = id
        self.name = name
        self.distance_km = distance_km
        self.gas_stations_count = gas_stations_count
        self.map_image = map_image
        self.photo = photo
        self.details = details
        self.description = description
        self.notes = notes

    def get_image_url(self):
        if self.photo:
            return f"http://127.0.0.1:9000/routes/{self.photo}"
        return "/static/default-image.jpg"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'distance_km': self.distance_km,
            'gas_stations_count': self.gas_stations_count,
            'map_image': self.map_image,
            'photo': self.photo,
            'image_url': self.get_image_url(),
            'details': self.details,
            'description': self.description,
            'notes': self.notes
        }


# Хранилище данных
_routes: Dict[int, Route] = {
    1: Route(
        id=1,
        name='ПУСКОВОЙ КОМПЛЕКС №1',
        distance_km=49.5,
        gas_stations_count=3,
        map_image='map1.png',
        photo='route1.jpg',
        details='От М-4 до 11 км А-107 — 49,5 км',
        description='Важный участок с высокой пропускной способностью.',
        notes='Этот участок включает несколько ключевых транспортных узлов.'
    ),
    2: Route(
        id=2,
        name='ПУСКОВОЙ КОМПЛЕКС №3',
        distance_km=105.9,
        gas_stations_count=5,
        map_image='map2.png',
        photo='route2.jpg',
        details='От М-11 до М-7 — 105,9 км',
        description='Маршрут по важному участку.',
        notes='Проходит через важные транспортные узлы.'
    )
}


def get_all_routes() -> List[Dict]:
    return [route.to_dict() for route in _routes.values()]


def get_route_by_id(route_id: int) -> Dict:
    route = _routes.get(route_id)
    return route.to_dict() if route else None
