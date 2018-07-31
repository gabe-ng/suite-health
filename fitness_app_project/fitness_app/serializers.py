from rest_framework import serializers
from .models import User, Profile, Custom_Meal, Custom_Circuit, Food


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ()
        depth = 1


class Custom_Meal_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Custom_Meal
        fields = ()
        depth = 1


class Custom_Circuit_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Custom_Circuit
        fields = ()
        depth = 1


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ()
        depth = 1
