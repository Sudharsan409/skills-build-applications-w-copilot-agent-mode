from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25, team="Team A")
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team A", description="A test team")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25, team="Team A")
        activity = Activity.objects.create(user=user, activity_type="Running", duration=30, date="2025-04-08")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25, team="Team A")
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Morning Run", description="A quick morning run", duration=30)
        self.assertEqual(workout.name, "Morning Run")