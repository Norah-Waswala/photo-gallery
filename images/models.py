
from django.db import models

# Create your models here.


class Location(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
    @classmethod
    def save_location(self):
        self.save()

    @classmethod
    def update_location(self):
        self.update()

    @classmethod
    def delete_location(self):
        self.delete() 

    @classmethod
    def find_locations(cls):
        locations = Location.objects.all()
        return locations

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    @classmethod
    def save_category(self):
        self.save()

    @classmethod
    def update_category(self):
        self.update()

    @classmethod
    def delete_category(self):
        self.delete() 

class Image(models.Model):
    Image=models.ImageField(upload_to = 'images/',default='DEFAULT VALUE')
    Image_Name=models.CharField(max_length=30)
    Image_Description=models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Image_Name
    
   

    @classmethod
    def search_by_category(cls, category):
        image = cls.objects.filter(category__name__icontains=category)
        return image

    @classmethod
    def filter_by_location(cls, location):
        location = Image.objects.filter(location__name=location).all()
        return location
    
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def save_image(self):
        self.save()

    @classmethod
    def update_image(self):
       self.update()

    @classmethod
    def delete_image(self):
        self.delete() 

    class Meta:
        ordering = ['date']