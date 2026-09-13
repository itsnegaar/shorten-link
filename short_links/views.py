from random import random, randint

from django.db import IntegrityError
from django.db.models import Model
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from short_links.models import LinkStorage
from short_links.serializers import ShortLinksSerializerInput, ShortLinksGetSerializerInput


# Create your views here.


class CreateShortLinksView(APIView):

    def post(self, request):
        serializer = ShortLinksSerializerInput(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = str(randint(100000, 999999))
        while True:
            try:
                short_link = serializer.save(original_link=request.data['original_link'], code=code)
            except IntegrityError:
                code = str(randint(100000, 999999))
                continue
            break


        return Response({
            "original_link": short_link.original_link,
            "code": short_link.code,
        }, status=201)


class RetriveShortLinksView(APIView):

    def get(self, request):
        code = request.query_params.get('code')
        link = get_object_or_404(
            LinkStorage,
            code=code
        )

        return redirect(link.original_link)


