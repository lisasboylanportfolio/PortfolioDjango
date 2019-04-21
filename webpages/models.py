from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator


class Projects(models.Model):
    name          = models.CharField(max_length=25)
    desc          = models.TextField(max_length=200)
    link          = models.TextField(validators=[URLValidator()], blank=True)
    image         = models.FileField(upload_to='img/', null=True, blank=True)
    created       = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    
    '''
        liked = models.ManyToManyField(
            User,
            related_name="liked_projects",
        )    
    '''
    
    def __str__(self):
        return dict([('name',self.name), ('desc', self.desc), ('link',self.link)])
