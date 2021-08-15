from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='images/', blank=True)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    
    class Meta:
        managed = True
        db_table = 'gameapp_blog'
