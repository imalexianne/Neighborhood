from django.db import models
from django.contrib.auth.models import User

class Neighborhood(models.Model):
    name = models.CharField(max_length=80, null=True)
    location = models.CharField(max_length=80, null=True)
    occupants=models.IntegerField()
    characteristics=models.TextField()

    def __str__(self):
        return self.name
    @classmethod
    def create_neighborhood(cls,name,location,occupants,characteristics):
        neighborhood=Neighborhood(name=name,location=location,occupants=occupants,characteristics=characteristics)
        return neighborhood
     
    @classmethod
    def find_neighborhood(cls,id):
        neighborhood=cls.objects.get(id=id)
        return neighborhood

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    def update_neighborhood(self,characteristics):
        self.name=characteristics
        self.save()

    def update_occupants(self,num):
        self.occupants=num
        self.save()


class Profile(models.Model):
    first_name=models.CharField(max_length=80,null=True)
    last_name=models.CharField(max_length=80,null=True)
    photo=models.ImageField(upload_to='news/')
    bio=models.TextField()
    email=models.EmailField()
    location= models.CharField(max_length=80,null=True)
    neighborhood=models.CharField(max_length=80,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.first_name

    def save_profile(self):
         self.save()
class Business(models.Model):
    name=models.CharField(max_length=80,null=True)
    location=models.CharField(max_length=100,null=True)
    email=models.EmailField()
    link=models.CharField(max_length=150,null=True)
    neighborhood=models.ForeignKey(Neighborhood,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    @classmethod
    def create_business(cls,name,location,neighborhood,email):
        business=Business(name=name,location=location,email=email,link=link,neighborhood=neighborhood,user=user)
        return business
    @classmethod
    def find_business(cls,id):
        business=cls.objects.get(id=id)
        return business

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    @classmethod
    def search_by_name(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

class Post(models.Model):
    title=models.CharField(max_length=80,null=True)
    image=models.ImageField(upload_to = 'news/')
    caption=models.CharField(max_length=80,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    neighborhood=models.ForeignKey(Neighborhood, null=True)

    def __str__(self):
        return self.title


     


class Health(models.Model):
    name=models.CharField(max_length=80,null=True)
    location=models.CharField(max_length=150,null=True)
    phone_number=models.IntegerField(null=True)
    email = models.EmailField()
    neighborhood=models.OneToOneField(Neighborhood,null=True)
    

    def __str__(self):
        return self.name

class Police(models.Model):
    name=models.CharField(max_length=80,null=True)
    location=models.CharField(max_length=150,null=True)
    phone_number=models.IntegerField(null=True)
    email = models.EmailField()
    neighborhood=models.OneToOneField(Neighborhood,null=True)
    

    def __str__(self):
        return self.name



     


# Create your models here.
