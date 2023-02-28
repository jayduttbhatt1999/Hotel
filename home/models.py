from django.db import models
import uuid
# Create your models here.

class BaseModel(model.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name


class Hotel(BaseModel):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)
    def __str__(self) -> str:
        return self.hotel_name


class HotelImage(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name="Hotel")
    images = models.ImageField(upload_to=="hotel")