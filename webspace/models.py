# Python Imports
import os

# Django Imports
from django.db import models
from django.contrib.auth.models import User

# WebSpace imports
from webspace import settings

# Create your models here.
class UserFile( models.Model ):
    # the filename
    slug = models.SlugField( max_length=1024 )
    name = models.CharField( max_length=100 )
    user = models.ForeignKey( User )
    uploaded_date = models.DateTimeField( auto_now_add=True )
    share = models.BooleanField( default=False )
    
    class Meta:
        unique_together = ('name', 'user',)
    
    def __unicode__( self ):
        return self.name
    
    def get_absolute_url( self ):
        return '/%s/%s/%s' % ( settings.FILES_DIR_NAME, self.user.pk, self.slug )
    
    def save( self, *args, **kwargs ):
        self.slug = self.name.replace( r' ', '_' )
        super( UserFile, self ).save( *args, **kwargs )
    
    def delete( self, *args, **kwargs ):
        self.deleteRealFile()
        super( UserFile, self ).delete( *args, **kwargs )
        
    @property
    def filePath( self ):
        return '%s/%s/%s' % ( settings.FILE_STORAGE, self.user.pk, self.name )
    
    def getRealFile( self ):
        return open( self.filePath, 'r+' )
    
    def deleteRealFile( self ):
        os.remove( self.filePath )
    
    def toggleShare( self ):
        self.share = not self.share
        self.save()