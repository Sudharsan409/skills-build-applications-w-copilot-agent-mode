from djongo import models
from bson import ObjectId

def generate_object_id():
    return str(ObjectId())

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_object_id)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    team = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_object_id)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_object_id)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.name}"

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_object_id)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.user.name}: {self.points} points"

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_object_id)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes

    def __str__(self):
        return self.name