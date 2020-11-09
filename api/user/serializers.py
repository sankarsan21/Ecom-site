from rest_framework import serializers
from django.contrib.auth.handlers import make_password
from rest_framework.decorators import authentication_classes, permission_classes

from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class meta:

        def create(self, validated_data):
            password = validated_data.pop('password',None)
            instance = self.Meta.model(**validated_data)

            if password in not None:
                instance.set_pssword(password)
            instance.save()
            return instance

        def update(self,instance, validated_data):
            for attr, value in validated_data.items():
                if attr == 'password':
                    instance.set_pssword(value)
                else:
                    setattr(instance,attr,value)

            instance.save()
            return instance  


        model = CustomUser
        extra_kwargs = {'password':{'write_only'=True}}
        fields = {'name','email','password','phone',
                    'gender','is_active','is_staff','is_superuser'}



