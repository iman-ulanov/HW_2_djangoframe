from rest_framework import serializers


from .models import Employee, Position


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    birth_date = serializers.DateField()
    position = serializers.CharField(max_length=30)
    salary = serializers.IntegerField()

    def create(self, validated_data):
        employee = Employee.objects.create(
            name=validated_data['name'],
            birth_date=validated_data['birth_date'],
            position=validated_data['position'],
            salary=validated_data['salary']
        )
        return employee

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.birth_date = validated_data['birth_date']
        instance.position = validated_data['position']
        instance.salary = validated_data['salary']
        return instance


class PositionSerializer(serializers.Serializer):
    branch = serializers.CharField(max_length=30)
    position = serializers.CharField(max_length=30)


    def create(self, validated_data):
        pos = Position.objects.create(
            branch=validated_data['branch'],
            position=validated_data['position']
        )
        return pos

    def update(self, instance, validated_data):
        instance.branch = validated_data['branch']
        instance.position = validated_data['position']
        return instance
