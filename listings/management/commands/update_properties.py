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
                # Extract the property details
                property_data = {
                    "date": property_element.find("date").text,
                    "property_purpose": property_element.find("property_purpose").text,
                    "ref": property_element.find("ref").text,
                    "price": property_element.find("price").text,
                    "currency": property_element.find("currency").text,
                    "price_freq": property_element.find("price_freq").text,
                    "property_type": property_element.find("type").text,
                    "sub_location": property_element.find("sub_location").text,
                    "town": property_element.find("town").text,
                    "province": property_element.find("province").text,
                    "country": property_element.find("country").text,

                    "location": {
                        "latitude": property_element.find("location/latitude").text,
                        "longitude": property_element.find("location/longitude").text,
                    },

                    "location_detail": property_element.find("location_detail").text,
                    "title": property_element.find("title").text,
                    "beds": property_element.find("beds").text,
                    "baths": property_element.find("baths").text,
                    "surface_area": {
                        "built": property_element.find("surface_area/built").text,
                        "plot": property_element.find("surface_area/plot").text,
                    },

                    "video_url": property_element.find("video_url").text,
                    "description": property_element.find("desc").text,

                    "agent": {
                        "name": property_element.find("agent/name").text,
                        "mobile": property_element.find("agent/mobile").text,
                        "email": property_element.find("agent/email").text,
                        "reference": property_element.find("agent/reference").text,
                        "profile_picture": property_element.find("agent/profile_picture").text,
                    },

                    "images": [
                        
                    ]


                }

                print(property_data["surface_area"])
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching XML data: {e}")
            return
       
