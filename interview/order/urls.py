
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderListView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('embargo/', OrderListView.as_view(), name='order-embargo-list'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]