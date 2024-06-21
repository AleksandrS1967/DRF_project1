from django.shortcuts import render
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from users.serializers import PaymentSerializer
from users.models import Payment


class PaymentCreateAPIView(generics.CreateAPIView):
    """
    создание платежа
    """
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """
    отображение списка платежей, с фильтрацией и сортировкой
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ('date_payment',)
