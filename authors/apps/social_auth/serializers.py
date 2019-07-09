from rest_framework import serializers


class SocialSerailizer(serializers.Serializer):
    access_token = serializers.CharField()