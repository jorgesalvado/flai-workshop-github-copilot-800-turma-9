from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    total_points = models.IntegerField(default=0)
    member_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField()
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in kilometers
    calories = models.IntegerField()
    points = models.IntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user_email = models.EmailField()
    user_name = models.CharField(max_length=200)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']
    
    def __str__(self):
        return f"{self.rank}. {self.user_name}"


class Workout(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    activity_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)  # Easy, Medium, Hard
    duration = models.IntegerField()  # in minutes
    target_calories = models.IntegerField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.title
