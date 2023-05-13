from django.db import models
from django.utils.text import slugify

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Categorie, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom}"  

class Service(models.Model):
    nom = models.CharField(max_length=50)
    slug = models.SlugField(default="slug")
    libelé = models.TextField(max_length=150)
    thumbnail = models.ImageField(upload_to="services")
    
    def save(self, *args , **kwargs) :
        self.slug = slugify(self.nom)
        super(Service, self).save(*args, **kwargs)
        
    def __str__(self) :
        return f"{self.nom}"


    


class Gallerie(models.Model):
    nom = models.CharField(max_length=50, default="Image")
    slug = models.SlugField(default="slug")
    image = models.ImageField(blank=True, null=True)
    
    def save(self, *args , **kwargs) :
        self.slug = slugify(self.nom)
        super(Gallerie, self).save(*args, **kwargs)
        
    def __str__(self) :
        return f"{self.nom}"
    


class Benin_Mobilier(models.Model):
    nom = models.CharField(max_length=50, default="Image")
    slug = models.SlugField(default="slug")
    image = models.ImageField(blank=True, null=True)
    categorie = models.ForeignKey(Categorie, null=True, blank=True, on_delete=models.CASCADE)

    def save(self, *args , **kwargs) :
        self.slug = slugify(self.nom)
        super(Benin_Mobilier, self).save(*args, **kwargs)
        
    def __str__(self) :
        return f"{self.nom}"