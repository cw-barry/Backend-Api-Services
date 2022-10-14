from rest_framework import serializers
from .models import *

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ("location","xid","name","osm","wikidata","kinds","image","text","html")


class LocationSerializer(serializers.ModelSerializer):
    places = PlacesSerializer(many=True, required=False)

    class Meta:
        model = Location
        fields = (
            "id",
            "name", 
            "country", 
            "lat", 
            "lon",
            "population",
            "timezone",
            "places"
            )

    # def validate(self, data):

    #     print(self.context.get('request').headers.get('OTM-Api-Key'))
    #     if not self.context.get('request').headers.get('OTM-Api-Key'):
    #         raise serializers.ValidationError({"api_key": "Provide your api key as OTM-Api-Key inside headers"})
    #     return data
