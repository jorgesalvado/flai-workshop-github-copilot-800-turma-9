from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserModelTest(TestCase):
    """Test User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name='Test Hero',
            email='test@hero.com',
            team='Team Test',
            total_points=100
        )
    
    def test_user_creation(self):
        """Test user is created correctly"""
        self.assertEqual(self.user.name, 'Test Hero')
        self.assertEqual(self.user.email, 'test@hero.com')
        self.assertEqual(self.user.team, 'Team Test')
        self.assertEqual(self.user.total_points, 100)
    
    def test_user_string_representation(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), 'Test Hero')


class TeamModelTest(TestCase):
    """Test Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Team Test',
            description='Test team description',
            total_points=500,
            member_count=5
        )
    
    def test_team_creation(self):
        """Test team is created correctly"""
        self.assertEqual(self.team.name, 'Team Test')
        self.assertEqual(self.team.description, 'Test team description')
        self.assertEqual(self.team.total_points, 500)
        self.assertEqual(self.team.member_count, 5)
    
    def test_team_string_representation(self):
        """Test team string representation"""
        self.assertEqual(str(self.team), 'Team Test')


class ActivityModelTest(TestCase):
    """Test Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='test@hero.com',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=300,
            points=150,
            date=date.today()
        )
    
    def test_activity_creation(self):
        """Test activity is created correctly"""
        self.assertEqual(self.activity.user_email, 'test@hero.com')
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.distance, 5.0)
        self.assertEqual(self.activity.calories, 300)
        self.assertEqual(self.activity.points, 150)


class LeaderboardModelTest(TestCase):
    """Test Leaderboard model"""
    
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email='test@hero.com',
            user_name='Test Hero',
            team='Team Test',
            total_points=1000,
            rank=1
        )
    
    def test_leaderboard_creation(self):
        """Test leaderboard entry is created correctly"""
        self.assertEqual(self.entry.user_email, 'test@hero.com')
        self.assertEqual(self.entry.user_name, 'Test Hero')
        self.assertEqual(self.entry.team, 'Team Test')
        self.assertEqual(self.entry.total_points, 1000)
        self.assertEqual(self.entry.rank, 1)


class WorkoutModelTest(TestCase):
    """Test Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            title='Test Workout',
            description='A test workout',
            activity_type='Running',
            difficulty='Medium',
            duration=45,
            target_calories=400,
            instructions='1. Warm up\n2. Run\n3. Cool down'
        )
    
    def test_workout_creation(self):
        """Test workout is created correctly"""
        self.assertEqual(self.workout.title, 'Test Workout')
        self.assertEqual(self.workout.activity_type, 'Running')
        self.assertEqual(self.workout.difficulty, 'Medium')
        self.assertEqual(self.workout.duration, 45)
        self.assertEqual(self.workout.target_calories, 400)


class APIRootTest(APITestCase):
    """Test API root endpoint"""
    
    def test_api_root(self):
        """Test API root returns correct endpoints"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
    
    def test_root_redirects_to_api(self):
        """Test root URL points to API"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserAPITest(APITestCase):
    """Test User API endpoints"""
    
    def setUp(self):
        self.user = User.objects.create(
            name='API Test Hero',
            email='apitest@hero.com',
            team='Team API',
            total_points=200
        )
        self.url = '/api/users/'
    
    def test_get_users_list(self):
        """Test retrieving users list"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_user(self):
        """Test creating a new user"""
        data = {
            'name': 'New Hero',
            'email': 'newhero@test.com',
            'team': 'Team New',
            'total_points': 0
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)


class TeamAPITest(APITestCase):
    """Test Team API endpoints"""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='API Team',
            description='API test team',
            total_points=1000,
            member_count=10
        )
        self.url = '/api/teams/'
    
    def test_get_teams_list(self):
        """Test retrieving teams list"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_team(self):
        """Test creating a new team"""
        data = {
            'name': 'New Team',
            'description': 'A new test team',
            'total_points': 0,
            'member_count': 0
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)


class ActivityAPITest(APITestCase):
    """Test Activity API endpoints"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='activity@test.com',
            activity_type='Cycling',
            duration=60,
            distance=20.0,
            calories=500,
            points=400,
            date=date.today()
        )
        self.url = '/api/activities/'
    
    def test_get_activities_list(self):
        """Test retrieving activities list"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_activity(self):
        """Test creating a new activity"""
        data = {
            'user_email': 'newactivity@test.com',
            'activity_type': 'Swimming',
            'duration': 45,
            'distance': 2.0,
            'calories': 400,
            'points': 450,
            'date': date.today().isoformat()
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 2)


class LeaderboardAPITest(APITestCase):
    """Test Leaderboard API endpoints"""
    
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            user_email='leader@test.com',
            user_name='Top Leader',
            team='Team Leaders',
            total_points=5000,
            rank=1
        )
        self.url = '/api/leaderboard/'
    
    def test_get_leaderboard_list(self):
        """Test retrieving leaderboard list"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class WorkoutAPITest(APITestCase):
    """Test Workout API endpoints"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            title='API Test Workout',
            description='Workout for API testing',
            activity_type='Boxing',
            difficulty='Hard',
            duration=50,
            target_calories=600,
            instructions='1. Warm up\n2. Box\n3. Cool down'
        )
        self.url = '/api/workouts/'
    
    def test_get_workouts_list(self):
        """Test retrieving workouts list"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_workout(self):
        """Test creating a new workout"""
        data = {
            'title': 'New Workout',
            'description': 'A new test workout',
            'activity_type': 'Yoga',
            'difficulty': 'Easy',
            'duration': 30,
            'target_calories': 150,
            'instructions': 'Stretch and relax'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 2)
