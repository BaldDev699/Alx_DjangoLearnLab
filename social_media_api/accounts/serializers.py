from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'following']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = get_user_model().objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            token, created = Token.objects.get_or_create(user=user)
            return {
                'username': user.username,
                'token': token.key
            }
        raise serializers.ValidationError("Invalid Credentials")

class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers_count', 'following_count']

class FollowSerializer(serializers.Serializer):
    target_user_id = serializers.IntegerField()

    def validate_target_user_id(self, value):
        try:
            user = get_user_model().objects.get(id=value)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        return value

    def save(self, **kwargs):
        request_user = self.context['request'].user
        target_user_id = self.validated_data['target_user_id']
        target_user = get_user_model().objects.get(id=target_user_id)

        if request_user == target_user:
            raise serializers.ValidationError("You cannot follow/unfollow yourself")

        if target_user in request_user.following.all():
            request_user.following.remove(target_user)
        else:
            request_user.following.add(target_user)

        return target_user