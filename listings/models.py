from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Location(models.Model):
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])

class Agent(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    reference = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="agent_profiles/", blank=True, null=True)

class Image(models.Model):
    url = models.URLField()

class Feature(models.Model):
    content = models.CharField(max_length=255)

class Amenity(models.Model):
    content = models.CharField(max_length=255)

class SurfaceArea(models.Model):
    built = models.IntegerField()
    plot = models.IntegerField(null=True, blank=True)

class Property(models.Model):
    date = models.DateTimeField()
    property_purpose = models.CharField(max_length=255)
    ref = models.CharField(max_length=20, unique=True)
    price = models.IntegerField()
    currency = models.CharField(max_length=10)
    price_freq = models.CharField(max_length=10)
    property_type = models.CharField(max_length=255)
    sub_location = models.TextField()
    town = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    location_detail = models.TextField()
    title = models.TextField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    surface_area = models.OneToOneField(SurfaceArea, on_delete=models.DO_NOTHING)
    video_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    agent = models.OneToOneField(Agent, on_delete=models.DO_NOTHING)
    images = models.ManyToManyField(Image)
    features = models.ManyToManyField(Feature)
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.title
