from rest_framework import serializers
from .models import Expense


class ExpenseSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['date', 'description', 'amount', 'category']
