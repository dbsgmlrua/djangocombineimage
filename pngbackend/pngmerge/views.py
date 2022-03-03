from django.shortcuts import render
from django.http import HttpResponse

#rest_framworks
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.serializers import Serializer
from rest_framework import status


from .serializers import TestSerializer
from pngmerge.serializerObjects.testserializers import testSerializerObject
from .gomenum import Hand, Bg, Bear, Hat, Mouth, Eye

from PIL import Image

from .serializers import TestSerializer, AttributesSerializer, MetaDataSerializer, MetaDataGetSerializer, ImagePostSerializer
from .models import MetaData

import json
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
    if hat != 0:
        hatimg = Image.open('pngmerge/ImageSource/hat/'+ str(hat) +'.png').convert("RGBA")
    if weapon != 0:
        weaponimg = Image.open('pngmerge/ImageSource/weapon/'+ str(weapon) +'.png').convert("RGBA")

    bg_img = Image.new('RGBA', (bodyimg.width,bodyimg.height), (0, 0, 0, 0))
    bg_img.paste(bodyimg, mask=bodyimg)
    if hat != 0:
        bg_img.paste(hatimg, mask=hatimg)
    if weapon != 0:
        bg_img.paste(weaponimg, mask=weaponimg)

    response = HttpResponse(content_type="image/png")
    bg_img.save(response, format="png")
    return response


@api_view(['GET'])
@permission_classes([AllowAny])
def gomimg(request, bg, gom, eye, mouth, hat, hand):
    bgimage = Image.open('pngmerge/gomimage/Background/'+ Bg(bg).lower_name_remove_space() +'.png').convert("RGBA")
    gomimage = Image.open('pngmerge/gomimage/Bear/'+ Bear(gom).lower_name_remove_space() +'.png').convert("RGBA")
    if eye != 0:
        eyeimage = Image.open('pngmerge/gomimage/Eye/'+ Eye(eye).lower_name_remove_space() +'.png').convert("RGBA")
    if mouth != 0:
        mouthimage = Image.open('pngmerge/gomimage/Mouth/'+ Mouth(mouth).lower_name_remove_space() +'.png').convert("RGBA")
    if hat != 0:
        hatimage = Image.open('pngmerge/gomimage/Hat/'+ Hat(hat).lower_name_remove_space() +'.png').convert("RGBA")
    if hand != 0:
        handimage = Image.open('pngmerge/gomimage/Hand/'+ Hand(hand).lower_name_remove_space() +'.png').convert("RGBA")

    base_img = Image.new('RGBA', (bgimage.width,bgimage.height), (0, 0, 0, 0))
    base_img.paste(bgimage, mask=bgimage)
    base_img.paste(gomimage, mask=gomimage)
    if eye != 0:
        base_img.paste(eyeimage, mask=eyeimage)
    if mouth != 0:
        base_img.paste(mouthimage, mask=mouthimage)
    if hat != 0:
        base_img.paste(hatimage, mask=hatimage)
    if hand != 0:
        base_img.paste(handimage, mask=handimage)
    
    response = HttpResponse(content_type="image/png")
    print("pngmerge/gomimage/result/" + str(bg) + "_" + str(gom) + "_" + str(eye) + "_" + str(mouth) + "_" + str(hat) + "_" + str(hand) + ".png")
    base_img.save("pngmerge/gomimage/result/" + str(bg) + "_" + str(gom) + "_" + str(eye) + "_" + str(mouth) + "_" + str(hat) + "_" + str(hand) + ".png", format="png") 
    base_img.save(response, format="png")
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


@api_view(['GET'])
@permission_classes([AllowAny])
def makeImageAndData(request):
    for a in list(Bg):
        for b in list(Bear):
            for c in list(Eye):
                for d in list(Mouth):
                    for e in list(Hat):
                        for f in list(Hand):
                            savegomimg(a.value,b.value,c.value,d.value,e.value,f.value)
    testObject = testSerializerObject(True)
    serializer = TestSerializer(testObject)
    return Response(serializer.data)


