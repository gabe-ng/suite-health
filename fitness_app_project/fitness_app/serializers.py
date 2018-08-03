from rest_framework import serializers
from .models import Profile, Custom_Meal, Custom_Circuit, Food, Workout


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','name','age','weight','height')
        depth = 1

class Custom_Meal_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Custom_Meal
        fields = ('id','ingredients','instructions','portions','macros','user')
        depth = 1

class Custom_Circuit_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Custom_Circuit
        fields = ('id','workouts','user')
        depth = 1


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('id','foodId', 'user','label','kcal','protein','fat','carbs')
        depth = 1


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = ('id','author','name','description', 'muscles')
        depth = 1     
