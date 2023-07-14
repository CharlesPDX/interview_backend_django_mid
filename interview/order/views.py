from rest_framework.response import Response
from rest_framework import generics, status

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class DeactivateOrderView(generics.UpdateAPIView):
      serializer_class = OrderSerializer
      queryset = OrderTag.objects.all()

      def put(self, request, *args, **kwargs):
        order = self.get_queryset(id=kwargs['id'])
        order.is_active = False
        order.save()
        
        serializer = self.serializer_class(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
