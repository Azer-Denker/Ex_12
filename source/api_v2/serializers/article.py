from rest_framework import serializers

from webapp.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'author', 'created_at')
        read_only_fields = ('author', 'id')

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance.pk
