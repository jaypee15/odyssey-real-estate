import requests
import logging
from django.core.management.base import BaseCommand
from listings.models import Property
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Updates the properties from XML API"

    def handle(self, *args, **kwargs):
        try:
            # Fetch XML data from the API
            xml_url = "https://api.odysseydubaire.com/listings/feed/generic"
            response = requests.get(xml_url)
            response.raise_for_status()  # Check for HTTP errors

            xml_data = response.text

            # Parse the XML data
            root = ET.fromstring(xml_data)

            # Iterate over the property elements
            for property_element in root.findall("property"):
                try:
                    # Extract property data from XML element
                    property_data = self.extract_property_data(property_element)

                    # Create or update property instance
                    property_instance, created = Property.objects.get_or_create(
                        ref=property_data["ref"], defaults=property_data
                    )

                    # If property already exists, update its fields
                    if not created:
                        logger.info(f"Property {property_instance.ref} exists and updated")
                    else:
                        logger.info(f"Property {property_instance.ref} created")
                except Exception as e:
                    logger.error(f"Error processing property element: {e}")

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching XML data: {e}")
            return

    def extract_property_data(self, property_element):
        data = {
            "date": property_element.findtext("date"),
            "property_purpose": property_element.findtext("property_purpose"),
            "ref": property_element.findtext("ref"),
            "price": property_element.findtext("price"),
            "currency": property_element.findtext("currency"),
            "price_freq": property_element.findtext("price_freq"),
            "type": property_element.findtext("type"),
            "sub_location": property_element.findtext("sub_location"),
            "town": property_element.findtext("town"),
            "province": property_element.findtext("province"),
            "country": property_element.findtext("country"),
            "latitude": property_element.findtext("location/latitude"),
            "longitude": property_element.findtext("location/longitude"),
            "location_detail": property_element.findtext("location_detail"),
            "title": property_element.findtext("title"),
            "beds": (property_element.findtext("beds")),
            "baths": (property_element.findtext("baths")),
            "built_area": property_element.findtext("surface_area/built"),
            "plot_area": property_element.findtext("surface_area/plot"),
            "video_url": property_element.findtext("video_url"),
            "description": property_element.findtext("desc"),
            "agent_name": property_element.findtext("agent/name"),
            "agent_mobile": property_element.findtext("agent/mobile"),
            "agent_email": property_element.findtext("agent/email"),
            "agent_reference": property_element.findtext("agent/reference"),
            "agent_profile_picture": property_element.findtext("agent/profile_picture"),
            "image": [
                {"url": image_element.findtext("url")}
                for image_element in property_element.findall("images/image")
            ],
            "features": [feature_element.text for feature_element in property_element.findall("features/feature")],
            "amenities": [amenity_element.text for amenity_element in property_element.findall("amenities/amenity")],
        }
        return data
