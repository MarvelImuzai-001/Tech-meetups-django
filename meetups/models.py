from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f"{self.name} {self.address}"

class Participant(models.Model):
    email = models.EmailField(unique=True)
    
    
    def __str__(self) -> str:
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizers = models.EmailField(max_length=200)
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    participant = models.ManyToManyField(Participant, blank=True)
    
    def __str__(self) -> str:
        return f"{self.title} "
