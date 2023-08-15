from django.shortcuts import render
from django.views.generic import TemplateView
from .serializers import RealEstateLeadSerializer, YoutubeLeadSerializer
from .models import RealEstateLead, YoutubeLead
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def index(request):
    return render(request, 'index.html')

def docs(request):
    return render(request, 'docs.html')


@api_view(['GET'])
def youtube_creators_leads(request):
    lead = YoutubeLead.objects.all()
    serializer = YoutubeLeadSerializer(lead, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def real_estate_agents_leads(request):
    lead = RealEstateLead.objects.all()
    serializer = RealEstateLeadSerializer(lead, many=True)
    return Response(serializer.data)