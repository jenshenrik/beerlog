from django.db import models
from datetime import date

# Create your models here.

class Beer(models.Model):
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Batch(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    brew_date = models.DateField('date brewed', default=date.today)
    bottle_date = models.DateField('date bottled', default=date.today)
    og = models.IntegerField(default=1000)
    fg = models.IntegerField(default=1000)
    ibu = models.IntegerField(default=0)

    def __str__(self) -> str:
        return "{} - {}".format(self.beer.name, self.brew_date)

    def calculate_abv(self) -> float:
        return (self.og - self.fg) * 0.13125
