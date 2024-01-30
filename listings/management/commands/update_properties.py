import requests
from django.core.management.base import BaseCommand
from listings.models import Property
import xml.etree.ElementTree as ET


class Command(BaseCommand):
    help = "Updates the properties from XML API"

    def handle(self, *args, **kwargs):
        # Fetch XML data from the API
        xml_url = "https://api.odysseydubaire.com/listings/feed/generic"
        try:
            response = requests.get(xml_url)
            xml_data = response.text

            # Parse the XML data
            root = ET.fromstring(xml_data)

            # Iterate over the property elements
            for property_element in root.findall("property"):
               
                property_data = {
                    "date": property_element.find("date").text,
                    "property_purpose": property_element.find("property_purpose").text,
                    "ref": property_element.find("ref").text,
                    "price": property_element.find("price").text,
                    "currency": property_element.find("currency").text,
                    "price_freq": property_element.find("price_freq").text,
                    "type": property_element.find("type").text,
                    "sub_location": property_element.find("sub_location").text,
                    "town": property_element.find("town").text,
                    "province": property_element.find("province").text,
                    "country": property_element.find("country").text,
                    "latitude": property_element.find("location/latitude").text,
                    "longitude": property_element.find("location/longitude").text,
                    "location_detail": property_element.find("location_detail").text,
                    "title": property_element.find("title").text,
                    "beds": property_element.find("beds").text,
                    "baths": property_element.find("baths").text,
                    "built_area": property_element.find("surface_area/built").text,
                    "plot_area": property_element.find("surface_area/plot").text,
                    "video_url": property_element.find("video_url").text,
                    "description": property_element.find("desc").text,
                    "agent_name": property_element.find("agent/name").text,
                    "agent_mobile": property_element.find("agent/mobile").text,
                    "agent_email": property_element.find("agent/email").text,
                    "agent_reference": property_element.find("agent/reference").text,
                    "agent_profile_picture": property_element.find(
                        "agent/profile_picture"
                    ).text,
                    "image": [
                        {
                            "url": image_element.find("url").text,
                        }
                        for image_element in property_element.findall("images/image")
                    ],
                    "features": [
                        {
                            "feature": feature_element.text,
                        }
                        for feature_element in property_element.findall(
                            "features/feature"
                        )
                    ],
                    "amenities": [
                        {
                            "amenity": feature_element.text,
                        }
                        for feature_element in property_element.findall(
                            "features/amenity"
                        )
                    ],
                }
                # print(property_data["amenities"])

                # Create or update property instance
                property_instance, created = Property.objects.get_or_create(
                    ref=property_data["ref"], defaults=property_data
                )

                # If propert already exists, update its fields
                if not created:
                    print(f"Property {property_instance.ref} exists")
                print(f"Property {property_instance.ref} created")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching XML data: {e}")
            return
