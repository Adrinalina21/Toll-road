from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=255)
    distance_km = models.FloatField()
    gas_stations_count = models.PositiveIntegerField(default=0)
    map_image = models.ImageField(upload_to='', blank=True, null=True)
    photo = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.photo:
            return f"http://127.0.0.1:9000/routes/{self.photo.name.split('/')[-1]}"
        return "/static/default-image.jpg"
