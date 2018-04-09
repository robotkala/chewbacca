import os
import django

def createClient(first_name, last_name, email):
    client = Client(first_name=first_name, last_name=last_name, email=email)
    client.save()
    return client

def createExercise(name, description, time):
    exercise = Exercise(name=name, description=description, time=time)
    exercise.save()
    return exercise

def createDailyExercisePlan(name):
    exercisePlan = DailyExercisePlan(name=name)
    exercisePlan.save()
    return exercisePlan

def createWorkoutPlan(name):
    workoutPlan = WorkoutPlan(name=name)
    workoutPlan.save()
    return workoutPlan

def createMembership(client, workoutplan):
    membership = Membership(client=client, workoutplan=workoutplan)
    membership.save()
    return membership

def populate():
    client_1 = createClient(first_name="Luke", last_name="Skywalker", email="luke@tatooine.com")
    client_2 = createClient(first_name="Leia", last_name="Organa", email="leia@alderaan.com")
    client_3 = createClient(first_name="Han", last_name="Solo", email="han@corellia.com")

    exercise_1 = createExercise(name="Pushups", description="40x5 pushups", time="17:00")
    exercise_2 = createExercise(name="Situps", description="40x5 situps", time="17:20")
    exercise_3 = createExercise(name="Pullups", description="10x4 pullups", time="17:40")
    exercise_4 = createExercise(name="Squats", description="50x5 squats", time="18:00")

    daily_exercise_plan_1 = createDailyExercisePlan(name="Exercise Plan 1: A Jump Rope")
    daily_exercise_plan_2 = createDailyExercisePlan(name="Exercise Plan 2: Bad Knee Strikes Back")
    daily_exercise_plan_3 = createDailyExercisePlan(name="Exercise Plan 3: Return of the Cardio")

    workout_plan_1 = createWorkoutPlan(name="Workout Plan 1: Heavy Lifting")
    workout_plan_2 = createWorkoutPlan(name="Workout Plan 2: Fit For Summer")


    daily_exercise_plan_1.exercises.add(exercise_1, exercise_2, exercise_3)
    daily_exercise_plan_1.save()

    daily_exercise_plan_2.exercises.add(exercise_2, exercise_3, exercise_4)
    daily_exercise_plan_2.save()

    daily_exercise_plan_3.exercises.add(exercise_4, exercise_1, exercise_2)
    daily_exercise_plan_3.save()

    workout_plan_1.monday.add(daily_exercise_plan_1)
    workout_plan_1.tuesday.add(daily_exercise_plan_2)

    workout_plan_2.monday.add(daily_exercise_plan_3)
    workout_plan_2.tuesday.add(daily_exercise_plan_2)

    membership_1 = createMembership(client=client_1, workoutplan=workout_plan_1)
    membership_1 = createMembership(client=client_2, workoutplan=workout_plan_2)
    membership_1 = createMembership(client=client_3, workoutplan=workout_plan_1)


if __name__ == '__main__':
    print("Start populating..")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chewbacca.settings')
    django.setup()
    from clients.models import Client, WorkoutPlan, Exercise, DailyExercisePlan, Membership
    populate()
