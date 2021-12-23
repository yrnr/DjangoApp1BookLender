from django.db.models.signals import post_save
from django.contrib.auth.models import User # sender of the signal
from django.dispatch import receiver # receiver of signal
from .models import Profile

@receiver(post_save, sender=User) 
# When a user is saved, send a signal to this receiver 
# ... which is create_profile function
# Here the signal is post_save, sender is the model User
# When a user is saved, send this signal
# The signal is going to be received by the receiver
# The receriver is create_profile function
# The create_profile function takes all these arguments that our post_save signal passed to it
# One of the arguments is the instance of the User 
# The instance is When a user is created, when a new row is created in in User table
# If the user is created, then create a Profile object with the 'user  = instance of the user created'
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Also trigger a signal when a user is saved, to save the user's profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()