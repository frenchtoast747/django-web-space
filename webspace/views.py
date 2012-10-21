# Python Imports
import os

# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson

# WebSpace Imports
from webspace import settings
from webspace.models import UserFile

# External Imports
from annoying.decorators import render_to


def handle_uploaded_file( file, filename, user ):
    if not os.path.exists( '%s/%s' % ( settings.FILES_DIR, user.pk ) ):
        os.makedirs( '%s/%s' % ( settings.FILES_DIR, user.pk ) )
    with open( '%s/%s/%s' % ( settings.FILES_DIR, user.pk, filename ), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write( chunk )
    UserFile.objects.create( name=filename, user=user )

@login_required
@render_to( 'webspace/index.html' )
def index( request ):
    if request.method == 'POST':
        if 'fileupload' in request.POST:
            for filename, file in request.FILES.iteritems():
                try:
                    handle_uploaded_file( file, filename, request.user )
                except IntegrityError:
                    response = {}
                    response['error'] = 'existing_file'
                    response['message'] = '%s already exists!' % filename
                    return HttpResponse( simplejson.dumps( response ), mimetype="application/json" )
        
    return {}

@login_required
@render_to( 'webspace/user_file_list.html' )
def displayfilesview( request ):
    files = UserFile.objects.filter( user=request.user )
    return { 'files': files }
    
    

def fileview( request, user_id, slug ):
    user = User.objects.get( pk=user_id )
    file = UserFile.objects.get( user=user, slug=slug )
    return HttpResponse( file.getRealFile() )