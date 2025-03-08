from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    type = models.JSONField()
    image = models.URLField()
    
    hp = models.IntegerField(default=45)
    attack = models.IntegerField(default=49)
    defense = models.IntegerField(default=49)
    special_attack = models.IntegerField(default=65)
    special_defense = models.IntegerField(default=65)
    
    def __str__(self):
        return self.title
