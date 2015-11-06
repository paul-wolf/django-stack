# -*- coding: utf-8 -*-
"""
This is for API views.
"""
from __future__ import absolute_import

import datetime
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from . models import Foo
from . serializers import *

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError

from rest_framework import permissions
from rest_framework import serializers
from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404


import logging

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MyPagination(pagination.PageNumberPagination):
    """Sample pagination object.

    You probably want your pages to be smaller. 

    """
    
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class IsOwnerPermission(permissions.BasePermission):
    """
    Sample permission object.
    """

    def has_object_permission(self, request, view, obj):
        # if our object had an 'owner' field, we might do this:
        # return obj.owner == request.user
        return True


# Here is a ModelViewSet that will expose Foo objects in a REST interface

class FooViewSet(viewsets.ModelViewSet):
    """Foo REST interface.

    This is all we need to make this work along with the serializer.

    """

    queryset = Foo.objects.all()
    serializer_class = FooSerializer
    pagination_class = MyPagination
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerPermission,)
                        

    @detail_route(methods=['post'], url_path='example_detail_route')
    def example_detail_route(self, request, pk=None):
        """Here's how you can create an arbitrary method."""
        pass

    def list(self, request):
        """You don't have to have this explicitly.
        
        But it will be useful if you need to override 
        something in getting a list of foo.

        """
        queryset = Foo.objects.all()
        serializer = FooSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """You do not need this. Just an example of overriding it."""
        serializer = FooSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'})
        else:
            logger.error(serializer.errors)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            
    def update(self, request, pk):
        """You do not need this. Just an example of overriding it."""

        foo = Foo.objects.get(uid=pk)
        serializer = FooSerializer(instance=foo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'})
        else:
            logger.error(serializer.errors)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
                                                                     

    def destroy(self, request, pk):
        """You don't need this. Just an example of overriding it."""
        foo = self.get_object()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_serializer_class(self):
        """You might want to return different 
        serializers for creating vs. updating.

        We only have one, but this shows how you could return different ones.

        """
        
        if self.action == 'list':
            return FooSerializer
        elif self.action == 'retrieve':
            return FooSerializer
        elif self.action == 'create':
            return FooSerializer
        return FooSerializer
                                   


@api_view(['GET'])
def foojitsu(request):
    """
    Vanilla GET request that doesn't need a model.
    """

    if request.method == 'GET':
        try:
            data['status'] = 'ok'
            return Response(data)
        except Foo.DoesNotExist:
            return Response("")
