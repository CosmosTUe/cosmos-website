from cms.models.pluginmodel import CMSPlugin
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField

############################
# Models for Content Cards #
############################
class CardImageLink(CMSPlugin):
    title_text = models.CharField(max_length=50, blank = True)
    content = HTMLField(blank = True)
    image_url = models.CharField(max_length=100, default='', blank = True)
    image_title = models.CharField(max_length=100, default='', blank = True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')
    link_text = models.CharField(max_length=100, default='', blank = True)
    link_destination = models.CharField(max_length=100, default='http://www.cosmostue.nl/', blank = True)

class CardImage(CMSPlugin):
    title_text = models.CharField(max_length=50, blank = True)
    content = HTMLField(blank = True)
    image_url = models.CharField(max_length=100, default='', blank = True)
    image_title = models.CharField(max_length=100, default='', blank = True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')

class CardLink(CMSPlugin):
    title_text = models.CharField(max_length=50, blank = True)
    content = HTMLField(blank = True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')
    link_text = models.CharField(max_length=100, default='', blank = True)
    link_destination = models.CharField(max_length=100, default='http://www.cosmostue.nl/', blank = True)

class Card(CMSPlugin):
    title_text = models.CharField(max_length=50, blank = True)
    content = HTMLField(blank = True)
    color_class = models.CharField(max_length=50, default='grey lighten-5')

#########################
#   Structural Models 	#
#########################
class ColumnPlugin(CMSPlugin):
    name = 'column'

class ParentPlugin(CMSPlugin):
	name = "Parent"

#########################
#     Widget Models 	#
#########################
class SliderModel(CMSPlugin):
    name = 'Slider Model'

class FacebookGalleryModel(CMSPlugin):
    name = 'Cosmos facebook gallery model'

class FacebookEventsModel(CMSPlugin):
    name = 'Cosmos facebook events model'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_nr = models.CharField(max_length=15)
    tue_id = models.CharField(max_length=25)
    card_number = models.CharField(max_length=25)
    key_access = models.CharField(max_length=3)
    member_type = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except:
        Profile.objects.create(user=instance)


class Token(models.Model):
    token = models.CharField(max_length=100)
    device = models.CharField(max_length=50) # the target entity that uses this token

class Door(models.Model):
    is_open = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

class Pi(models.Model):
    ip = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)



