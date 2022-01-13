from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Equip
from .serializers import EquipSerializer

class EquipList(ListCreateAPIView):
    queryset = Equip.objects.all()
    serializer_class = EquipSerializer

class EquipDetail(RetrieveUpdateDestroyAPIView):
    queryset = Equip.objects.all()
    serializer_class = EquipSerializer