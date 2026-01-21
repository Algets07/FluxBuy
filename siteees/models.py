from django.db import models

# Create your models here.
class movie(models.Model):
    name =models.CharField(max_length=50)
    desc =models.TextField()
    img =models.ImageField ()

    def __str__  (self):
        return self.name

class reviews(models.Model):
    rating=models.IntegerField()
    comment=models.TextField()
    movie_id=models.IntegerField()




