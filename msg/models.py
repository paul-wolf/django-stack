import uuid
import hashlib

from django.db import models
from django.contrib.auth.models import User

from strgen import StringGenerator as SG

class UserProfile(models.Model):
    """One way to add information to the user."""
    
    user = models.OneToOneField(User)

    # this is a non-incremental unique id
    # we can use it when we want to have an id in the UI
    # so we don't expose the primary key of the User object
    uid = models.CharField(max_length=12,unique=True)

    # this is a temporary id to associate account confirmation
    # actions with the correct account
    uuid = models.CharField(max_length=120,null=True,blank=True)

    # a flag to indicate the email is validated.
    # Set to false for user to confirm
    email_validated = models.BooleanField(default=False)

    # image of user for showing in comments et al.
    #profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            while True:
                uid = SG("[\w\d]{12}").render()
                if not UserProfile.objects.filter(uid=uid).exists():
                    self.uid =  uid
                    break
        super(UserProfile, self).save(*args, **kwargs) 

class Foo(models.Model):
    """Test model to make sure all is well."""

    content = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        """Insert test data."""
        
        if not self.content:
            self.content = SG("[\w\d]{10}").render()

        super(Foo, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.content
