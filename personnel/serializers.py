from rest_framework import serializers

from .models import Department, Personnel
from django.utils.timezone import now

class PersonnelSerializer(serializers.ModelSerializer):

    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField()

    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        fields = "__all__"
        
    
    def get_days_since_joined(self, obj):
        return (now().date() - obj.date_joined).days


class DepartmentSerializer(serializers.ModelSerializer):
    personnel_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = "__all__"
    
    def get_personnel_count(self, obj):

        return Personnel.objects.filter(department = obj.id).count()

class DepartmentDetailSerializer(serializers.ModelSerializer):

    staff = PersonnelSerializer(many = True, read_only = True)
    class Meta:
        model = Department
        fields = "__all__"