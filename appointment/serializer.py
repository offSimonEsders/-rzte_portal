from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from appointment.models import Appointment
from doctor.serializers import DoctorSerializer


class ReadAppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Appointment
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context.get('request', None)

        if request and request.method == 'GET':
            ret['doctor'] = DoctorSerializer(instance.doctor).data
        else:
            ret['doctor'] = instance.doctor.id

        return ret