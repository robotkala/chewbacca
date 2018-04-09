from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from clients.models import Client, WorkoutPlan, Exercise, DailyExercisePlan
from clients.serializers import ClientSerializer, WorkoutPlanSerializer, ExerciseSerializer, DailyExercisePlanSerializer

class ClientList(APIView):
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WorkoutPlanList(APIView):
    def get(self, request, format=None):
        workout_plan_list = WorkoutPlan.objects.all()
        serializer = WorkoutPlanSerializer(workout_plan_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkoutPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutDetail(APIView):
    def get_object(self, pk):
        try:
            return WorkoutPlan.objects.get(pk=pk)
        except WorkoutPlan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        workout_plan = self.get_object(pk)
        serializer = WorkoutPlanSerializer(workout_plan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        workout_plan = self.get_object(pk)
        serializer = WorkoutPlanSerializer(workout_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        workout_plan = self.get_object(pk)
        workout_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DailyExercisePlanList(APIView):
    def get(self, request, format=None):
        exercise_plan_list = DailyExercisePlan.objects.all()
        serializer = DailyExercisePlanSerializer(workout_plan_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DailyExercisePlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DailyExercisePlan(APIView):
    def get_object(self, pk):
        try:
            return DailyExercisePlan.objects.get(pk=pk)
        except DailyExercisePlan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)
        serializer = DailyExercisePlanSerializer(exercise_plan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)
        serializer = DailyExercisePlanSerializer(workout_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exercise_plan = self.get_object(pk)
        exercise_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExerciseList(APIView):
    def get(self, request, format=None):
        exercise_list = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        exercise = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseDetail(APIView):
    def get_object(self, pk):
        try:
            return Exercise.objects.get(pk=pk)
        except DailyExercisePlan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(exercise_plan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(workout_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exercise = self.get_object(pk)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
