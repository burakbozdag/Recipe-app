from django.db import models

DIFF = (
	('easy', 'Easy'),
	('medium', 'Medium'),
	('hard', 'Hard'),
)

# Create your models here.
class Recipe(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/')
	ingredients = models.TextField()
	description = models.TextField()
	difficulty = models.CharField(max_length=6, choices=DIFF, default='easy')
