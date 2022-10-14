from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Places, Location
from .serializers import PlacesSerializer, LocationSerializer
import requests
from django.http import JsonResponse
from decouple import config

# Create your views here.
class LocationView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('name', )

    def get(self, request, *args, **kwargs):
        # if not request.headers.get('OTM-Api-Key'):
        #     return JsonResponse({"api_key": "Provide your api key as OTM-Api-Key inside headers"})
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Location.objects.all()
       
        # title = self.kwargs["location"]
        name = self.request.query_params.get('name')
        print(name)

        if not name:
            queryset = Location.objects.none()
            return queryset

        queryset = queryset.filter(name__iexact = name)


        if not queryset:
            api_key = self.request.headers.get('Otm-Api-Key')

            if not api_key and config('DEBUG'):
                api_key = config('OTM_API_KEY')
           

            url = "https://api.opentripmap.com/0.1/en/places/geoname?apikey="+api_key+"&name="+name

            res = requests.get(url)
            data = res.json()
            print(data)
            if data:

                data.pop('status')
                place = Location.objects.create(**data)

                url = "https://api.opentripmap.com/0.1/en/places/radius?apikey="+api_key+"&rate=3&radius=1000&lat="+str(place.lat)+"&lon="+str(place.lon)+"&format=json"

                res = requests.get(url)
                data_places = res.json()

                for item in data_places:
                    data_save = dict()
  
                    # point = item.pop("point")
                    # item.pop("rate")
                    # if item.get("dist"):
                    #     item.pop("dist")
                    # item["lat"] = point.get("lat")
                    # item["lon"] = point.get("lon")

                    data_save["xid"] = item.get("xid")
                    data_save["name"] = item.get("name")
                    data_save["osm"] = item.get("osm")
                    data_save["wikidata"] = item.get("wikidata")
                    data_save["kinds"] = item.get("kinds")

                    item_url = "https://api.opentripmap.com/0.1/en/places/xid/"+item.get("xid")+"?apikey="+api_key
                    res_item = requests.get(item_url)
                    item_data = res_item.json()

                    data_save["image"] = item_data.get("preview").get("source")
                    data_save["text"] = item_data.get("wikipedia_extracts").get("text")
                    data_save["html"] = item_data.get("wikipedia_extracts").get("html")

                    Places.objects.create(location=place, **data_save)
       
        return Location.objects.all().filter(name__iexact = name)
