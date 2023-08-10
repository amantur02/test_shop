from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category.name

        tags = instance.tags.all()
        tag_names = [tag.name for tag in tags]
        representation['tags'] = tag_names

        return representation
