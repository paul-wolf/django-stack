from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . import models

import logging

logger = logging.getLogger(__name__)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups',)
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)

class FooSerializer(serializers.HyperlinkedModelSerializer):
    """Our own model serializer.

    We might want more than one serializer.
    For instance, if we want to allow some info to be blank
    on create, we can not include those fields.

    """
 
    class Meta:
        model = models.Foo
        fields = ('content',)


