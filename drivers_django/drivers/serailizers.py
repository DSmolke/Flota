from rest_framework import serializers
from drivers.models import DriverModel


class DriverModelSerializer(serializers.ModelSerializer):
    """Serialize and deserialize DriverModel objects."""
    class Meta:
        model = DriverModel
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'car_registration']


class DriverSerializer(serializers.Serializer):
    """
    Serializer for the Driver model.

    This serializer is used for serializing and deserializing Driver objects.

    Attributes:
        - id (int): The id of the driver.
        - first_name (str): The first name of the driver.
        - last_name (str): The last name of the driver.
        - phone_number (str): The phone number of the driver.
        - email (str): The email address of the driver.
        - car_registration (str): The car registration number of the driver.

    Methods:
        - create(validated_data): Creates a new Driver object with the given validated data.
        - update(instance, validated_data): Updates an existing Driver object with the given validated data.

    """
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(allow_blank=True, required=False, max_length=50)
    last_name = serializers.CharField(allow_blank=True, required=False, max_length=50)
    phone_number = serializers.CharField(allow_blank=True, required=False, max_length=9)
    email = serializers.CharField(allow_blank=True, required=False, max_length=500)
    car_registration = serializers.CharField(allow_blank=True, required=False, max_length=7)

    def create(self, validated_data):
        """
        Create a new object in the database with the provided validated_data.
        """
        return DriverModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Updates the fields of the given instance with the provided validated data.
        ```
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.car_registration = validated_data.get('car_registration', instance.car_registration)
        instance.save()
        return instance
