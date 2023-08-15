from rest_framework import serializers
from api_app.models import RealEstateLead, YoutubeLead

class RealEstateLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateLead 
        fields = '__all__'
        
        
class YoutubeLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeLead
        fields = '__all__'
               