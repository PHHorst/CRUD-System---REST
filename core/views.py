from rest_framework import viewsets
from .models import Game,Developer
from .serializers import GameSerializer,DevSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    
class DevViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DevSerializer