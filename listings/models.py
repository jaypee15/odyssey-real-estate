from django.db import models


class Property(models.Model):
    date = models.CharField(max_length=255)
    property_purpose = models.CharField(max_length=255)
    ref = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    price_freq = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    sub_location = models.TextField()
    town = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    location_detail = models.TextField()
    title = models.TextField()
    beds = models.CharField(max_length=255, blank=True, null=True)
    baths = models.CharField(max_length=255, blank=True, null=True)
    built_area = models.CharField(max_length=255, blank=True, null=True)
    plot_area = models.CharField(max_length=255, blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    # Agent Information
    agent_name = models.CharField(max_length=255)
    agent_mobile = models.CharField(max_length=20)
    agent_email = models.EmailField()
    agent_reference = models.CharField(max_length=255)
    agent_profile_picture = models.CharField(max_length=255, blank=True, null=True)

    # Image URLs
    images = models.TextField()

    # Features
    features = models.TextField()

    # Amenities
    amenities = models.TextField()

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title
