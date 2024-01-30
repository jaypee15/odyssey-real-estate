import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from listings.models import Propertyy

class Command(BaseCommand):
    help = 'Import properties from XML file'

    def add_arguments(self, parser):
        parser.add_argument('xml_file', type=str, help='Path to the XML file')

    def handle(self, *args, **options):
        xml_file_path = options['xml_file']
        self.import_properties(xml_file_path)

    def import_properties(self, xml_file_path):
        # Parse XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Iterate through XML elements and save to database
        for property_element in root.findall('property'):
            property_data = self.extract_property_data(property_element)
            Propertyy.objects.create(**property_data)

    def extract_property_data(self, property_element):
        # Extract data from XML element and return as a dictionary
        # You need to implement this based on your XML structure
        # For example:
        
        data = {
            'date': property_element.findtext('date'),
            'property_purpose': property_element.findtext('property_purpose'),
            'ref': property_element.findtext('ref'),
            'price': property_element.findtext('price'),
            'currency': property_element.findtext('currency'),
            'price_freq': property_element.findtext('price_freq'),
            'type': property_element.findtext('type'),
            'sub_location': property_element.findtext('sub_location'),
            'town': property_element.findtext('town'),
            'province': property_element.findtext('province'),
            'country': property_element.findtext('country'),
            'latitude': property_element.findtext('latitude'),
            'longitude': property_element.findtext('longitude'),
            'location_detail': property_element.findtext('location_detail'),
            'title': property_element.findtext('title'),
            'beds': int(property_element.findtext('beds')),
            'baths': int(property_element.findtext('baths')),
            'built_area': property_element.findtext('built_area'),
            'plot_area': property_element.findtext('plot_area'),
            'video_url': property_element.findtext('video_url'),
            'description': property_element.findtext('description'),
            'agent_name': property_element.findtext('agent/name'),
            'agent_mobile': property_element.findtext('agent/mobile'),
            'agent_email': property_element.findtext('agent/email'),
            'agent_reference': property_element.findtext('agent/reference'),
            'agent_profile_picture': property_element.findtext('agent/profile_picture'),
            'image': property_element.findtext('image'),
            'features': [feature.text for feature in property_element.findall('features/feature')],
            'amenities': [amenity.text for amenity in property_element.findall('amenities/amenity')],
        }
        return data
    

     # # Extract image details
                # image_data = [
                #     {
                #         "url": image_element.find("url").text,
                #     }
                #     for image_element in property_element.findall("images/image")
                # ]

                # # Create or update image instance
                # image_instance, _ = Image.objects.get_or_create(
                #     url=image_data[0]["url"] if image_data else "",
                # )