# def savegomimg(bg, gom, eye, mouth, hat, hand):
#     print("pngmerge/gomimage/result/" + str(bg) + "_" + str(gom) + "_" + str(eye) + "_" + str(mouth) + "_" + str(hat) + "_" + str(hand) + ".png")

@api_view(['GET'])
@permission_classes([AllowAny])
def makeGomImage(request, bg, gom, eye, mouth, hat, hand):
    response, base_img = savegomimg(bg, gom, eye, mouth, hat, hand)
    base_img.save(response, format="png")
    return response

def savegomimg(bg, gom, eye, mouth, hat, hand):
    bgimage = Image.open('pngmerge/gomimage/Background/'+ Bg(bg).lower_name_remove_space() +'.png').convert("RGBA")
    gomimage = Image.open('pngmerge/gomimage/Bear/'+ Bear(gom).lower_name_remove_space() +'.png').convert("RGBA")
    if eye != 0:
        eyeimage = Image.open('pngmerge/gomimage/Eye/'+ Eye(eye).lower_name_remove_space() +'.png').convert("RGBA")
    if mouth != 0:
        mouthimage = Image.open('pngmerge/gomimage/Mouth/'+ Mouth(mouth).lower_name_remove_space() +'.png').convert("RGBA")
    if hat != 0:
        hatimage = Image.open('pngmerge/gomimage/Hat/'+ Hat(hat).lower_name_remove_space() +'.png').convert("RGBA")
    if hand != 0:
        handimage = Image.open('pngmerge/gomimage/Hand/'+ Hand(hand).lower_name_remove_space() +'.png').convert("RGBA")

    base_img = Image.new('RGBA', (bgimage.width,bgimage.height), (0, 0, 0, 0))
    base_img.paste(bgimage, mask=bgimage)
    base_img.paste(gomimage, mask=gomimage)
    if eye != 0:
        base_img.paste(eyeimage, mask=eyeimage)
    if mouth != 0:
        base_img.paste(mouthimage, mask=mouthimage)
    if hat != 0:
        base_img.paste(hatimage, mask=hatimage)
    if hand != 0:
        base_img.paste(handimage, mask=handimage)
    
    response = HttpResponse(content_type="image/png")
    print("pngmerge/gomimage/result/" + str(bg) + "_" + str(gom) + "_" + str(eye) + "_" + str(mouth) + "_" + str(hat) + "_" + str(hand) + ".png")
    base_img.save("pngmerge/gomimage/result/" + str(bg) + "_" + str(gom) + "_" + str(eye) + "_" + str(mouth) + "_" + str(hat) + "_" + str(hand) + ".png", format="png")
    return response, base_img


@api_view(['POST'])
@permission_classes([AllowAny])
def metadata(request):
    MetaData.objects.all().delete()
    serializer = MetaDataSerializer(data = request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print('error', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def getmetadata(request):
    data = MetaData.objects.all();
    for d in data:
        att = d.metadata.all()
        d.attributes = att
    serializer = MetaDataGetSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def getmetadatabyid(request, id):
    metadata = MetaData.objects.filter(id=id).first()
    att = metadata.metadata.all()
    metadata.attributes = att
    serializer = MetaDataGetSerializer(metadata, context={'base_url': request.get_host()})
    
        
    with open('pngmerge/gomimage/json/' + str(metadata.id) + '.json', 'w') as jsonfile:
        serializer = MetaDataGetSerializer(metadata)
        json.dump(serializer.data, jsonfile, indent=4)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([AllowAny])
def getmetadatatojson(request):
    data = MetaData.objects.all();
    for d in data:
        att = d.metadata.all()
        d.attributes = att
        
        with open('pngmerge/gomimage/json/' + str(d.id) + '.json', 'w') as jsonfile:
            serializer = MetaDataGetSerializer(d)
            json.dump(serializer.data, jsonfile, indent=4)
            
    serializer = MetaDataGetSerializer(data, many=True)
    return Response(serializer.data)