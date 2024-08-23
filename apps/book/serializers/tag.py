from rest_framework import serializers
from apps.book.models import Tag
import re 

class TagSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()


    def get_name(self,obj):
      
        return obj.name.title()

    def validate_name(self, value):
        """
        Validate the 'name' field to ensure it does not contain special characters.
        """
        if re.search(r'[!@#$%^&*]', value):
            raise serializers.ValidationError("Tag name should not contain special characters like !@#$%^&*")
        return value

    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ('id',)