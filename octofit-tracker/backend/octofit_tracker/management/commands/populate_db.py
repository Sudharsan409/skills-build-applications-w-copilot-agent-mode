# Updated the script to use pymongo for dropping collections
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_tracker']

        # Drop collections to clear existing data
        db['octofit_tracker_user'].drop()
        db['octofit_tracker_team'].drop()
        db['octofit_tracker_activity'].drop()
        db['octofit_tracker_leaderboard'].drop()
        db['octofit_tracker_workout'].drop()

        # Create and save users
        thor = User.objects.create(email='thundergod@mhigh.edu', name='Thor', age=30, team='Blue Team')
        tony = User.objects.create(email='ironman@mhigh.edu', name='Tony Stark', age=35, team='Red Team')
        steve = User.objects.create(email='captain@mhigh.edu', name='Steve Rogers', age=32, team='Blue Team')

        # Create and save teams
        blue_team = Team.objects.create(name='Blue Team', description='Team of heroes in blue')
        red_team = Team.objects.create(name='Red Team', description='Team of heroes in red')

        # Create and save activities
        Activity.objects.create(user=thor, activity_type='Running', duration=30, date='2025-04-01')
        Activity.objects.create(user=tony, activity_type='Cycling', duration=45, date='2025-04-02')

        # Create and save leaderboard entries
        Leaderboard.objects.create(user=thor, points=100)
        Leaderboard.objects.create(user=tony, points=150)

        # Create and save workouts
        Workout.objects.create(name='Morning Run', description='A quick morning run', duration=30)
        Workout.objects.create(name='Evening Yoga', description='Relaxing yoga session', duration=60)

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))