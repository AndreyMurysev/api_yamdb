import csv
import os

from django.conf import settings
from django.core.management import BaseCommand
from django.db import IntegrityError

from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User

PATH = os.path.join(settings.STATICFILES_DIRS[0], 'data')
FILE_NOT_FOUND = 'File {filename} not found in {path}'


class Command(BaseCommand):
    help = 'Добавляет данные из файла CSV в базу данных sqlite3'

    def add_arguments(self, parser):
        parser.add_argument('type', type=str, help='Тип вносимых данных')

    def handle(self, *args, **kwargs):
        data_type = kwargs.get('type')
        filename = data_type + '.csv'
        path = os.path.join(PATH, filename)
        self.stdout.write(path)
        try:
            with open(path, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                data = []
                for row in reader:
                    data.append(row)
        except FileNotFoundError as err:
            self.stdout.write(
                FILE_NOT_FOUND.format(filename=filename, path=PATH)
            )
        print(data)
        if data_type == 'users':
            list_of_user = [
                User(
                    id=user_data.get('id'),
                    username=user_data.get('username'),
                    email=user_data.get('email'),
                    role=user_data.get('role'),
                    bio=user_data.get('bio'),
                    first_name=user_data.get('first_name'),
                    last_name=user_data.get('last_name'),
                )
                for user_data in data
            ]
            try:
                msg = User.objects.bulk_create(list_of_user)
            except IntegrityError:
                pass
        if data_type == 'category':
            list_of_category = [
                Category(
                    id=category_data.get('id'),
                    name=category_data.get('name'),
                    slug=category_data.get('slug')
                )
                for category_data in data
            ]
            try:
                msg = Category.objects.bulk_create(list_of_category)
            except IntegrityError:
                pass
        if data_type == 'genre':
            list_of_genres = [
                Genre(
                    id=genre_data.get('id'),
                    name=genre_data.get('name'),
                    slug=genre_data.get('slug')
                )
                for genre_data in data
            ]
            try:
                msg = Genre.objects.bulk_create(list_of_genres)
            except IntegrityError:
                pass
        if data_type == 'titles':
            list_of_titles = [
                Title(
                    id=title_data.get('id'),
                    name=title_data.get('name'),
                    year=title_data.get('year'),
                    category=Category.objects.get(
                        pk=title_data.get('category')
                    )
                )
                for title_data in data
            ]
            print(list_of_titles)
            try:
                msg = Title.objects.bulk_create(list_of_titles)
                print(msg)
            except IntegrityError:
                pass
        if data_type == 'genre_title':
            list_of_relations = [
                GenreTitle(
                    title_id=Title.objects.get(
                        pk=relation.get('title_id')
                    ),
                    genre_id=Genre.objects.get(
                        pk=relation.get('genre_id')
                )
                )
                for relation in data
            ]
            try:
                GenreTitle.objects.bulk_create(list_of_relations)
            except IntegrityError:
                pass
        if data_type == 'review':
            list_of_reviews = [
                Review(
                    title_id=Title.objects.get(pk=review_data.get('title_id')),
                    text=review_data.get('text'),
                    author=User.objects.get(pk=review_data.get('author')),
                    score=review_data.get('score')
                )
                for review_data in data
            ]
            try:
                msg = Review.objects.bulk_create(list_of_reviews)
            except IntegrityError:
                pass
        if data_type == 'comments':
            list_of_comments = [
                Comment(
                    review_id=Review.objects.get(
                        id=comment_data.get('review_id')
                    ),
                    text=comment_data.get('text'),
                    author=User.objects.get(pk=comment_data.get('author')),
                )
                for comment_data in data
            ]
            try:
                msg = Comment.objects.bulk_create(list_of_comments)
            except IntegrityError:
                pass
