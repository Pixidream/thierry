"""user/models.py
handle user model
"""
# third party
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model,
    for now the class just implements the AbstractUser model,
    expecting to need to add features to the model
    """

    def __str__(self):
        return self.username


class UserProxy(User):
    """
    User proxy,
    avoid conflict with django.contrib.auth.models.User
    when added to admin panel
    """

    class Meta:
        app_label = "auth"
        proxy = True
        verbose_name = "User"
        verbose_name_plural = "Users"
