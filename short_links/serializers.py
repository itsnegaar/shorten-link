from rest_framework import serializers

from short_links.models import LinkStorage


class ShortLinksSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = LinkStorage
        fields =['original_link']

class ShortLinksGetSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = LinkStorage
        fields =['code']

    def validate_code(self, value):
        if len(value) != 6:
            raise serializers.ValidationError("Code must be 6 characters")
