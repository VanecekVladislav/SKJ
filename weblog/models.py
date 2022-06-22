from django.db import models

class Post(models.Model): # todo Models https://docs.djangoproject.com/en/4.0/ref/models/fields/#module-django.db.models.fields
    title = models.CharField(max_length=100)  # todo CharField https://docs.djangoproject.com/en/4.0/ref/forms/fields/#charfield
    body = models.TextField()  # todo TextField https://docs.djangoproject.com/en/4.0/ref/models/fields/#textfield
    pub_date = models.DateTimeField('date published',auto_now_add=True) # todo DateTimeField https://docs.djangoproject.com/en/4.0/ref/models/fields/#datetimefield

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # todo nyní přidělíme podmínku (vztah) 1 post může mít několik komentářů (1 k N)  https://docs.djangoproject.com/en/4.0/ref/models/fields/#foreignkey
    body = models.TextField()
    date = models.DateTimeField('date commented', auto_now_add=True)
