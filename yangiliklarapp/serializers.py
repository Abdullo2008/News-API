from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import NewsModel, Category


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = ['title', 'body', 'category']
        # fields = ['title', 'body', 'category']
        # extra_kwargs = {
        #     'title': {'required': False},
        #     'body': {'required': False},
        #     'category': {'required': False}
        # }

    def validate(self, data):
        title = data.get('title', None)

        if title == title.upper():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Sarlavhaning hamma harflari katta bulishi mumkin emas.'
                }
            )
        if not title.isalpha():
            raise ValidationError(
                                {
                                    "status": False,
                                    'message': "Yangilikning sarlavhasi harflardan tashkil topishi kerak!"
                                }
                            )
        if title:
            if NewsModel.objects.filter(title=title).exists():
                raise ValidationError(
                    {
                        'status': False,
                        'message': 'Yangilik sarlavhasi mavjud! Iltimos boshqa sarlavha yozing'
                    }
                )


# class NewsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     body = serializers.CharField()
#     category = serializers.ChoiceField(Category)

# class New_Patch_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewsModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, data):
        name = data.get('name', None)

        if name == name.upper():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Kategoriya nomi hamma harflari katta bulishi mumkin emas.'
                }
            )
        if not name.isalpha():
            raise ValidationError(
                                {
                                    "status": False,
                                    'message': "Kategoriya nomi harflardan tashkil topishi kerak!"
                                }
                            )
        if name:
            if NewsModel.objects.filter(name=name).exists():
                raise ValidationError(
                    {
                        'status': False,
                        'message': 'Ushbu kategoriya nomi mavjud!'
                    }
                )
