from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor', 'Hulk'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman', 'Flash'])

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Tony Stark', team='Marvel', super_hero='Iron Man'),
            User(email='cap@marvel.com', name='Steve Rogers', team='Marvel', super_hero='Captain America'),
            User(email='thor@marvel.com', name='Thor Odinson', team='Marvel', super_hero='Thor'),
            User(email='hulk@marvel.com', name='Bruce Banner', team='Marvel', super_hero='Hulk'),
            User(email='superman@dc.com', name='Clark Kent', team='DC', super_hero='Superman'),
            User(email='batman@dc.com', name='Bruce Wayne', team='DC', super_hero='Batman'),
            User(email='wonderwoman@dc.com', name='Diana Prince', team='DC', super_hero='Wonder Woman'),
            User(email='flash@dc.com', name='Barry Allen', team='DC', super_hero='Flash'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Tony Stark', activity_type='Running', duration=30, date=date.today()),
            Activity(user='Steve Rogers', activity_type='Cycling', duration=45, date=date.today()),
            Activity(user='Clark Kent', activity_type='Swimming', duration=60, date=date.today()),
            Activity(user='Bruce Wayne', activity_type='Weightlifting', duration=50, date=date.today()),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity interval training for heroes.', suggested_for='Marvel'),
            Workout(name='Justice Circuit', description='Circuit training for justice league.', suggested_for='DC'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
