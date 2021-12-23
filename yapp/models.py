from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    donor = models.ForeignKey(User, on_delete = models.CASCADE)
    date_barrowed = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Gets the URL pattern (not a pattern, but an actual full URL)
        # of the boo-detail page for this perticular book being created/added/updated
        # It also passes the required parameter 'pk' (primary key) to form the URL
        # such as "/book/6". The 6 being the primary key of the created/updated book.
        # The below function reverse() does all that, and returns the URL to the (Book)CreateView.
        # If you do not want this and if you wanted to resirect to the homepage,
        # you could have set an attribute in the CreateView called success_url
        # and set that to the homepage instead.
        return reverse('book-detail', kwargs={'pk': self.pk})
