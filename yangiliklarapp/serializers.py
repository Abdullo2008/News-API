from rest_framework import serializers

from .models import NewsModel, Category


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'
        # fields = ['title', 'body', 'category']
        # extra_kwargs = {
        #     'title': {'required': False},
        #     'body': {'required': False},
        #     'category': {'required': False}
        # }


# class New_Patch_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewsModel



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
