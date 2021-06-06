from django.contrib.auth.base_user import BaseUserManager


class MainUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, **extra_fields):
        email: str = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)
