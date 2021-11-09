from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import TestSerializer
from pngmerge.serializerObjects.testserializers import testSerializerObject

from PIL import Image

@api_view(['GET'])
@permission_classes([AllowAny])
def Test(request):
    testObject = testSerializerObject(False)
    serializer = TestSerializer(testObject)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def img(request, body, hat, weapon):
    bodyimg = Image.open('pngmerge/ImageSource/body/'+ str(body) +'.png').convert("RGBA")
    hatimg = Image.open('pngmerge/ImageSource/hat/'+ str(hat) +'.png').convert("RGBA")
    weaponimg = Image.open('pngmerge/ImageSource/weapon/'+ str(weapon) +'.png').convert("RGBA")

    bg_img = Image.new('RGBA', (bodyimg.width,bodyimg.height), (0, 0, 0, 0))
    bg_img.paste(bodyimg, mask=bodyimg)
    bg_img.paste(weaponimg, mask=weaponimg)
    bg_img.paste(hatimg, mask=hatimg)

    response = HttpResponse(content_type="image/png")
    bg_img.save(response, format="png")
    return response