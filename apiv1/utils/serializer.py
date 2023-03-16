from rest_framework import serializers

from users.utils import CellphoneField

class CellphoneSerializer(serializers.Serializer):
    
    cell = CellphoneField()