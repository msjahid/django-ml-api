from rest_framework import serializers


class SalaryInputSerializer(serializers.Serializer):
    YearsExperience = serializers.FloatField()

    def validate_YearsExperience(self, value):
        if value < 0:
            raise serializers.ValidationError('YearsExperience must be a non-negative value.')
        return value


