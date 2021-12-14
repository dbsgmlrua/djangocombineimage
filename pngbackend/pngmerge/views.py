from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import TestSerializer
from pngmerge.serializerObjects.testserializers import testSerializerObject
from .gomenum import Hand

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


@api_view(['GET'])
@permission_classes([AllowAny])
def img(request, body, hat, weapon):
    bodyimg = Image.open('pngmerge/ImageSource/body/'+ str(body) +'.png').convert("RGBA")
    if hat is not 0:
        hatimg = Image.open('pngmerge/ImageSource/hat/'+ str(hat) +'.png').convert("RGBA")
    if weapon is not 0:
        weaponimg = Image.open('pngmerge/ImageSource/weapon/'+ str(weapon) +'.png').convert("RGBA")

    bg_img = Image.new('RGBA', (bodyimg.width,bodyimg.height), (0, 0, 0, 0))
    bg_img.paste(bodyimg, mask=bodyimg)
    if hat is not 0:
        bg_img.paste(hatimg, mask=hatimg)
    if weapon is not 0:
        bg_img.paste(weaponimg, mask=weaponimg)

    response = HttpResponse(content_type="image/png")
    bg_img.save(response, format="png")
    return response


@api_view(['GET'])
@permission_classes([AllowAny])
def gomimg(request, bg, gom, eye, mouth, head, hand):
    gomimage = Image.open('pngmerge/gomimage/body/'+ str(gomimage) +'.png').convert("RGBA")
    if hat is not 0:
        hatimg = Image.open('pngmerge/gomimage/hat/'+ str(hat) +'.png').convert("RGBA")

    bg_img = Image.new('RGBA', (bodyimg.width,bodyimg.height), (0, 0, 0, 0))
    bg_img.paste(bodyimg, mask=bodyimg)
    if hat is not 0:
        bg_img.paste(hatimg, mask=hatimg)
    if weapon is not 0:
        bg_img.paste(weaponimg, mask=weaponimg)

    response = HttpResponse(content_type="image/png")
    bg_img.save(response, format="png")
    return response


@api_view(['GET'])
@permission_classes([AllowAny])
def enumTest(request, number):
    print(list(Hand))
    print(Hand(number).label)
    print(Hand(number).lower_name())
    print(Hand(number).lower_name_remove_space())
    testObject = testSerializerObject(True)
    serializer = TestSerializer(testObject)
    return Response(serializer.data)