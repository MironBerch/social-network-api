from rest_framework.request import Request
from django.shortcuts import get_object_or_404

from accounts.models import User
from posts.models import Post


def get_feed(user: User):
    return Post.objects.feed(user)


def get_post_by_pk(pk: int):
    return get_object_or_404(Post, pk=pk, is_active=True)


def get_recommend_posts(user: User, long: bool):
    return Post.objects.recommend_posts(user=user, long=long)


def get_user_post_by_pk(user: User, pk: int):
    return get_object_or_404(Post, author=user, pk=pk, is_active=True)


def get_liked_posts(user: User):
    return Post.objects.posts().filter(liked=user)


def get_user_profile_posts(user: User):
    return Post.objects.profile_posts(user)


def get_post_by_id(id: int):
    return get_object_or_404(Post, id=id)