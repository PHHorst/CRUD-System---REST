from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Developer(models.Model):
        nome= models.CharField(max_length=254,unique=True,)
        Local=models.CharField(max_length=254)
        fundacao= models.IntegerField(validators=[MinValueValidator(1930), MaxValueValidator(2040)],default=2024)
        def __str__(self) -> str:
                return self.nome

class Game(models.Model):
        nome= models.CharField(max_length=50,unique=True)
        tema= models.CharField(max_length=30)
        genero= models.CharField(max_length=30)
        ano= models.IntegerField(validators=[MinValueValidator(1930), MaxValueValidator(2040)],default=2024)
        nota= models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=0)
        desenvolvedora= models.ForeignKey(Developer,on_delete=models.CASCADE)

        def __str__(self) -> str:
                return self.nome
        
