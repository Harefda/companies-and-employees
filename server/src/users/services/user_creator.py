from users.models import User
from app.errors import ObjectAlreadyExists


class CurrencyCreator:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

    def __call__(self):
        if self.allowed_to_create:
            user = self.create_user()
            user.save()
        else:
            return False

    def create_user(self):
        return User.objects.create(
            email=self.email,
            password=self.password
        )

    def allowed_to_create(self, raise_exception=True):
        try:
            if User.objects.filter(email=self.username).exists():
                raise ObjectAlreadyExists
        except ObjectAlreadyExists as exc:
            if raise_exception:
                raise exc
            else:
                return False

        return True

