from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        # Create Teams
        self.stdout.write('Creating teams...')
        teams_data = [
            {
                'name': 'Team Marvel',
                'description': 'Avengers assemble! The mighty heroes of Marvel unite for fitness.',
                'total_points': 0,
                'member_count': 0
            },
            {
                'name': 'Team DC',
                'description': 'Justice League heroes fighting for fitness and health.',
                'total_points': 0,
                'member_count': 0
            }
        ]
        teams = []
        for team_data in teams_data:
            team = Team.objects.create(**team_data)
            teams.append(team)
            self.stdout.write(f'  Created team: {team.name}')
        
        # Create Users (Superheroes)
        self.stdout.write('Creating users...')
        marvel_heroes = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Steve Rogers', 'email': 'captain@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Wanda Maximoff', 'email': 'scarletwitch@marvel.com', 'team': 'Team Marvel'},
            {'name': 'Carol Danvers', 'email': 'captainmarvel@marvel.com', 'team': 'Team Marvel'},
        ]
        
        dc_heroes = [
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team': 'Team DC'},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team': 'Team DC'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'team': 'Team DC'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'team': 'Team DC'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'team': 'Team DC'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com', 'team': 'Team DC'},
            {'name': 'Victor Stone', 'email': 'cyborg@dc.com', 'team': 'Team DC'},
            {'name': 'Oliver Queen', 'email': 'greenarrow@dc.com', 'team': 'Team DC'},
        ]
        
        users = []
        for hero_data in marvel_heroes + dc_heroes:
            user = User.objects.create(**hero_data)
            users.append(user)
            self.stdout.write(f'  Created user: {user.name} ({user.team})')
        
        # Update team member counts
        teams[0].member_count = len(marvel_heroes)
        teams[0].save()
        teams[1].member_count = len(dc_heroes)
        teams[1].save()
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = [
            {'type': 'Running', 'points_per_min': 10, 'calories_per_min': 12, 'has_distance': True},
            {'type': 'Cycling', 'points_per_min': 8, 'calories_per_min': 10, 'has_distance': True},
            {'type': 'Swimming', 'points_per_min': 12, 'calories_per_min': 14, 'has_distance': True},
            {'type': 'Yoga', 'points_per_min': 5, 'calories_per_min': 4, 'has_distance': False},
            {'type': 'Weight Training', 'points_per_min': 9, 'calories_per_min': 8, 'has_distance': False},
            {'type': 'Boxing', 'points_per_min': 11, 'calories_per_min': 13, 'has_distance': False},
        ]
        
        activities = []
        for user in users:
            # Create 5-8 activities per user
            num_activities = random.randint(5, 8)
            for i in range(num_activities):
                activity_info = random.choice(activity_types)
                duration = random.randint(20, 90)
                distance = round(random.uniform(2.0, 15.0), 2) if activity_info['has_distance'] else None
                calories = duration * activity_info['calories_per_min']
                points = duration * activity_info['points_per_min']
                
                activity_date = date.today() - timedelta(days=random.randint(0, 30))
                
                activity = Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_info['type'],
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    points=points,
                    date=activity_date
                )
                activities.append(activity)
                
                # Update user points
                user.total_points += points
            
            user.save()
        
        self.stdout.write(f'  Created {len(activities)} activities')
        
        # Update team points
        for team in teams:
            team_users = User.objects.filter(team=team.name)
            team.total_points = sum(user.total_points for user in team_users)
            team.save()
        
        # Create Leaderboard
        self.stdout.write('Creating leaderboard...')
        sorted_users = sorted(users, key=lambda u: u.total_points, reverse=True)
        for rank, user in enumerate(sorted_users, start=1):
            Leaderboard.objects.create(
                user_email=user.email,
                user_name=user.name,
                team=user.team,
                total_points=user.total_points,
                rank=rank
            )
        self.stdout.write(f'  Created leaderboard with {len(sorted_users)} entries')
        
        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'title': 'Thor\'s Thunder Run',
                'description': 'Channel the power of Asgard with this intense running workout',
                'activity_type': 'Running',
                'difficulty': 'Hard',
                'duration': 45,
                'target_calories': 540,
                'instructions': '1. Warm up with 5 minutes of light jogging\n2. Sprint for 1 minute at maximum effort\n3. Jog for 2 minutes to recover\n4. Repeat sprint/jog cycle 8 times\n5. Cool down with 5 minutes of walking'
            },
            {
                'title': 'Captain America\'s Shield Circuit',
                'description': 'Build strength and endurance like the First Avenger',
                'activity_type': 'Weight Training',
                'difficulty': 'Medium',
                'duration': 60,
                'target_calories': 480,
                'instructions': '1. 10 push-ups\n2. 15 squats\n3. 20 mountain climbers\n4. 10 pull-ups\n5. 15 lunges (each leg)\n6. Rest 2 minutes\n7. Repeat circuit 4 times'
            },
            {
                'title': 'Wonder Woman\'s Warrior Workout',
                'description': 'Train like an Amazon warrior with this full-body routine',
                'activity_type': 'Boxing',
                'difficulty': 'Hard',
                'duration': 50,
                'target_calories': 650,
                'instructions': '1. Jump rope for 5 minutes\n2. Shadow boxing for 3 minutes\n3. Heavy bag work for 5 minutes\n4. Speed bag for 3 minutes\n5. Repeat cycle 3 times\n6. Cool down with stretching'
            },
            {
                'title': 'Flash\'s Speed Cycle',
                'description': 'Build explosive speed and endurance on two wheels',
                'activity_type': 'Cycling',
                'difficulty': 'Medium',
                'duration': 40,
                'target_calories': 400,
                'instructions': '1. Warm up with 5 minutes of easy cycling\n2. Sprint at maximum effort for 30 seconds\n3. Easy pace for 90 seconds\n4. Repeat sprint/easy cycle 12 times\n5. Cool down with 5 minutes of easy cycling'
            },
            {
                'title': 'Aquaman\'s Ocean Swim',
                'description': 'Master the water with this swimming endurance workout',
                'activity_type': 'Swimming',
                'difficulty': 'Easy',
                'duration': 30,
                'target_calories': 420,
                'instructions': '1. Warm up with 200m easy freestyle\n2. 4 x 100m freestyle at moderate pace\n3. 4 x 50m backstroke\n4. 200m cool down\n5. Focus on smooth, efficient strokes'
            },
            {
                'title': 'Black Widow\'s Flexibility Flow',
                'description': 'Enhance flexibility and mental focus with yoga',
                'activity_type': 'Yoga',
                'difficulty': 'Easy',
                'duration': 45,
                'target_calories': 180,
                'instructions': '1. Start with sun salutations (5 rounds)\n2. Warrior poses sequence (hold each 1 minute)\n3. Balance poses (tree, eagle, dancer)\n4. Seated forward folds\n5. Finish with savasana (10 minutes)'
            },
            {
                'title': 'Hulk Smash Strength Training',
                'description': 'Build massive strength with compound movements',
                'activity_type': 'Weight Training',
                'difficulty': 'Hard',
                'duration': 75,
                'target_calories': 600,
                'instructions': '1. Deadlifts - 5 sets of 5 reps\n2. Bench press - 5 sets of 5 reps\n3. Squats - 5 sets of 5 reps\n4. Overhead press - 4 sets of 8 reps\n5. Barbell rows - 4 sets of 8 reps\n6. Rest 3 minutes between sets'
            },
            {
                'title': 'Spider-Man Agility Run',
                'description': 'Develop speed and agility with interval running',
                'activity_type': 'Running',
                'difficulty': 'Medium',
                'duration': 35,
                'target_calories': 420,
                'instructions': '1. Warm up with 5 minutes of light jogging\n2. Run at 80% effort for 3 minutes\n3. Walk for 1 minute\n4. Repeat 6 times\n5. Cool down with 5 minutes of walking'
            }
        ]
        
        for workout_data in workouts_data:
            workout = Workout.objects.create(**workout_data)
            self.stdout.write(f'  Created workout: {workout.title}')
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Database population completed!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('='*50))
