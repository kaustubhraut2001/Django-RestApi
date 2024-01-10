from rest_framework import serializers

from .models import Student

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('name', 'rollno',)
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = Student.objects.create_user(**validated_data)
		return user