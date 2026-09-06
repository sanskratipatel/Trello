from rest_framework import serializers 

from users.models  import User 

class SignupSerializer(serializers.ModelSerializer) : 
    password_confirm = serializers.CharField( write_only=True) 
    class Meta: 
        model = User 
        fields = [ 
            'name' , 
            'email' , 
            'password' , 
            'password_confirm'
        ] 
        extra_kwargs = { 
            "password" : { 
                "write_only" : True
            }
        } 
    def validate(self, attrs) : 
        if attrs['password'] != attrs["password_confirm"]: 
            raise serializers.ValidationError( 
                "Password Do not match "
            ) 

        return attrs 
    
    def create(self,validate_data) : 
        validate_data.pop("password_confirm") 
        user = User.objects.create_user( 
            **validate_data
        ) 
        return user 

class LoginSerializer(serializers.Serializer) : 
    email = serializers.EmailField() 
    password = serializers.CharField( 
        write_only=True
    ) 

    def validate(self, attrs) : 
        email = attrs["email"] 
        password = attrs["password"] 

        try: 
            user = User.objects.get(email=email) 
        except User.DoesNotExist: 
            raise serializers.ValidationError( 
                "Invalid Email or Password"
            ) 
        if not user.check_password(password) : 
            raise serializers.ValidationError( 
                "User Account or password"
            ) 
        if not user.is_active: 
            raise serializers.ValidationError( 
                "User Account is Inactive"
            ) 
        attrs["user"] = user 
        return attrs 

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from rest_framework import serializers

from users.models import User


class ForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs["email"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "No account found with this email."
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "User account is inactive."
            )

        attrs["user"] = user

        return attrs

    def save(self, **kwargs):
        user = self.validated_data["user"]

        uid = urlsafe_base64_encode(
            force_bytes(user.pk)
        )

        token = default_token_generator.make_token(user)

        reset_link = (
            f"http://localhost:3000/reset-password/"
            f"{uid}/{token}/"
        )

        print("PASSWORD RESET LINK:")
        print(reset_link)

        return reset_link 

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        try:
            self.token = RefreshToken(attrs["refresh"])
        except TokenError:
            raise serializers.ValidationError(
                "Invalid or expired refresh token."
            )

        return attrs

    def save(self, **kwargs):
        self.token.blacklist()