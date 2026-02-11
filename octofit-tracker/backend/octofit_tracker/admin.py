from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team', 'total_points', 'created_at')
    search_fields = ('name', 'email', 'team')
    list_filter = ('team',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_count', 'total_points', 'created_at')
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'activity_type', 'duration', 'calories', 'points', 'date')
    search_fields = ('user_email', 'activity_type')
    list_filter = ('activity_type', 'date')
    ordering = ('-date',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('rank', 'user_name', 'team', 'total_points', 'updated_at')
    search_fields = ('user_name', 'user_email', 'team')
    list_filter = ('team',)
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'activity_type', 'difficulty', 'duration', 'target_calories')
    search_fields = ('title', 'activity_type')
    list_filter = ('activity_type', 'difficulty')
