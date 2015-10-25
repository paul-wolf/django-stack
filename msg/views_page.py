import os
import logging
import datetime
import mimetypes
import json
import django
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import Context, RequestContext, Template
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from strgen import StringGenerator as SG

from django.db.models import Q
import codecs
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import models

from . import util

logger = logging.getLogger(__name__)

from django.contrib.auth import authenticate, login


def is_truthy(s):
    return s == 'true'

def home(request):
    """Home page."""
    return render_to_response('home.html',
                              {

                              },
                              context_instance=RequestContext(request))    
    

