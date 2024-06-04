from rest_framework import serializers
from .models import Game,Developer

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
class DevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

    def validate_ano(self, value):
        if value < 1930 or value > 2040:
            raise serializers.ValidationError("O ano deve estar entre 1930 e 2040.")
        return value

    def validate_nota(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("A nota deve estar entre 0 e 10.")
        return value