import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Advert
from api_v2.serializers import AdvertSerializer


class AdvertView(APIView):
    def get(self, request, *args, **kwargs):
        adverts = Advert.objects.all()
        serializer = AdvertSerializer(adverts, many=True)
        response_data = serializer.data

        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        advert_data = request.data
        print(advert_data)
        serializer = AdvertSerializer(data=advert_data)
        print(serializer)
        if serializer.is_valid():
            advert = serializer.save()
            return JsonResponse({'id': advert.id})

        return JsonResponse({'error': 'Data not valid'}, status=400)


class AdvertDetailView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs.keys():
            advert = get_object_or_404(Advert, pk=kwargs.get('pk'))
            slr = AdvertSerializer(advert)
            return JsonResponse(slr.data)

    def put(self, request, *args, **kwargs):
        advert = get_object_or_404(Advert.objects.all(), pk=kwargs.get('pk'))
        data = json.loads(request.body)
        srl = AdvertSerializer(instance=advert, data=data, partial=True)
        if srl.is_valid(raise_exception=True):
            advert = srl.update(advert, srl.validated_data)
            return JsonResponse(srl.data, safe=False)
        else:
            response = JsonResponse(srl.errors, safe=False)
            response.status_code = 400
            return response

    def delete(self, request, pk):
        advert = get_object_or_404(Advert.objects.all(), pk=pk)
        advert.delete()
        return Response({
            "message": "Advert with id `{}` has been deleted.".format(pk)
        }, status=204)




