from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    def save(self, **kwargs): 
        # This method exists in the parent class models.Model
        # we are overriding to add some functionality (image resizing)
        print(kwargs.items())
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)