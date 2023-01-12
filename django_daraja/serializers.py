from rest_framework import serializers

from .models import Hro

class HroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hro
        fields = ('MSISDN', 'accessPoint','sessionID','input')