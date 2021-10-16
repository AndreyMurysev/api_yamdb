from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from reviews.models import Genre, Category, Title
from users.models import User


MESS_VAL_LOG = 'Отсутствует обязательное поле или оно некорректно'


class AuthenticationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],)
        user.save()
        return user

    def validate(self, data):
        if data['username'] in ('me', 'Me'):
            raise ValidationError(MESS_VAL_LOG)
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'bio',
                  'role',)
        model = User
        ordering = ['-id']


class LoginSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()
        self.fields['confirmation_code'] = serializers.CharField(max_length=6)
        del self.fields['password']

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'token': str(refresh.access_token)}

    def validate(self, data):
        user = get_object_or_404(User, username=data['username'])
        if data['confirmation_code'] != user.confirmation_code:
            raise serializers.ValidationError(MESS_VAL_LOG)
        return self.get_tokens_for_user(user)



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )

    class Meta:
        model = Title
        fields = '__all__'

