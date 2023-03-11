from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Staff

class StaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Staff
        fields = ['staff_id', 'firstname', 'lastname', 'phonenumber', 'email_address', 'department', 'gender', 'state_of_origin', 'account_number', 'bank', 'account_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        staff = Staff(**validated_data)
        staff.set_password(password)
        staff.save()
        return staff

class LoginSerializer(serializers.Serializer):
    staff_id = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        staff_id = data.get('staff_id')
        password = data.get('password')

        if staff_id and password:
            staff = authenticate(staff_id=staff_id, password=password)
            if not staff:
                raise serializers.ValidationError('Invalid login credentials')
        else:
            raise serializers.ValidationError('Must include "staff_id" and "password"')

        data['staff'] = staff
        return data
