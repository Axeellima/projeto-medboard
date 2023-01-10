from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(max_length=100)
    number = serializers.IntegerField(unique=True)
    district = serializers.CharField(max_length=50)
    cep = serializers.IntegerField()
