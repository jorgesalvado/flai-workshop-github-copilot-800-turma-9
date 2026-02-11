from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'team', 'total_points', 'created_at']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'total_points', 'member_count', 'created_at']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user_email', 'activity_type', 'duration', 'distance', 'calories', 'points', 'date', 'created_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user_email', 'user_name', 'team', 'total_points', 'rank', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'title', 'description', 'activity_type', 'difficulty', 'duration', 'target_calories', 'instructions', 'created_at']
