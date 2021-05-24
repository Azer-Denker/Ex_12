import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Article
from api_v2.serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        response_data = serializer.data

        return Response(data=response_data)

    def post(self, request, *args, **kwargs):
        article_data = request.data
        print(article_data)
        serializer = ArticleSerializer(data=article_data)
        print(serializer)
        if serializer.is_valid():
            article = serializer.save()
            return JsonResponse({'id': article.id})

        return JsonResponse({'error': 'Data not valid'}, status=400)


class ArticleDetailView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs.keys():
            article = get_object_or_404(Article, pk=kwargs.get('pk'))
            slr = ArticleSerializer(article)
            return JsonResponse(slr.data)

    def put(self, request, *args, **kwargs):
        article = get_object_or_404(Article.objects.all(), pk=kwargs.get('pk'))
        data = json.loads(request.body)
        srl = ArticleSerializer(instance=article, data=data, partial=True)
        if srl.is_valid(raise_exception=True):
            article = srl.update(article, srl.validated_data)
            return JsonResponse(srl.data, safe=False)
        else:
            response = JsonResponse(srl.errors, safe=False)
            response.status_code = 400
            return response

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)




