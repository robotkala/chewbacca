from rest_framework import serializers
from clients.models import Client, WorkoutPlan, Exercise, DailyExercisePlan


class ClientSerializer(serializers.ModelSerializer):
    workout_plans = serializers.StringRelatedField(many=True, required=False)
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'workout_plans')


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'time')


class DailyExercisePlanSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = DailyExercisePlan
        fields = ('id', 'name', 'exercises')

class WorkoutPlanSerializer(serializers.ModelSerializer):
    members = ClientSerializer(many=True, required=False)

    monday = DailyExercisePlanSerializer(many=True)
    tuesday = DailyExercisePlanSerializer(many=True)
    wednensday = DailyExercisePlanSerializer(many=True)
    thursday = DailyExercisePlanSerializer(many=True)
    friday = DailyExercisePlanSerializer(many=True)
    saturday = DailyExercisePlanSerializer(many=True)
    sunday = DailyExercisePlanSerializer(many=True)

    class Meta:
        model = WorkoutPlan
        fields = ('id', 'name', 'members', 'monday', 'tuesday', 'wednensday', 'thursday', 'friday', 'saturday', 'sunday')
