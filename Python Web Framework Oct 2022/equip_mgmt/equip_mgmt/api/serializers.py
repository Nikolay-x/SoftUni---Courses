from rest_framework import serializers

from equip_mgmt.certificates.models import Certificate
from equip_mgmt.m_activities.models import Activity
from equip_mgmt.manuals.models import Manual
from equip_mgmt.pumps.models import Pump
from equip_mgmt.spares.models import Spares


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'


class SparesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spares
        fields = '__all__'


class PumpSerializer(serializers.ModelSerializer):
    certificate_set = CertificateSerializer(many=True)
    activity_set = ActivitySerializer(many=True)
    manual_set = ManualSerializer(many=True)
    spares_set = SparesSerializer(many=True)

    class Meta:
        model = Pump
        fields = '__all__'


class PumpCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pump
        fields = '__all__'
