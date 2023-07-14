from datetime import datetime
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        start_date_string = self.request.query_params.get('start_date')
        embargo_date_string = self.request.query_params.get('start_date')

        if not start_date_string or not embargo_date_string:
            return Response({'error': 'Please provide both start_date and embargo_date query parameters.'}, status=400)
        
        try:
            start_date = datetime.strptime(start_date_string, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Please provide the start_date in YYYY-MM-DD format.'}, status=400)
                
        try:
            embargo_date = datetime.strptime(embargo_date_string, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Please provide the embargo_date in YYYY-MM-DD format.'}, status=400)
        
        serializer = self.serializer_class(self.filter_queryset(start_date__gte=start_date, embargo_date__lte=embargo_date), many=True)
        return Response(serializer.data, status=200)
            
    def filter_queryset(self, **kwargs):
        return self.queryset.filter(**kwargs)
