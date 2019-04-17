from django.db import models
from django.contrib.auth.models import User

class Village(models.Model):
    name = models.CharField(max_length=80, null=True)
    location = models.CharField(max_length=80, null=True)
    occupants=models.IntegerField()
    characteristics=models.TextField()

    def __str__(self):
        return self.name
    @classmethod
    def create_village(cls,name,location,occupants,characteristics):
        village=Village(name=name,location=location,occupants=occupants,characteristics=characteristics)
        return village
     
    @classmethod
    def find_village(cls,id):
        village=cls.objects.get(id=id)
        return village

    def save_village(self):
        self.save()

    def delete_village(self):
        self.delete()

    def update_village(self,characteristics):
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
    village=models.ForeignKey(Village,null=True)
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
    village=models.ForeignKey(Village,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    @classmethod
    def create_business(cls,name,location,village,email):
        business=Business(name=name,location=location,email=email,link=link,village=village,user=user)
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
    village=models.ForeignKey(Village, null=True)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()


     


class Health(models.Model):
    name=models.CharField(max_length=80,null=True)
    location=models.CharField(max_length=150,null=True)
    phone_number=models.IntegerField(null=True)
    email = models.EmailField()
    village=models.ForeignKey(Village, null=True)
    

    def __str__(self):
        return self.name

    def save_health(self):
        self.save()

class Police(models.Model):
    name=models.CharField(max_length=80,null=True)
    location=models.CharField(max_length=150,null=True)
    phone_number=models.IntegerField(null=True)
    email = models.EmailField()
    village=models.ForeignKey(Village, null=True)
    

    def __str__(self):
        return self.name
    def save_police(self):
        self.save()

class Guest(models.Model):
    name=models.CharField(max_length=80,null=False)
    location=models.CharField(max_length=150,null=False)
    phone_number=models.IntegerField(null=True)
    id_number=models.IntegerField(null=True)
    village=models.ForeignKey(Village, null=True)
    

    def __str__(self):
        return self.name

    def save_guest(self):
        self.save()



     


# Create your models here.
