from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail

class Client(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    workout_plans = models.ManyToManyField('WorkoutPlan', through="Membership", blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.last_name


class Exercise(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=254, blank=True)
    time = models.TimeField(blank=True)

    class meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

class DailyExercisePlan(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField('Exercise', blank=True)

    class meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField('Client', through="Membership", blank=True)

    monday = models.ManyToManyField('DailyExercisePlan', related_name="monday", blank=True)
    tuesday = models.ManyToManyField('DailyExercisePlan', related_name="tuesday", blank=True)
    wednensday = models.ManyToManyField('DailyExercisePlan', related_name="wednensday", blank=True)
    thursday = models.ManyToManyField('DailyExercisePlan', related_name="thursday", blank=True)
    friday = models.ManyToManyField('DailyExercisePlan', related_name="friday", blank=True)
    saturday = models.ManyToManyField('DailyExercisePlan', related_name="saturday", blank=True)
    sunday = models.ManyToManyField('DailyExercisePlan', related_name="sunday", blank=True)

    class meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Membership(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    workoutplan = models.ForeignKey('WorkoutPlan', on_delete=models.CASCADE)


def workout_edit(sender, instance, created, **kwargs):
    if created:
        print("A new workout plan has been created")
    else:
        # workout has been edited
        specific_workout = WorkoutPlan.objects.get(name=instance)
        member_list = specific_workout.members.all()

        for member in member_list:

            # send email to user
            '''
            send_mail(
                'Workout update',
                'Your workout details have changed',
                'oskarkala@gmail.com',
                member.email,
                fail_silently=False,
            )
            '''

            print("A workout has been edited. An email has been sent to: ", member.email)

def new_membership(sender, instance, created, **kwargs):
    member = instance.client

    # send email to user
    '''
    send_mail(
        'New workout schedule',
        'You have been added to a new workout group',
        'oskarkala@gmail.com',
        member.email,
        fail_silently=False,
    )
    '''

    print("A member has been added to a new workout group. An email has been sent to: ", member.email)

post_save.connect(workout_edit, sender=WorkoutPlan)
post_save.connect(new_membership, sender=Membership)
