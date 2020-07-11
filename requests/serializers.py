from rest_framework import serializers
from .models import Request
from django.contrib.auth import get_user_model
User = get_user_model()

class RequestSerializer(serializers.ModelSerializer):
    requester = serializers.HyperlinkedRelatedField(
        view_name='users:useraccount-detail',
        read_only=True,
    )
    name = serializers.SerializerMethodField()
    status = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    
    class Meta:
        model = Request
        exclude = ['last_edit']

    def get_name (self, obj):
        return obj.requester.first_name
    