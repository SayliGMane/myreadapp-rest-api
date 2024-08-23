from rest_framework import serializers
from apps.book.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    #specify the model ie going to link with seriallizer
    #Specify  which field  should be considered in model

    name= serializers.CharField(read_only = True)
    username = serializers.SerializerMethodField()
   


    def get_username(self,obj): 
        return '_'.join([obj.first_name,obj.last_name])
    

    def validate(self, attrs):
        if attrs.get('first_name') == attrs.get('last_name'):
            raise serializers.ValidationError('first name should not be same')
        return attrs

    def validate_first_name(self,value):
        if '-' in value:
            raise serializers.ValidationError('first name should not contain hyphen (-)')
        return value
    

        
    class Meta:
        model = Author
        fields = "__all__" 
        read_only_fields = ('id',)

     