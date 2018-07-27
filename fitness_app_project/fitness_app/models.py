from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    passworld = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Custom_Meal(models.Model):
    ingredients = models.TextField()
    instructions = models.TextField()
    portions = models.TextField()
    macros = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')

class Custom_Circuit(models.Model):
    workouts = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='circuits')
    
# class Workout(models.Model):
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')

# class Food(models.Model):
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foods')
