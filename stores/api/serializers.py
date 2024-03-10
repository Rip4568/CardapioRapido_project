from rest_framework import serializers
from stores.models import Store, AddressStore, OpeningHours

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'

class AddressStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressStore
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    opening_hours = OpeningHoursSerializer(many=True, read_only=True)
    address = AddressStoreSerializer(read_only=True)

    class Meta:
        model = Store
        fields = '__all__'