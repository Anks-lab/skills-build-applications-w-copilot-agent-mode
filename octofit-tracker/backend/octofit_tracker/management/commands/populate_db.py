from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User(email='captain@marvel.com', name='Captain America', team='marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create Activities
        activities = [
            Activity(user=users[0], type='run', duration=30, date=date(2026, 5, 20)),
            Activity(user=users[1], type='cycle', duration=45, date=date(2026, 5, 19)),
            Activity(user=users[2], type='swim', duration=25, date=date(2026, 5, 18)),
            Activity(user=users[3], type='yoga', duration=60, date=date(2026, 5, 17)),
        ]
        Activity.objects.bulk_create(activities)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create Workouts
        workouts = [
            Workout(name='Pushups', description='Do 20 pushups', suggested_for='marvel'),
            Workout(name='Situps', description='Do 30 situps', suggested_for='dc'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
