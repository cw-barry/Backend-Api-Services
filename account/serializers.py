from django.contrib.auth.models import User
from rest_framework import serializers, validators
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"}
    )

    password2 = serializers.CharField(
        write_only=True,
        required=False,
        style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = [
            # 'username',
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "password2": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("password2")
        username = validated_data.get("email")

        user = User.objects.create(username = username, **validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, data):
        if data["password2"]:
            if data["password"] != data["password2"]:
                raise serializers.ValidationError(
                    {"password": "Password fields didn't match."})
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            # "username",
            "email",
            "first_name",
            "last_name"
        )

class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only = True)

    class Meta(TokenSerializer.Meta):
        fields = (
            "key",
            "user"
        )
