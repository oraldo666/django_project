from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    decription = models.CharField(max_length=250)
    # The path that images will be saved :
    image = models.ImageField(upload_to='portfolio/images/')
    # blank=True so u dont necesary need to fill this url model
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email