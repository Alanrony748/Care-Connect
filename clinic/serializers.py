from rest_framework import serializers
from clinic.models import DoctorDb,Appointment
from django.utils import timezone

class Doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDb
        fields="__all__"

        # "fields=["id","doctor_name","specialization"]

        read_only_fields=["id"]

#automatic field generation
#default validation
#conversion between model instances and serialized data
#class meta:Defines the serializer's configurations

class Appointment_serializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"
        read_only_fields=["id"]

    def validate(self,validated_data):
        phone=validated_data.get('phone')
        appointment_date=validated_data.get("appointment_date")
        if appointment_date<timezone.localdate():
            raise serializers.ValidationError("Invalid date")
        if Appointment.objects.filter(
            phone=phone,
            appointment_date=appointment_date).exists():
            raise serializers.ValidationError("Already Booked..!")
        else:
            return validated_data